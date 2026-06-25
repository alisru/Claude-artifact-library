# Local AI Activity Tracker — Architecture

A local-first, read-only PC activity observer with a multi-agent summarisation pipeline and a queryable context cache. No cloud dependency required. Designed for a 32GB RAM + GTX 1660 Super (6GB VRAM) system running Ollama.

---

## Concept

The system passively observes meaningful PC activity, compresses it through a layered agent pipeline, and stores structured context in a local cache. A query interface lets you ask "what have I been doing" style questions against the accumulated context. Nothing is sent off-device.

---

## Event Taxonomy

Not all events are worth capturing. The relevance filter is the first agent in the pipeline and its only job is to decide what gets processed downstream.

### Capture

- Tab switch — URL, page title, timestamp
- New tab opened — URL, page title
- Document open — file path, file type, timestamp
- File save — file path, timestamp
- Application focus change — app name, window title, timestamp
- Clipboard copy — content snippet (truncated at 500 chars), source app
- Browser address bar navigation — URL entered directly (catches searches and manual nav)
- PDF/document viewed — file path, page range if detectable

### Discard

- Tab switches under 10 seconds (accidental or transient)
- Application focus under 5 seconds
- Repeated clipboard copies of the same content within a session
- System app focus (Task Manager, Settings, Calculator, etc.)
- Duplicate URL visits within 30 minutes in the same session

---

## Cache Schema

Three layers. Each layer feeds the next. The query model only sees Layer 2 and Layer 3.

### Layer 1 — Raw Event Log (Hot)

Append-only JSON lines file. Rolling window, last 2 hours retained in full.

```
{
  "ts": "2026-06-26T14:23:11",
  "type": "tab_switch",
  "url": "https://example.com/article",
  "title": "Article Title",
  "summary": null,
  "tags": null,
  "session_id": "session_20260626_1400"
}
```

Types: `tab_switch`, `tab_open`, `doc_open`, `file_save`, `app_focus`, `clipboard`, `nav`

Summary and tags are null at Layer 1, filled in by the tab/page agent before the record is promoted to Layer 2.

### Layer 2 — Session Blocks (Warm)

Structured JSON files, one per session. A session is defined as a continuous activity window with no gap longer than 20 minutes.

```
{
  "session_id": "session_20260626_1400",
  "start": "2026-06-26T14:00:00",
  "end": "2026-06-26T15:42:00",
  "duration_minutes": 102,
  "apps": ["Chrome", "VS Code", "Obsidian"],
  "topics": ["local LLM", "activity tracker", "Python event capture"],
  "projects": ["activity-tracker-build"],
  "urls_visited": [
    {
      "url": "https://example.com",
      "title": "Page Title",
      "summary": "Two sentence summary of page content.",
      "tags": ["llm", "ollama", "local"]
    }
  ],
  "docs_opened": [
    {
      "path": "C:/Projects/tracker/capture.py",
      "type": "python",
      "summary": "Event capture module"
    }
  ],
  "session_summary": "Working on local activity tracker architecture. Researched Ollama model options, reviewed pynput and Chrome DevTools Protocol docs, edited capture.py."
}
```

### Layer 3 — Topic/Project Index (Cold)

Single JSON file, continuously updated by the topic tracker agent.

```
{
  "projects": {
    "activity-tracker-build": {
      "first_seen": "2026-06-26T14:00:00",
      "last_seen": "2026-06-26T15:42:00",
      "session_count": 3,
      "total_minutes": 240,
      "related_topics": ["local LLM", "Python", "event capture", "Ollama"],
      "urls": ["https://..."],
      "files": ["C:/Projects/tracker/capture.py"]
    }
  },
  "topics": {
    "local LLM": {
      "first_seen": "2026-06-26T14:00:00",
      "last_seen": "2026-06-26T15:42:00",
      "session_count": 2,
      "related_projects": ["activity-tracker-build"]
    }
  }
}
```

### Layer 3b — Vector Store (Semantic Search)

Each session block summary is embedded and stored in a local Chroma or Qdrant instance. Used for semantic queries like "when did I last read about X" where keyword matching fails.

Embedding model: `nomic-embed-text` via Ollama. Tiny, fast, stays local.

---

## Agent Pipeline

Five agents. All run locally. Small models (1-3B) for the continuous agents, larger query model GPU-resident for the interface.

### Agent 1 — Relevance Filter

- Trigger: every raw event from the capture layer
- Model: Qwen3 1.7B (CPU)
- Input: raw event JSON
- Output: pass/discard decision + event type classification
- Task: apply the discard rules above, classify ambiguous events

### Agent 2 — Tab/Page Summariser

- Trigger: tab_switch or tab_open events that pass the filter
- Model: Qwen3 1.7B (CPU)
- Input: page title + scraped page text (first 2000 chars via Chrome DevTools Protocol)
- Output: 2-sentence summary + topic tags array
- Writes back to the Layer 1 event record before Layer 2 promotion

