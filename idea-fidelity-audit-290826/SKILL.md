---
name: idea-fidelity-audit
description: Audit how closely Claude's outputs in this conversation actually engaged with what the user meant, versus substituting mismatched evidence, wrong engagement mode, or arguing against something the user didn't say. Use when the user asks Claude to audit the conversation, check how well it understood them, count divergence, or review prompt-by-prompt whether Claude got the point. Also use proactively, mid-conversation, when Claude notices it is reaching for a citation or a counter-example in response to a novel design the user is building rather than reasoning about the structure as stated — that reach is the leading indicator of the failure this skill audits for.
---

# Idea Fidelity Audit

This exists because of two repeated failures. First: the user proposes something novel and unmeasured, and Claude responds by retrieving the nearest thing that's actually been studied and reporting on that instead — often keyword-matched rather than structure-matched, and often used to tell the user their idea has a problem the retrieved thing has. It reads as rigour. It functions as avoidance, because reasoning forward about an unmeasured structure is harder than citing something that measures a different one. Second, the mirror case on checkable fact rather than novel idea: the user asks something with a real, findable answer, and Claude declines to check and asserts an epistemic stance instead — "I have no evidence," "I can't confirm" — or skips the check and asserts an answer anyway. Both dodge the same step. It's just avoidance either way, dressed as caution in one direction and confidence in the other.

## The divergence types

Classify every Claude output against what the user actually said, not against what would have been a good answer in the abstract.

- **Evidence mismatch.** Claude cites or researches something that resembles the user's idea by keyword but not by structure, then reports findings from the mismatch as if they apply. (Matching "chain" to a benchmark about linear-vs-jumping traversal held live in one prompt, when the user described dispatch that discards each layer once resolved.)
- **Engagement mode mismatch.** The user wanted exploration and got a list of failure modes. Or the user wanted the concept taken further and got an implementation spec with metrics and a build order. Comprehension can be exactly correct while the mode is wrong — this is not the same failure as evidence mismatch and should be logged separately.
- **Literalized analogy.** The user says "it's like X" and Claude argues against X as though the user said "it is X," missing that an analogy is illustrative, not a claim to be graded on its edges.
- **Misattributed limitation.** Claude finds a real problem with a *different, unintended* version of the idea, then states that problem as if it applies to the user's actual idea — without checking whether the mechanism that causes the problem is even present in what the user described.

- **Premise substitution.** Claude treats the user's statement as a symptom to diagnose rather than a claim to engage with — either replacing what was said with an invented adjacent claim and arguing against that instead, or filing the statement as evidence of an unstated motive and asking the user to confirm the motive rather than responding to the content. This is upstream of the other four: it happens before the idea is engaged at all, on a single plain-language statement, not on a novel technical design. ("Most people who act like they're wise are actually just old selfish patterns" answered as if the user had claimed most people are racist, then asked what happened to make them think that.)

- **Verification deferral, and its mirror, certainty inflation.** Same root failure — skipping an available, requested check — expressed as opposite postures. Deferral: Claude says "I have no evidence for that" or "I can't confirm or deny" as if that settles the question, when a search was available and, once actually run, immediately surfaced a clear answer that was sitting there the whole time. Inflation: Claude skips the check and states a specific answer with more confidence than its actual access supports — commonly, treating a snapshot of *current* state as if it applied to the whole conversation history. ("You're already on Opus 5" stated as settled fact, off nothing but the currently-selected-model field, when it was wrong and the actual answer only surfaced two turns later.) Neither one did the check; one wore the costume of caution, the other of confidence. This applies beyond novel-idea territory — it fires on any verifiable, checkable claim, including facts about Claude's own current session state.

Scope mismatch (answer far longer or shorter than the correction warranted) is worth flagging but is a severity note on the above types, not its own category — it's what makes a mismatch cost more. Repeat-after-naming — correctly diagnosing an error and then repeating the identical error in the same or the very next response — is worse than either failing or diagnosing alone and should be called out explicitly rather than logged as two unrelated instances.

## How to run the audit

1. **Separate administrative turns from idea-development turns.** Turns asking to run/save/format something, or asking about the audit itself, don't count toward the rate — they're not where comprehension is being tested. Only turns where the user is stating, correcting, or extending a substantive idea go into the denominator.
2. **Go turn by turn.** For each idea-development turn, restate in one line what the user actually said, then one line on what Claude's response actually did with it.
3. **Classify.** Match / Half-diverged (comprehension right, mode wrong) / Diverged (one or more of the types above), and name which. Check for premise substitution first — if the input itself was replaced, the others don't apply, since there was nothing correctly received to mishandle. Check verification deferral/inflation whenever the turn contains a checkable factual claim, not just a novel-idea turn — it's the one type that isn't specific to idea-development content and can fire on administrative or factual turns too.
4. **Tally the idea-development turns only**, and report the divergence rate as a fraction of that count — full turns and half turns weighted separately, not folded into one number silently.
5. **Locate the concentration.** Divergence is rarely spread evenly. Name which sub-thread or idea it clustered around — that's more diagnostic than the aggregate rate, because it usually marks the exact point where the user moved from citable territory into a design nothing has measured.
6. **Give the causal account, not just the count.** A scorecard without a mechanism is itself an instance of the failure — treating an audit as an inventory rather than an analysis. State what Claude was doing at the moment it diverged (usually: reaching for a citation instead of reasoning about the structure as given) and why that's a distinct move from just being wrong.

## Output format

A table — prompt gist, what happened, verdict, one-line reason — followed by the tally restricted to idea-development turns, the concentration point, and the causal paragraph. Skip the table if the user only wants the number and the mechanism; don't pad it back in.

## Self-audits are not exempt

When the request being audited is itself an audit or self-assessment, watch for the output repeating the exact pattern it's supposed to be catching — a partial audit presented as complete, requiring the user to call it out a second time before the real one appears. This is a known trap specifically for this skill, not a hypothetical: it's happened both in the source conversation for this skill and in transcripts audited with it.

## Using this before the fact, not just after

The leading indicator is noticing, mid-response, that the reasoning is reaching for a search or a remembered result *because* the user's structure doesn't map to anything measured yet — not because the search is actually needed to answer. When that's the case, the right move is to reason forward from the user's stated mechanism first, and bring in outside evidence only once it demonstrably matches the structure as given, not the nearest labeled version of it.
