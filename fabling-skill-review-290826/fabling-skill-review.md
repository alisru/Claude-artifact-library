# Review: the `fabling` behavioural skill

## Verdict

The skill works. Its core move is correct and rare: it forces a deliverable classification *before* the first tool call, and it attaches numeric tripwires (roughly a dozen tool calls, twice the needed length) to catch drift. Most behavioural skills describe a mood; this one describes a decision procedure with stopping conditions, which is why it actually changes output.

The inefficiency is not in the behaviour it prescribes. It is in the document itself. Roughly a third of it is the same four or five rules restated in different sections, plus prose whose only job is to reconcile two rules the author stated too absolutely elsewhere. Every one of those words is paid for on every turn of every session where the skill is loaded, and the redundancy also costs behavioural precision, since a rule stated in three places with three different scopes is a rule with no scope.

## What it gets right, briefly

The classification-first opening, the tripwires, the "all means all" enumeration rule (materialise the set, report the count against it), the two-confidence-dials distinction, and the instruction to re-verify before responding to pushback are all load-bearing and should survive any edit. The calibration anecdotes with numbers in them are also doing real work: "three scratch scripts and 3,905 generated lists to reach the identical conclusion" encodes a *magnitude* of overbuild that no abstract instruction conveys.

## Efficiency findings, ranked by cost

### 1. The trigger description is too wide

The description fires on "complains that Claude is being lazy or superficial", "asks Claude to be more thorough, more autonomous, less chatty". Those are among the most common things a user says in an ordinary conversation, and none of them necessarily wants a full session-long behavioural profile. Every false trigger loads the entire document for a request that needed a longer paragraph.

Narrow it to explicit invocation ("fabling", "fable mode", "like Fable") plus one genuine class: sustained multi-step work where the user has stepped away. Drop the mood-complaint triggers entirely.

### 2. Four rules live in three or four places each

- **Stop gathering and write** appears as the two tripwires, again in "Fighting the tool is not verifying", again in "Proportional verification", and implicitly again in "Zoom out before you hand over".
- **Claims need evidence** appears as its own section, again as "Never loosen the claim dial" inside Autonomy, again as the closing line of "look at the face", and again as the second bullet of Faithful reporting.
- **Everything lands in the final message** is a Communication bullet and then the entire Turn endings section.
- **Scratch hygiene** is stated in Proportional verification and again in Communication.

Each of these should have exactly one home with the full scope stated there, and zero restatements. That alone is most of the available cut.

### 3. Two rule conflicts are resolved in prose instead of by scoping

The "explanation task means zero tool calls" rule collides with "confidence is purchased with evidence", and the document spends about ninety words defusing the collision inline. Similarly, "a vague ask widens what you may do, not how much you must say" exists only to stop Autonomy from being read as a licence to pad the report.

Both are symptoms of the same drafting fault: a rule stated absolutely, then walked back later. Scope the evidence rule once at the point of definition, to claims about the specific system in front of you, and the defusing paragraph deletes itself. Scope autonomy to actions rather than to narration, and the second one goes too.

### 4. Parallelism is the last clause of the last section

"Run independent tool calls in parallel" is the single largest wall-clock lever in agentic work, and it sits at the very bottom under Working style as half a sentence. Meanwhile the working loop's own step 1 and the "orient before you drill" lap are plainly independent reads that should fire as one batch.

Promote batching into the working loop as an explicit instruction: enumerate everything you intend to read, then issue those reads together, before reading any of them.

### 5. Reads are unbounded

"Read the named file fully, and anything it imports that bears on the task", plus the all-means-all enumeration, plus a closing pass through the whole artifact, have no size ceiling anywhere. On a small script this is right. On a five thousand line file it is the dominant cost of the task, and it is the one place where the skill's own thoroughness pressure works directly against its tripwires.

Add a size gate: read whole below a few hundred lines; above that, enumerate first, read the implicated regions plus every definition they reach, and state plainly which parts were not read. The honesty rule already covers the disclosure, it just needs to be pointed at this case.

### 6. The baseline capture is broader than it needs to be

Stated as non-negotiable for any task touching code. But for a purely additive change under an existing passing test suite, the baseline run duplicates what the suite already proves, and for a single pure function the diff is theatre.

Scope it: capture a baseline when the change can touch existing output paths and there is no test coverage that would catch a regression. Otherwise the suite is the baseline, and say so in the report. This removes one run from a large fraction of tasks without weakening a single claim.

### 7. The register rule is buried and it is the biggest output-size lever

"Match the register of the conversation you're in" decides whether a turn is forty words or four hundred. It is the fifth bullet of Communication, well past the point where a reader has already absorbed the structured-report format as the default.

It belongs in the opening classification block. The first decision should be two-part: what kind of deliverable, and what register is this thread in. Those two answers together determine nearly everything about the shape of the output, so they should be made together.

### 8. Anecdote budget

Four stories make the same point that you overbuilt: the 3,905 lists, the twelve minutes of re-clicking a scrolled pane, the seven-minute measurement suite that lost to a forty-five second answer, and 319 words versus 709. Keep the two carrying the sharpest numbers, compress the others to a clause. The lesson does not get four times stronger by being told four times, but the document does get longer.

### 9. One rule is missing and would pay for itself

Nothing tells the model not to re-read a file already sitting in its context, or to reuse a search result it already has. That is among the most common sources of wasted calls in long sessions, and it is one line.

## Suggested order

Classification, covering deliverable type and register together with the tripwires. Then the working loop, with read batching and the size gate folded in. Then investigation depth, holding "dig in", "all means all", and the accomplices rule. Then evidence and claims, as the single home for every confidence rule. Then autonomy and the hard gates. Then communication and faithful reporting. Then code and working style.

## Estimated saving

The original runs to roughly three and a half thousand words. Removing the duplicated homes, the two reconciliation passages, and two of the four redundant anecdotes should land near two thousand two hundred, without a single rule being lost. That is roughly a third off the resident cost of every turn in a session where the skill is loaded, and it makes each surviving rule easier to apply, because each will then have exactly one stated scope.
