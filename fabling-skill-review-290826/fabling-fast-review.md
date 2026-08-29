# Review: `fabling-fast`

## Verdict

This is the better document, and it should be the base rather than the variant. It lands at roughly a fifth of the parent's length while carrying nearly every behaviour-changing rule, and it independently fixes most of what was wrong with the original: the tripwires are tighter and numeric, the baseline capture is scoped instead of universal, parallel reads are named as the quiet time sink rather than buried as a closing aside, the register rule survives, and the evidence rule is stated once with its scope attached instead of three times with none.

But it cut three rules that were doing work, and one of its caps actively fights a rule it kept. Those four things are the whole review.

## What the compression got right

The reconciliation passages are gone because the conflicts they patched no longer exist, which is the correct way to remove them. The four redundant anecdotes are gone. The sweep rule survived intact with its "names hide in strings and aliases" trap, and it is explicitly marked as the one place this variant never cuts, which is exactly the right carve-out since incomplete sweeps are a reporting failure rather than a thoroughness preference. The autonomy section is now two sentences and loses nothing.

The wide trigger description ("complains the assistant is slow") was the parent's most expensive fault and is nearly harmless here. A false trigger now costs a few hundred words instead of several thousand, so the loose description is a reasonable trade in this document even though it was not in the other.

## The four problems

### 1. The probe cap fights the accomplice rule

"Bug → cap: the repro plus two probes" is a hard cap on hypotheses tested, which is a different instrument from a tripwire. A tripwire says stop gathering and write what you have. A cap on probes says stop investigating, and those produce different failures: the first ships an honest partial answer, the second ships a confident single-cause diagnosis.

This collides directly with the accomplice rule two sections later, which requires by construction that after finding a defective part you spend another probe asking what it conspires with. The parent skill's hardest test case was a two-cause bug where the obvious finding could not explain the reported symptom at all. Under a two-probe cap that case is a coin flip.

Convert the cap to a tripwire: at three probes, write what you have and name what remains untested. The budget stays roughly the same, the failure mode changes from wrong to incomplete, and incomplete is recoverable.

### 2. Fix-or-diagnose is missing entirely

The parent had an explicit rule that when the user asks a question, the deliverable is the diagnosis rather than a patch, and that a fix is never applied silently. Nothing in the fast version carries this. The gates clause covers forks needing information only the user has, but "they asked why, not for an edit" is not a fork, it is a reading of the request.

This is the single most consequential omission, because the failure is invisible in the report. The reply looks decisive and correct while having modified a file the user only wanted explained. Restore it as one sentence: a question earns a diagnosis, and any fix applied is disclosed in the first sentence.

### 3. The named file is no longer stated to be a starting point

The parent was explicit that the file the user names is where you begin, not the boundary, and that a bug reported against one module is routinely caused by something it imports. The fast version has the orientation lap and the accomplice rule, both of which point the same direction, but neither says to read past the named file.

Paired with an eight-call tripwire, this leans toward exactly the shallow single-file answer that the parent skill exists to prevent. The tripwire and the missing boundary rule reinforce each other in the wrong direction, which is the one place where compression changed behaviour rather than word count. One clause fixes it.

### 4. Broken verification channels are no longer handled

The parent's rule that fighting the tool is not verifying, and that a check failing twice for tool reasons means switching channels rather than retrying, was dropped. That rule matters more here, not less. With a hard eight-call ceiling and a single verification pass, a check that fails for environmental reasons can consume the entire budget and leave the task both unverified and out of calls. Restore it as a clause on the tripwire line.

## The calibration question

Cutting all four anecdotes is defensible and mostly free, because the numeric tripwires now carry the magnitude that the stories used to. That is a real substitution rather than a loss. The residual risk is that the tripwires are the only calibration left, so any task class where eight calls is the wrong number has nothing else holding the line.

Keeping one anecdote with its numbers, the three scratch scripts and 3,905 generated lists reaching the same conclusion as a five-line probe, would cost about thirty words and restore a sense of proportion that generalises past the specific counts. That is the only place where adding text back is worth it.

## Structural recommendation

Do not maintain two skills. Overlapping behavioural documents drift, and the drift is silent because nothing tests them against each other. The fast version plus the four restorations above lands somewhere near nine hundred words and dominates the parent on every axis, so make it the base and keep at most a short escalation clause for the rare task that genuinely warrants deeper investigation, triggered by the work rather than by a separate skill load.
