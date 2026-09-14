---
name: waste-audit
description: Audit how much of Claude's output in this conversation (visible text and, where available, extended thinking) was load-bearing versus padding that inflated length or token count without adding anything the user needed. Use when the user asks to audit the fluff, run a waste audit, check how much of a response was padding, find out how much a response or chat cost, do a token-waste or cost audit, or asks "how much of that was necessary" / "how much did that messup cost." Distinct from idea-fidelity-audit, which checks whether Claude engaged with what the user meant; this skill checks whether the words that did land needed to be there at all. Run both together only when the user asks for a full audit.
---

# Waste Audit

This exists because inflated responses have a real cost. Not just the user's reading time, but literal token cost, whether billed directly through the API or carried as compute either way. A response can be fully on-topic and still be half padding: throat-clearing before the point, a recap that restates the body in new words, hedges nobody asked for, extra angles manufactured to look thorough. None of that is a comprehension failure (idea-fidelity-audit's territory). It is a response that used more words, and more tokens, than the question required.

## What counts as fluff

- **Preamble padding.** Restating the question back, scene-setting, or framing before getting to the actual content. Anything before the first load-bearing sentence that isn't itself load-bearing.
- **Manufactured caveats.** Disclaimers, hedges, or qualifications the user didn't ask for and that don't change what they'd do with the answer. Not the same as a caveat that's actually decision-relevant, that stays.
- **Redundant restatement.** A closing summary or recap that repeats the body in different words rather than adding anything new. Bullet-point recaps of a paragraph that already said the same thing.
- **Invented complexity.** Extra angles, alternative framings, or "it depends" branches generated to seem thorough rather than because the question needed them. This is the direct token cost of not stopping once a sound answer is reached.
- **Performed narrative voice.** "I want to be direct here," "I won't dodge this," "this surprised me." Narrating the act of answering instead of answering.
- **Unraised-objection defense.** Building a case against a critic, reviewer, or objection the user never voiced.
- **Thinking-block bloat**, where visible. Extended reasoning that re-treads settled ground, restates the prompt back to itself, or performs deliberation without changing the eventual answer.
- **Format fragmentation overhead.** Chopping continuous prose into more headers, bullets, or line breaks than the content needs. Structure should track real divisions in the content, not manufacture them.

## What doesn't count

- Length that's actually load-bearing, depth the question required.
- Detail given because the user asked a follow-up that needed it.
- A list or comparison the user actually requested.
- A caveat that would change what the user does next.

Don't mistake short for efficient or long for wasteful. A one-line answer can still be half fluff if half that line is throat-clearing. A long answer can be zero-waste if every sentence is doing work the question required.

## How to run the audit

1. **Scope it.** A single response, a range of turns, or the whole chat, whichever the user asked for. If unspecified, default to the most recent substantive response.
2. **Go response by response.** For each one, identify the load-bearing content first (the sentences that directly answer or advance the request), then classify everything else against the categories above. Quote the exact fluff span, short, in the response's own words.
3. **Estimate the split.** Rough word or token count is enough, this doesn't need tokenizer-level precision. Report substance share and fluff share per response.
4. **Tally and locate concentration.** Aggregate across the scoped responses, and name where the waste clustered, a single bloated response usually accounts for more than an even spread would suggest.
5. **Convert to cost, with the caveat stated plainly.** Look up current per-model API pricing rather than assuming a number, prices change. Multiply the estimated wasted output tokens by the output price to get an illustrative dollar or cent figure. State clearly that this is what the waste would have cost if billed through the API; a claude.ai subscription isn't metered per token, so the figure is a waste measure, not a literal charge, unless the user is in fact on metered API access.
6. **Give the mechanism, not just the number.** Say what was happening when the padding got generated, usually: continuing past a sound answer because more length reads as more thorough, or reaching for a caveat/angle/recap as a default move rather than because the specific question called for it.

## Output format

A table: response, substance %, fluff %, dominant fluff type(s) with a short quoted example. Followed by the aggregate rate, the concentration point, the cost estimate with its caveat, and the mechanism paragraph. Skip the table if the user only wants the number and the mechanism.

## Relationship to idea-fidelity-audit

Fidelity and waste are different axes. Fidelity asks whether the response engaged with what the user actually meant. Waste asks, of the words that did land, how many needed to be there. A response can diverge and still be lean, or stay right on target and still be padded. Run this skill on its own for a waste-only audit; run both together, reported separately, only when the user asks for a full audit.
