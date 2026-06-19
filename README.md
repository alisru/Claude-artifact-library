# Claude Artifact Library

This repo is a raw, ongoing log of artifacts Claude produces across conversations with alisru. It is not a curated showcase. It is not organised by topic or project. It is organised by chat, in the order things were actually built.

## How it works

Every conversation that produces one or more artifacts gets its own folder at the root of this repo.

Folder naming: `chat-name-ddmmyy`

- `chat-name` is a short, lowercase, hyphenated slug describing the chat (no spaces, ever)
- `ddmmyy` is the date the chat happened, two digits each for day, month, year, no separators

Example: a chat about GitHub artifact versioning on 19 June 2026 becomes `github-artifact-versioning-190626`.

## What goes in a chat folder

The first artifact created in a chat creates a new file inside that chat's folder. Every artifact made later in that same chat goes into the same folder.

If an artifact gets revised later in that same chat, the revision is committed to the same file path, not a new file. That means the file's own commit history on GitHub is the version history for that artifact. Nothing gets overwritten and lost. Every version is one commit back.

New chat, new folder. Always. Nothing from a new chat gets merged backward into an old chat's folder, even if the new chat is continuing the same idea or fixing the same artifact. The folder boundary is the chat boundary, not the topic boundary.

## What this repo deliberately is not

- It is not a portfolio. Half-finished, abandoned, or superseded artifacts stay in the log.
- It is not deduplicated across chats. If the same idea gets rebuilt in three different chats, there are three folders.
- It is not retroactive. This system covers artifacts from the point the system was set up onward. Anything built before that in earlier chats is not in here.

## Reading the history

To see every version of one specific artifact: open the file directly and look at its commit history.

To see everything that happened in one conversation: open that chat's folder and look at all the files inside it.

To see everything across all conversations: this is the root of the repo, scroll the folder list.
