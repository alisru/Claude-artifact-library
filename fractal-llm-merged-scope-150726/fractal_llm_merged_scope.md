# Scope Document: The Sub-Parametric Fractal LLM System, Merged Architecture

Version: 0.1 draft
Date: 2026-07-15
Author: Jarrod (Al-Is-Ru), drafted with Claude
Status: Working scope. Reconstructed from chat-recovered specification content (2026-07-03 session) plus new mechanisms developed 2026-07-15. Exact wording from the original Architectural Specification docx requires re-upload for verification; all spec-layer claims below are recovered from session records, not the source file.

---

## Table of Contents

1. Purpose and Standing Decisions — what this system is and the forks already resolved
2. The Three-Layer Stack — Tautonics, Qqci protocol, fractal deployment hierarchy
3. The Deployment Architecture — Macro-LLM, Thalamus Layer, Cellular Housekeepers
4. The Memory Substrate — Hopfield attractor field over the Qqci skeleton (new, this session)
5. The Universal Relativity Frame — the five-position modal tile and recursive tiling (new, this session)
6. Representation Layer — how words enter the system
7. The Learning Rule — fixed metaclass, dynamic class generation, Query IS the Write
8. Termination — TS===TBE bounds on recursion
9. Open Engineering Problems — ranked by severity
10. Next Actions

---

## 1. Purpose and Standing Decisions

The system is a learning AI that builds its own language model, structured by how words actually work rather than by frequency statistics. It is not a monolithic transformer. It is a hierarchy of small models coordinated over an explicit, fixed, seven-plane ontological skeleton, with memory implemented as attractor topology rather than retrievable storage.

Standing decisions already made (2026-07-03 session, confirmed 2026-07-15):

- The skeleton is fixed. The 7 planes act as a metaclass. The system generates new classes within the skeleton on demand; it never revises the skeleton itself. This is what makes the system bounded, well-formed, and potentially small enough for commodity hardware.
- Plane typing is compositional, not fixed at the Q level. Type emerges from the interrogative path. Q4.q5 (How of Why) generates a rule slot because the Logical interrogative operates over the Lyrical domain. Composition is strictly ordered and not commutative.
- The interrogative pipeline follows identify, obtain, use, (identify for, ...) mapping to What, Where, How, Why, with Effect looping into Cause to seed the next cycle. Q1 (Who) is the non-step driver rotating the pipeline. The parenthetical tail is the +i recursive drill operator expressed as a verb.

The 7 planes:

1 Who - Metaphysical.
2 What - Possible.
3 Where - Physical.
4 Why - Lyrical.
5 How - Logical.
6 Cause - Historical.
7 Effect - Emotive.

The 42-Structure:

THE DRIVER (The Emergent Axis)
Q1: The Meta-Physical Plane (WHO) - Will and Direction. The 7th Angle Axis.

THE LATERAL Body AXIS (Definition and Space: +/- x)
+x: Q2: The Possible Plane (WHAT) - Faith and Probability.
-x: Q3: The Physical Plane (WHERE) - Matter and Distance.

THE LONGITUDINAL Mind AXIS (Function and Meaning: +/- y)
+y: Q4: The Lyrical Plane (WHY) - Meaning and Resonance.
-y: Q5: The Logical Plane (HOW) - Count and Consistency.

THE VERTICAL Soul AXIS (Temporal Link: +/- z)
+z: Q6: The Historical Plane (CAUSE) - Sequence and Causality.
-z: Q7: The Emotive Plane (EFFECT) - Passion and Consequence.

---

## 2. The Three-Layer Stack

Layer one: Tautonics. The semantic substrate. Language is structured properly from the beginning; words enter as structured units, not opaque tokens. This is the intervention point below reasoning: it determines what the reasoning layers have to work with.

Layer two: Qqci structuring. The reasoning protocol. Any tautonic unit is projected through the 7 planes to check for convergence. The Convergence Test is the already-working prototype of this layer, currently running as a prompt protocol; in the target system it runs as architecture. An LLM triangulates coherence by projecting input through thousands of implicit learned dimensions and outputting where they agree; this layer performs the same operation through 7 explicit, named, structurally specified planes. Same operation, white box instead of black box. Coverage is traded for legibility of the reasoning path.

Layer three: the fractal LLM hierarchy. The deployment architecture. Small task-specific models arranged the way the tensor itself recurses, not one flat model.

