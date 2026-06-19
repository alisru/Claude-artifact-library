# How I Pull Things Back Out of the Artifact Library

This covers the read side of the system: how retrieval actually works once something is committed to alisru/Claude-artifact-library, what I can and can't do with it, and where the limits are.

## The short version

GitHub indexes everything it stores automatically, that's just baseline functionality on any repo. What makes that indexing actually useful for you specifically is the folder convention we're running: every chat gets its own dated folder, every artifact from that chat lives at a consistent path inside it, and revisions get committed to the same path instead of a new one. Search works on any repo. Search being useful depends on the structure underneath it, and that part isn't automatic, it's the convention we agreed on.

## The three retrieval modes

**Whole file by path.** If I know roughly where something lives, I fetch it directly. This is the fastest and most reliable mode because it skips search entirely, I'm just asking GitHub for a specific file at a specific path.

**Search by filename or path.** Useful when you remember what something was called but not which folder it ended up in. This searches across the whole repo for matching file or path names.

**Search by content.** Useful when you remember a phrase, term, or concept that was in a file but you don't remember the filename or folder. This is GitHub's code search reaching into file contents, not just names.

There's a fourth mode worth naming separately: listing a folder. Since folders are dated, "what's in the convergence-lite folder" or "show me everything from mid June" is really just a directory listing, not a search at all. It's the cheapest and most exact of the four when you know roughly when something happened.

## Getting parts of a file, not the whole thing

There's no API call that does "give me lines 40 to 80" directly. What happens instead: I pull the full file content back, then slice it down to whatever section you actually need on my end. For a normal sized file this is trivial and basically instant. For something genuinely huge, a large log or a big generated JSON, pulling the whole thing first gets unwieldy, so in that case I'd run a content search first to find the matching line, then pull just enough surrounding context rather than the entire file.

## Pulling history, not just current state

Because revisions get committed to the same path rather than a new file, the commit history on any given file is its full version history. I can pull an older version of a file at a specific commit and diff it against the current version, which means "what did this look like before the last change" is answerable directly from git rather than from anything I'd have to remember.

## What this depends on

The whole thing rests on the folder and naming convention actually being followed every time. The README specifies: a new chat always gets a new folder, even if it's continuing the same idea or fixing the same artifact from a different chat. Nothing gets merged backward. That's a deliberate design choice documented in the README, not a limitation, but it does mean the repo is a raw chronological log, not a deduplicated, organized library. If the same idea gets rebuilt across three different chats, there will be three folders, not one canonical one.

Current state of the repo as of this writeup: one real chat folder exists at github-mcp-test-190626. There's also a stray file at root, lowercase readme with no extension, sitting alongside the proper README.md. That file doesn't follow the dated folder convention, it's a small inconsistency in an otherwise clean structure, worth knowing about since it's the kind of thing that could confuse a future content search if it grows.

## Limitations, plainly stated

Search quality depends entirely on the convention holding. If a future artifact gets committed without the folder pattern, it still exists and is still fetchable by direct path, but it becomes harder to find by search alone since the structure that makes search useful would be partially broken for that one item.

This system only covers what's been committed since the system was set up. The README is explicit that it's not retroactive, anything built in earlier chats before this convention existed isn't in the repo and isn't searchable this way.

Code search on GitHub is good but it's not semantic. It matches on filenames, paths, and literal text content. If you remember the gist of an idea but not any of the actual words used in the file, content search may not surface it, and the better move in that case is a folder listing by approximate date instead.

Large files are the one case where pulling the whole thing isn't free. Most of what's in here will be markdown, HTML, or JSON well under any size that matters, but anything that grows into the hundreds of KB range is better approached through content search plus targeted context rather than a full fetch.

## Practical shortcuts

Knowing roughly when something happened is the strongest lever you have, since it turns a search into a direct folder listing. Knowing the exact phrase or term used in the file is the second strongest lever, since it turns a vague memory into a precise content search. Knowing neither is still workable, it just means I'd search broader and narrow down with you rather than landing on the right file in one call.
