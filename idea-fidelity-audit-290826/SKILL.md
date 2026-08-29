---
name: idea-fidelity-audit
description: Audit how closely Claude's outputs in this conversation actually engaged with what the user meant, versus substituting mismatched evidence, wrong engagement mode, or arguing against something the user didn't say. Use when the user asks Claude to audit the conversation, check how well it understood them, count divergence, or review prompt-by-prompt whether Claude got the point. Also use proactively, mid-conversation, when Claude notices it is reaching for a citation or a counter-example in response to a novel design the user is building rather than reasoning about the structure as stated — that reach is the leading indicator of the failure this skill audits for.
---

# Idea Fidelity Audit

This exists because of a specific, repeated failure: the user proposes something novel and unmeasured, and Claude responds by retrieving the nearest thing that's actually been studied and reporting on that instead — often keyword-matched rather than structure-matched, and often used to tell the user their idea has a problem the retrieved thing has. It reads as rigour. It functions as avoidance, because reasoning forward about an unmeasured structure is harder than citing something that measures a different one.

## The four divergence types

Classify every Claude output against what the user actually said, not against what would have been a good answer in the abstract.

- **Evidence mismatch.** Claude cites or researches something that resembles the user's idea by keyword but not by structure, then reports findings from the mismatch as if they apply. (Matching "chain" to a benchmark about linear-vs-jumping traversal held live in one prompt, when the user described dispatch that discards each layer once resolved.)
- **Engagement mode mismatch.** The user wanted exploration and got a list of failure modes. Or the user wanted the concept taken further and got an implementation spec with metrics and a build order. Comprehension can be exactly correct while the mode is wrong — this is not the same failure as evidence mismatch and should be logged separately.
- **Literalized analogy.** The user says "it's like X" and Claude argues against X as though the user said "it is X," missing that an analogy is illustrative, not a claim to be graded on its edges.
- **Misattributed limitation.** Claude finds a real problem with a *different, unintended* version of the idea, then states that problem as if it applies to the user's actual idea — without checking whether the mechanism that causes the problem is even present in what the user described.

Scope mismatch (answer far longer or shorter than the correction warranted) is worth flagging but is a severity note on the above types, not a fifth category — it's what makes a mismatch cost more.

## How to run the audit

1. **Separate administrative turns from idea-development turns.** Turns asking to run/save/format something, or asking about the audit itself, don't count toward the rate — they're not where comprehension is being tested. Only turns where the user is stating, correcting, or extending a substantive idea go into the denominator.
2. **Go turn by turn.** For each idea-development turn, restate in one line what the user actually said, then one line on what Claude's response actually did with it.
3. **Classify.** Match / Half-diverged (comprehension right, mode wrong) / Diverged (one or more of the four types above), and name which type.
4. **Tally the idea-development turns only**, and report the divergence rate as a fraction of that count — full turns and half turns weighted separately, not folded into one number silently.
5. **Locate the concentration.** Divergence is rarely spread evenly. Name which sub-thread or idea it clustered around — that's more diagnostic than the aggregate rate, because it usually marks the exact point where the user moved from citable territory into a design nothing has measured.
6. **Give the causal account, not just the count.** A scorecard without a mechanism is itself an instance of the failure — treating an audit as an inventory rather than an analysis. State what Claude was doing at the moment it diverged (usually: reaching for a citation instead of reasoning about the structure as given) and why that's a distinct move from just being wrong.

## Output format

A table — prompt gist, what happened, verdict, one-line reason — followed by the tally restricted to idea-development turns, the concentration point, and the causal paragraph. Skip the table if the user only wants the number and the mechanism; don't pad it back in.

## Using this before the fact, not just after

The leading indicator is noticing, mid-response, that the reasoning is reaching for a search or a remembered result *because* the user's structure doesn't map to anything measured yet — not because the search is actually needed to answer. When that's the case, the right move is to reason forward from the user's stated mechanism first, and bring in outside evidence only once it demonstrably matches the structure as given, not the nearest labeled version of it.