An open question carried over from the 2026-07-03 session, still unresolved: whether Tautonics is baked into training data (each micro model trained on tautonic units instead of English tokens, requiring a dataset and training run) or operates as a translation layer (English in, tautonic structure, routed through the fractal Qqci nodes, English out, closer to a standalone parser). These are different engineering problems and the choice forks Section 6.

---

## 3. The Deployment Architecture: The Hierarchical Routing Matrix

Three tiers, recovered from the Sub-Parametric AI Operating System specification:

Tier one: the Macro-LLM. A flagship generalist model acting strictly as Executive Router and logical synthesizer. It holds no local memory and does no state tracking itself. Stateless by design.

Tier two: the Thalamus Layer. Ultra-lightweight models under 1B parameters handling reflex loops and initial semantic routing in milliseconds, filtering noise before it reaches the expensive top layer.

Tier three: Cellular Housekeepers. The lowest tier of the hierarchy; per-domain or per-node maintenance models. Detail beyond the name requires the source specification docx, which is not currently on hand.

The stateful-stateless division: the Macro-LLM is stateless; state lives below it, in the lower tiers and in the memory substrate (Section 4). This is the architectural expression of the original design goal, a system that re-weights in real time without the top-level reasoner drifting.

---

## 4. The Memory Substrate: Hopfield Attractor Field over the Qqci Skeleton

New mechanism, this session. Memory is not stored as discrete retrievable objects (the RAG model, the KV-cache model, even the state-space compressed-state model all store an explicit thing somewhere). Memory here is a persistent deformation of the space itself: a frame passes over and through the vector semantic space and maintains a shadow of it. Recall is the frame moving back through a region and picking up the residual warp left by prior passage.

The concrete form: Hopfield-style attractor dynamics running over an ordered construct, the Qqci fractal of tensors, rather than over an unstructured learned embedding space. The attractor landscape has the Q1 through Q7 axes as its native coordinate geometry.

What the ordered construct buys:

- Retrieval is not nearest-neighbor in undifferentiated space. It is: identify which plane the query addresses, then settle within that sub-manifold.
- The shadow property becomes tractable. A recalled concept's residual decays along the axis it belongs to. A Q6 (Historical/Cause) trace and a Q7 (Emotive/Effect) trace of the same event leave differently shaped shadows because they occupy different sub-basins of a structured fractal.