### Agent 3 — Session Compiler

- Trigger: scheduled, every 30 minutes or on session close (20 min inactivity)
- Model: Qwen3 1.7B (CPU)
- Input: all Layer 1 events from the current session window
- Output: complete Layer 2 session block JSON
- Task: aggregate, deduplicate, identify topics and project references, write session summary

### Agent 4 — Topic/Project Tracker

- Trigger: after each new session block is written
- Model: Qwen3 1.7B (CPU)
- Input: new session block + current Layer 3 index
- Output: updated Layer 3 index
- Task: identify new projects and topics, update last_seen timestamps, merge related entities

### Agent 5 — Query Interface

- Trigger: on demand, user invokes hotkey or CLI
- Model: Qwen3 7B Q4_K_M (GPU, 1660 Super VRAM)
- Input: Layer 3 topic/project index + last N session blocks (default 5) + vector search results for the query
- Output: natural language answer
- Task: answer questions about activity, summarise recent work, find when something was last seen

---

## Event Capture Layer

Python-based. Three capture hooks running as threads.

### Chrome DevTools Protocol (CDP)

Connects to Chrome via `--remote-debugging-port=9222`. Listens for `Page.frameNavigated` and `Target.targetInfoChanged` events. On tab switch, fetches `Runtime.evaluate` to extract page text. No browser extension needed, no permissions beyond launching Chrome with the debug flag.

```
chrome.exe --remote-debugging-port=9222
```

### Filesystem Watcher

`watchdog` library. Watches configured directories (Documents, Projects, Downloads, Desktop). Events: file created, file modified (debounced to avoid spam on autosave).

### Application Focus

`pywinauto` or raw `win32api` via `pywin32`. Polls foreground window every 2 seconds, emits focus event on change.

### Clipboard

`pyperclip` with a polling loop or `pynput` keyboard hook to catch Ctrl+C. Captures content and source window title.

---

## Model Stack

| Role | Model | Runtime | RAM/VRAM |
|---|---|---|---|
| Relevance Filter | Qwen3 1.7B Q4 | CPU (Ollama) | ~1.2GB RAM |
| Tab Summariser | Qwen3 1.7B Q4 | CPU (Ollama) | ~1.2GB RAM (shared instance) |
| Session Compiler | Qwen3 1.7B Q4 | CPU (Ollama) | same instance |
| Topic Tracker | Qwen3 1.7B Q4 | CPU (Ollama) | same instance |
| Embedding | nomic-embed-text | CPU (Ollama) | ~0.3GB RAM |
| Query Interface | Qwen3 7B Q4_K_M | GPU (Ollama) | ~4.5GB VRAM |

The four small agents share one Ollama instance with the 1.7B model resident. They run sequentially via a task queue, not in parallel, so memory stays flat. Total resident footprint: ~3GB RAM + 4.5GB VRAM. Well within budget.

---

## Directory Structure

```
tracker/
  capture/
    chrome_cdp.py       # Chrome tab event capture
    filesystem.py       # File open/save watcher
    app_focus.py        # Foreground window tracker
    clipboard.py        # Clipboard monitor
  agents/
    filter.py           # Relevance filter agent
    summariser.py       # Tab/page summariser agent
    session.py          # Session compiler agent
    topics.py           # Topic/project tracker agent
  cache/
    events/             # Layer 1 rolling JSON lines (per day)
    sessions/           # Layer 2 session block JSON files
    index.json          # Layer 3 topic/project index
    vectors/            # Chroma vector store
  query/
    interface.py        # CLI query interface, hotkey listener
  orchestrator.py       # Main loop, event routing, agent task queue
  config.json           # Watch dirs, discard rules, model names, thresholds
```

---

## Query Interface

Simple CLI to start. `python query/interface.py` opens a prompt. Hotkey (configurable) raises it from anywhere on the desktop via `pynput` global hotkey listener.

Example queries the system should handle:

- "What have I been working on today"
- "When did I last look at something about X"
- "What tabs did I have open this afternoon"
- "What files was I editing yesterday"
- "What projects have I touched this week"

The query agent loads the Layer 3 index, pulls the last 5 session blocks, runs a vector search for the query terms, and passes the combined context to the 7B GPU model.

---

## Build Order

1. Chrome CDP capture + raw event log write (Layer 1 skeleton)
2. Relevance filter agent (prune the noise before building anything else)
3. Tab summariser agent (Layer 1 enrichment)
4. Session compiler agent (Layer 2)
5. Query interface against Layer 2 only (validate usefulness before adding complexity)
6. Topic tracker agent + Layer 3 index
7. Vector store + embedding pipeline
8. Filesystem and app focus capture
9. Clipboard capture
10. Hotkey invocation + desktop integration

Validate at step 5 before going further. If the session blocks aren't useful to query against, fix that before adding more data sources.