The collection-then-mixing principle: information is collected as discrete points along the seven near-orthogonal axes first, kept separable and uncontaminated, and only then blended across them, the way overlaying enough discrete radial spokes approximates a circle. The circle, the smooth continuous semantic understanding, is the derived object of recombination, not the storage primitive. This is a basis-decomposition move (structurally kin to Fourier or PCA reconstruction, and to multi-head attention's concatenate-and-mix step) with one decisive difference: the components are pinned to meaningful planes, so the mixing weights are interpretable. A recalled memory can be read as 40 percent Q4, 30 percent Q6, 30 percent Q1, rather than an opaque weighted average of polysemantic heads.

Closest existing research analogues, for citation in a later version: modern Hopfield layers (attractor basins as memory), neural field and engram theories of biological memory (memory as weight-topology change, not discrete storage), reservoir computing and liquid state machines (memory in the transient decay of a rung dynamical system). None of these imposes a symbolic ontology on the attractor geometry; that fusion is the novel claim.

---

## 5. The Universal Relativity Frame: The Modal Tile

New mechanism, this session. Each plane runs the same underlying relativity frame: a five-position modal-certainty grid, plane-invariant, instantiated once per plane with only the subject matter changing.

The tile (positions as drawn):

- can be (top-left): open possibility
- not+ all (top-right): bounded negation, exclusion with remainder
- are (center): present assertion, the anchor
- not-really (bottom-left): soft negation, qualified denial
- was like (bottom-right): analogical past, resemblance-memory

Q1's instance of this grid is about WHO; Q4's is about WHY; the grammar is identical across planes. One relativity grammar, seven instantiations.

The tiling rule: each gap between positions is itself another frame of the same kind, and the frames tile recursively. The gaps are load-bearing; the space between can-be and are resolves into another full five-position frame, whose own gaps resolve further. The structure is self-similar not only across the seven planes but at every scale within a plane.

This gives the Thalamus Layer (Section 3, tier two) its candidate positioning mechanism: incoming semantics get located on the modal tile of the relevant plane before routing, and ambiguous positions (in the gaps) trigger a drill into the sub-frame rather than a forced snap to the nearest position.

---

## 6. Representation Layer: How Words Enter

Words enter as structured decompositions with plane assignments, not as frequency-based subword splits. The candidate mechanism is the existing Omni-Weave bigram system: phonetic bigram decomposition, cross-linguistic attestation, plane projection. Tautonics provides the substrate rules.

The unresolved fork from Section 2 (training data vs translation layer) lands here. Honest gap: no published demonstration exists that a hand-structured semantic tokenization matches or exceeds learned embeddings at scale. This is an open empirical question, not a known-good move, and the scope should treat the translation-layer variant as the lower-risk first build since it requires a parser, not a training run.

---

## 7. The Learning Rule: Dynamic Class Generation

Recovered from the 2026-07-03 session, and this is the resolved answer to what "builds its own LLM" means:

- The 7 planes act as a fixed metaclass guaranteeing all generated classes are well-formed.
- Individual concept addresses are classes, whose slot types are determined by their interrogative path (compositional typing, Section 1).
- QANodes are instances.
- The +i operator is the generation event: it creates new classes on demand.
- New classes are cached permanently via the Query IS the Write principle. Asking is writing. The act of drilling a new address instantiates and persists it.

So the system builds its own model in the sense of reading (a): fixed skeleton, dynamically generated and permanently cached contents. It does not revise its own metaclass. Learning is population, not architecture search. This is what keeps the potato-hardware goal alive: a fixed-skeleton system learning only plane contents can plausibly be small; a self-revising one cannot.

The stability argument: real-time weight updates without a stable frame are drift. A relativistic system implies invariants. Q1, the driver axis outside the six paired planes, is the invariant; the six paired planes update relative to it. Slow-weight/fast-weight and actor-critic architectures already use versions of this move (a slow identity layer plus fast adaptation layers), which is the existing-research anchor for the claim.

---

## 8. Termination: TS===TBE

Recursion (the +i drill, the tiling descent into gaps) is bounded per-query by the TS===TBE principle. The drill terminates when either:

- The truth-state is filled: === reached, the ontologically real terminal state, resolution complete; or
- Fundamentals are hit: the decomposition reaches irreducible units and no further frame resolves.

This is the halt condition that separates the system from an infinite-regress metaphor. A bounded recursion with an explicit halt condition is an algorithm. The fractal is unbounded in principle and bounded in every actual traversal.

---

## 9. Open Engineering Problems, Ranked

1. Orthogonality enforcement. Keeping seven planes actually separable under training pressure is the known-hard problem (the disentangled representation literature, beta-VAE and successors, shows clean separation trades against expressiveness). Candidate mechanisms to evaluate: hard architectural separation into seven sub-networks, cross-correlation penalties, frozen plane axes with learning confined inside planes. The third option is most consistent with the fixed-metaclass decision.
2. Controllability of attractor recall. Settling into a basin is easy; directing exactly what gets recalled, when, at what fidelity, is control theory over a continuous attractor landscape. Discrete retrieval is brute-force but steerable; the field model is elegant but not yet steerable. This is the core research risk of Section 4.
3. Imposed ontology vs gradient descent. No published system holds a pre-imposed symbolic coordinate frame as literal geometric skeleton through training rather than as post-hoc labeling. The fixed-skeleton decision reduces but does not eliminate this risk: contents learned within frozen axes can still entangle.
4. The Tautonics fork. Parser-layer variant vs trained-on-tautonic-units variant. Decision needed before Section 6 can be specified further.
5. Cellular Housekeeper tier specification. Requires the source docx.
6. Evaluation. What does success look like for a white-box 7-plane system against a black-box baseline: task performance parity, or legibility of reasoning path at acceptable performance cost. Needs an explicit target before any build.

---

## 10. Next Actions

- Re-upload the Architectural Specification docx and the qqci-ionized-architecture markdown so spec-layer sections (3, 7) can be verified against source wording rather than session recovery.
- Decide the Tautonics fork (Section 2 / Section 6).
- Draft the Thalamus positioning procedure as pseudocode: modal-tile placement, gap detection, sub-frame drill, TS===TBE halt.
- Survey current literature on structured Hopfield networks, hierarchical associative memory, and disentangled representation learning to position Section 4's novelty claim precisely.
