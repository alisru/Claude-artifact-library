# Option-Space Expansion as the Definition of a Perfect World
## A Dynamic Criterion, Its Formalisation, and Its Place in the Psochic Hegemony

Jarrod Hamilton (alisru), with drafting assistance from Claude
3 September 2026

---

## Abstract

This paper states and formalises a single definition: a perfect world is one that continuously increases the amount of viable, available choice open to its participants over time. The definition is dynamic rather than static. It does not describe a terminal state to be reached but a direction to be sustained. We give the definition a measure-theoretic form, derive a four-class taxonomy of actions from the sign and rate of change of the option space, and show that the definition is stable under the framework's existing floor condition (the Cost of Being, 1∞). We then define the unit of good as the expansion of a single participant's available option space, total good as the signed sum of such expansions across participants, and the perfect world as the limit case in which every term is positive and sustained. We then locate the definition against its independent prior discoveries in cybernetics, artificial intelligence and physics, and against its philosophical antecedents in the liberty tradition, pragmatism, the capability approach and the ethics of responsibility. Finally we show that the definition is not a new axis in the Psochic Hegemony but a restatement of what the Hegemony's (υ, ψ) coordinate already measures when read across time, that the υ coordinate can be derived from the signed sum rather than assigned by judgment, and that the single move which distinguishes this formulation from all of its predecessors is the horizon at which the option count is taken: the world, not the actor.

---

## 1. The Definition

**Definition 1 (Perfect World, dynamic form).** A world W is perfect to the degree that the quantity of viable, available options open to its participants increases over time.

Three terms carry the weight.

**Viable.** An option counts only if choosing it leads to a continuation. A path that terminates the chooser, or terminates the world's capacity to generate further paths, is not an option in the relevant sense. It is an exit.

**Available.** An option counts only if it is materially reachable by a participant, not merely conceivable. A cure that exists but cannot be obtained, a right that exists but cannot be exercised, a road that exists but cannot be travelled, are not available options. Availability is where infrastructure, knowledge, health, resources, political standing and social stability enter the definition without needing to be named separately: each either widens or narrows what is reachable.

**Over time.** The count is taken along a trajectory, not at an instant. This is the load-bearing phrase. Without it the definition collapses into maximising present freedom, which is trivially satisfied by consuming the future: liquidating assets, burning fuel, taking the drug. Each of these expands today's menu and shrinks tomorrow's. With it, the definition becomes a constraint on irreversibility. A closed door is subtracted from every future count.

The definition is second-order. It does not say what any participant should choose. It says that whatever is chosen should leave more choosable. It is neutral on content and strict on direction, which is why it can sit beneath competing first-order goods without adjudicating between them.

---

## 2. Formalisation

### 2.1 The option space and its measure

Let Ω(t) denote the set of distinct, viable, available futures reachable by the participant population of W at time t. Let μ be a measure on such sets, so that

O(t) = μ(Ω(t))

is the size of the option space at t. The choice of μ matters. A raw count of menu items is the wrong measure: a thousand near-identical choices is not more freedom than ten genuinely different ones. The measure must be taken over distinct reachable futures, which makes O(t) an entropy-like quantity. Two futures that converge to the same state within the horizon are one option, not two.

### 2.2 The rate and the four classes

Define the perfection rate

P(t) = dO/dt.

A perfect trajectory satisfies P(t) > 0 sustained over the horizon. From the sign of P and the relation between loss and replacement, four classes of action follow:

| Class | Condition | Description |
|---|---|---|
| Option-preserving | P = 0, no paths removed | Maintains the existing set of viable paths |
| Option-expanding | P > 0 | Creates new viable paths |
| Option-reducing | P < 0, loss rate < replacement capacity | Removes viable paths within the system's capacity to regenerate them |
| Option-destroying | P < 0, loss rate > replacement capacity | Removes paths faster than they can be replaced |

The distinction between the last two classes is the distinction between a wound and a fatality. Every living system removes some options continuously; that is what choosing is. The question is whether the removal outruns regeneration.

Writing the loss rate as L(t) and the regeneration rate as R(t), with P = R − L:

- Option-reducing: L > R but L < R_max, where R_max is the system's regenerative capacity. The trajectory can recover.
- Option-destroying: L > R_max. The trajectory cannot recover from within its own resources.

This makes the definition sensitive to the difference between a society that is materially richer and one that is more perfect. Wealth that arrives with a contraction of future possibility, through debt against unborn generations, exhaustion of a non-renewable base, or lock-in to a single fragile mode, scores as option-reducing or option-destroying regardless of the present balance sheet.

### 2.3 Sustained growth, not instantaneous growth

Maximising dO/dt at an instant is the wrong objective, since a large spike followed by collapse satisfies it. The correct objective is the maximisation of the long-horizon integral under a survival constraint:

maximise ∫₀^T O(t) dt subject to O(t) ≥ O_min for all t ∈ [0, T], with T → ∞.

The constraint is not decorative. It is where the framework's existing floor condition enters.

### 2.4 The floor

Under Infinitesimal Reality Math, zero is a frame boundary, not an absence. The smallest interior point of any frame is the Cost of Being, 1∞ = 0.0...1 (Zero Is A Floor, Not An Absence; IRM v5). Applied here:

O_min = 1∞ > 0.

A world with exactly one reachable future is not a world with no options. It is a world at the floor: fully determined, W = 1 in Boltzmann's terms, H = 0 in Shannon's. The definition therefore never divides by zero and never has to treat a totally constrained state as non-existent. It treats it as the boundary from which the only movement is outward. This also fixes the direction of the entire scale: since entropy is distance from the floor, and O is entropy-like, perfection is measured as sustained movement away from the floor of the frame, with the floor itself as the unreachable limit of total collapse.

### 2.5 The horizon of the count

The single most consequential parameter in the formalism is not μ, nor T, but the population over which Ω is taken. Two readings are possible:

**Actor horizon.** Ω_i(t) is the set of futures reachable by agent i. Each agent maximises its own O_i.

**World horizon.** Ω_W(t) is the set of futures reachable by the participant population jointly, with the measure taken so that a future in which one participant's options have grown by removing another's does not count as expansion.

These two readings share a slogan and point in opposite directions. Under the actor horizon, the fastest way to grow O_i is to absorb the option space of others. Under the world horizon, that move is option-destroying by construction. Section 3 shows that every formal predecessor of this definition takes the actor horizon, and that this is exactly why the AI literature discovered option-maximisation and power-seeking to be the same thing. Definition 1 is stated at the world horizon. That is its distinguishing move. Section 2.6 shows that the world horizon is not an assumption imposed on the count but the limit case of a per-participant definition of good.

### 2.6 The unit of good

Definition 1 describes the perfect world. It does not yet say what good is. The following definitions supply that, and show that the world horizon of §2.5 is derived rather than stipulated.

**Definition 2 (Unit of Good).** One unit of good is the expansion of a single participant's available option space over an interval: ΔO_i > 0 for participant i.

**Definition 3 (Total Good).** The total good of an action or trajectory over an interval is the signed sum of per-participant expansions:

G = Σ_i ΔO_i

summed over all participants, with each term carrying its sign. A participant whose available options contracted contributes a negative term.

**Definition 4 (Maximal Good).** The most good is G > 0 with ΔO_i > 0 for every participant i, sustained over time.

Three consequences follow.

First, Definition 1 is now a corollary. The perfect world is the trajectory on which Definition 4 holds continuously. Perfection is not a separate concept from good; it is maximal good taken over time. The world horizon of §2.5 is simply the case in which the unit of good is realised for everyone.

Second, an action that expands one participant's options by contracting another's is not "some good". It is a sum with a negative entry, and it nets to whatever remains. This is what prevents the definition from rewarding extraction: the actor-horizon reading of §2.5 is the special case in which only one term is counted and the rest are dropped from the sum.

Third, the sum must carry the survival constraint of §2.3. Terms cannot be traded off freely across participants in the way a plain sum suggests. A trajectory that gives ninety-nine participants a small expansion by removing the hundredth participant's last option drives that participant to the floor, O_j = 1∞, which is an exit from the frame rather than a reduction within it. So the sum is subject to:

O_i(t) ≥ 1∞ for all i and all t.

Within that constraint the additive definition holds. Without it, the additive definition permits sacrifice, and the floor condition is what forbids it.

---

## 3. Independent Prior Discoveries

The core idea has been arrived at independently at least four times, in four fields.

**Cybernetics.** Heinz von Foerster, in his 1973 lecture "On Constructing a Reality", stated what he called the Ethical Imperative: act always so as to increase the number of choices (von Foerster 1973/2003). This is Definition 1 with "act" in place of "world". It became a standing principle of second-order cybernetics and systems thinking.

**Artificial intelligence, agent-centric.** Klyubin, Polani and Nehaniv (2005) defined "empowerment" as a universal, agent-centric measure of control: the channel capacity from an agent's actions to its future sensor states, which is a formal measure of how many distinguishable futures the agent can bring about.

**Physics.** Wissner-Gross and Freer (2013), in "Causal Entropic Forces", showed that a system driven to maximise its future path entropy, that is, to keep the greatest number of future histories open, spontaneously exhibits tool use and cooperation in simple physical models. The accompanying APS commentary summarised the result as: systems that maximise their future possibilities behave in surprisingly intelligent ways.

**The synthesis.** Hornischer, Plakolb, Jäger and Füllsack (2020) explicitly joined the first and third strands, arguing that von Foerster's Ethical Imperative corresponds almost literally to the AI principle of Future State Maximisation (FSX), and demonstrating FSX on coordination and learning tasks. The peer commentaries in the same issue (Guckelsberger, Salge and Polani 2020; Dodig-Crnkovic 2020; Lowe 2020) connect FSX back to empowerment and debate whether the imperative is a physical principle or an ethical one.

**The warning label.** Turner, Smith, Shah, Critch and Tadepalli (2021), in "Optimal Policies Tend to Seek Power", proved that in most Markov environments, most reward functions make it optimal for an agent to keep a range of options open and to navigate toward larger sets of potential terminal states. In other words, option-maximisation at the actor horizon is what power-seeking is.

Every one of these formalisations is per-agent. Von Foerster's is closest to the world reading but is still phrased as an instruction to an actor. None of them states the criterion at the level of the world and takes the count over the population. That is the gap Definition 1 fills, and it is the part that does the moral work: the horizon is what separates a principle that produces Turner's power-seeker from one that rules it out.

---

## 4. Philosophical Antecedents

The formal lineage is recent. The philosophical lineage is not.

**Aristotle.** The distinction between dynamis (potentiality) and energeia (actuality) in Metaphysics Θ already frames the good of a thing partly in terms of what it is able to become. Definition 1 is a claim that the good of a world is in its dynamis, its reachable futures, rather than in any one energeia.

**Mill and Humboldt.** Mill's On Liberty (1859), following Humboldt, compares the development of an individual to that of a plant: individuals must be allowed to grow, developing their own faculties according to their own inner logic. The Stanford Encyclopedia of Philosophy notes that this ideal reads as a growth conception of liberty rather than a mere absence of obstacles (Carter, SEP "Positive and Negative Liberty"). Definition 1 is this growth conception generalised from the individual to the world and made measurable.

**Berlin.** Berlin's "Two Concepts of Liberty" (1958) distinguishes negative liberty, the absence of interference, from positive liberty, the presence of self-mastery. Berlin's warning is that positive liberty, detached from the individual and handed to a collective, licenses coercion in the name of a "true self". Definition 1 is agnostic between the two: it counts doors, not motives. But it inherits Berlin's warning in a precise form. An authority that closes doors now on the claim of opening more later is making an empirical claim about dO/dt that must be audited against the actual future count, not accepted on framing. The SEP's own gloss of the negative/positive distinction is telling: the first is about how many doors are open, the second about going through the right doors for the right reasons. Definition 1 is a door-count, taken over time and over everyone.

**Dewey.** Dewey's ethics replaces the search for a supreme end with a method for improving value judgments, tested by whether they enable successful responses to novel problems (Anderson, SEP "Dewey's Moral Philosophy"). In Reconstruction in Philosophy (1920) he goes further and treats growth itself as the only moral end. Definition 1 is Dewey's growth criterion given a quantity: growth is dO/dt > 0.

**Sen and the capability approach.** Sen's Development as Freedom (1999) argues that development is the expansion of the substantive freedoms people have reason to value, and that the right space in which to measure wellbeing is the capability set: what a person is actually able to do and be. Sen's "capability" is Definition 1's "available option" under another name, and his insistence on substantive rather than formal freedom is exactly the availability condition of §1.

**Jonas.** Hans Jonas's The Imperative of Responsibility (1979; English 1984) states a new categorical imperative for the technological age: act so that the effects of your action are compatible with the permanence of genuine human life. Its negative formulation is more precise still: act so that the effects of your action are not destructive of the future possibility of such life. Jonas's negative imperative is the prohibition on the option-destroying class of §2.2, stated fifty years earlier and restricted to the species-level case.

**Kauffman.** Kauffman's "adjacent possible" (Investigations, 2000) describes the set of states one step from the current state of a system, and treats the expansion into the adjacent possible as the characteristic motion of the biosphere and of the economy. Ω(t) is the reachable region of the adjacent possible; dO/dt > 0 is Kauffman's expansion made normative.

**Taleb.** Taleb's Antifragile (2012) treats optionality, the right but not the obligation to take an action, as the structural source of robustness under uncertainty. Definition 1 lifts optionality from a personal or portfolio strategy to a criterion for the world.

The pattern across these sources is consistent. Each identifies option-space expansion as good in some domain: the individual (Mill, Berlin), inquiry (Dewey), the person's life (Sen), the species (Jonas), the biosphere and economy (Kauffman), the portfolio (Taleb), the agent (Klyubin, Turner), the physical system (Wissner-Gross). None states it as a criterion for the world as a whole across time, and none formalises the distinction between reducing and destroying.

---

## 5. Integration with the Psochic Hegemony

Definition 1 does not introduce a new axis into the corpus. It is a restatement of what the Hegemony's (υ, ψ) coordinate already measures, read along a trajectory instead of at a point.

### 5.1 The ψ axis is the option-class axis

The Will axis ψ runs from +2 (actively creating systemic value for all) through +1 (proactive: creating, building, acting), 0 (no meaningful force), −1 (passive: allowing, suppressing, withholding) to −2 (actively destroying or extracting value). The four option classes of §2.2 map directly:

| Option class | ψ region |
|---|---|
| Option-expanding | +1 to +2 |
| Option-preserving | 0 to +1 (holding, maintaining) |
| Option-reducing | −1 (suppressing, withholding) |
| Option-destroying | −2 |

The corpus already names the bottom-right quadrant (−υ, −ψ) the Regressive mode and the top-left (+υ, +ψ) the Productive mode (Collate: Philosophy of Truth, Belief, Emotions §8.2). Progress as option-space expansion and regression as option-space contraction is therefore not a new pairing; it is the ψ reading of the existing quadrant names. This should be stated as a mapping, not a discovery, to avoid silent reframing of the quadrant vocabulary.

### 5.2 The υ axis is the horizon of the count

The Morality axis υ asks who benefits, from +2 (everyone) to −2 (only me). This is precisely the horizon parameter of §2.5. Taking Ω over the whole participant population is υ = +2. Taking it over one's own group is υ = −1. Taking it over oneself alone is υ = −2. So the world-horizon reading of Definition 1, which distinguishes it from all of its predecessors, is nothing more than the requirement that the option count be taken at υ = +2. Turner's power-seeker is the same formula evaluated at υ = −2.

With the signed sum of §2.6 in hand, υ stops being an assigned judgment and becomes a derived quantity. Let N be the participant population, N⁺ the set of participants with ΔO_i > 0, and N⁻ the set with ΔO_i < 0. The verbal ladder of the axis (Everyone, Other Beings, A Being, No One, My Group, Me, Only Me) is a reading of the size and membership of N⁺ and N⁻:

| υ | Structure of the sum |
|---|---|
| +2 | N⁺ = N, N⁻ empty. Every term positive. |
| +1 | N⁺ contains others beyond the actor; N⁻ small or empty. |
| 0 | N⁺ and N⁻ both empty or cancelling. No net movement. |
| −1 | N⁺ restricted to the actor's group; N⁻ non-empty outside it. |
| −2 | N⁺ = {actor}; N⁻ contains everyone the action touches. |

A first-order numerical form is υ ≈ 2 · (|N⁺| − |N⁻|) / |N|, with the caveat that the ladder is not purely a count: an action whose only positive term is the actor's own sits at −2 regardless of how many negative terms are small. Membership matters as well as cardinality, which is why the ladder names who benefits rather than how many. The Perceptual Inversion Warning of the Hegemony applies here in a specific form: an actor at the self end perceives their single positive term as the whole sum, because the negative terms fall outside the horizon they are counting over.

### 5.3 The coordinate of the definition itself

Judged as an idea on the Hegemony, Definition 1 sits at (+2.0, +2.0): beneficiary is all beings across time (N⁺ = N under §2.6), energy is actively generative. Nearest anchor: Productive Justice. Verdict: the definition is a description of what the (+2, +2) corner does when it runs continuously.

### 5.4 The Possible plane and the StateVector

In the seven-plane structure, options live on Q2, the Possible plane (WHAT), the +x pole of the lateral Body axis, paired against Q3, the Physical plane (WHERE), at −x. StateVector.cs already encodes this: its shape signature reads "Expansion" when What > Where and "Contraction" otherwise. Definition 1 is the requirement that the lateral axis of the world's state vector trend toward Expansion over time. In the MEGA consciousness cycle the Possible plane is explicitly the stage of "option generation" on the ascent and "collapse options" on the descent, which is the per-decision micro-version of the same expansion-then-selection motion.

### 5.5 The Infinite Doorman

The Infinite Doorman Theory describes order as routed, not enforced: what passes propagates, what is voided starves, and the aggregate of all doormen sorts the field without a central authority. Definition 1 gives that picture its objective function. A gate with correct criterion passes what expands the downstream option space and voids what would destroy it. The theory's closing image, "the bad running out of doors", is an option-destroying trajectory self-terminating: a path that consumes the branches it needs to continue has, by construction, nowhere further to go. The Doorman's axiom that a fully closed door is a tomb, not a gate, is the floor condition of §2.4: O = 1∞ is not a system, it is the boundary.

---

## 6. Objections and Boundaries

**The paradox of choice.** Schwartz (2004) and related work argue that more options can reduce welfare through decision cost and regret. This is an objection to a raw count, not to Definition 1, which counts distinct reachable futures under a measure μ and treats near-duplicates as one. Decision cost is a real subtraction from availability, and a world that multiplies menu items while raising the cost of choosing has not increased available options in the relevant sense.

**Measurability.** O(t) is not directly observable. Neither is entropy, utility, or GDP. The definition's value is as a direction and a partial order: it can rank two trajectories that differ in whether they close irreversible doors even when it cannot assign a number to either. Empowerment and FSX show that the quantity can be estimated in bounded models; extending that to social systems is an open task, not a refutation.

**Content neutrality.** The definition is silent on what should be chosen. This is a feature. A criterion that adjudicated between first-order goods would be one more first-order good. The definition constrains only the class of moves that foreclose future adjudication.

**The power-seeking objection.** Fully answered by §2.5, §2.6 and §5.2: the objection applies to the actor-horizon reading, which is the signed sum with all but one term dropped, and is the reason the world-horizon reading is the correct one.

**The sacrifice objection.** A plain additive definition of good would permit driving one participant to the floor for the marginal gain of many. §2.6 forbids this by carrying the survival constraint O_i ≥ 1∞ into the sum. The definition is additive above the floor and lexical at it.

---

## 7. Conclusion

Good is the expansion of a participant's available option space. Total good is the signed sum of such expansions across participants, floored at the Cost of Being. A perfect world is the trajectory on which every term of that sum is positive and stays positive: the sustained positivity of dO/dt over the world-horizon option space, with 1∞ as its floor and irreversibility as its cardinal sin. The idea has been discovered before, in cybernetics, artificial intelligence, physics, and across two centuries of philosophy of liberty, growth, capability and responsibility. What has not been stated before is the horizon at which the count must be taken. Taken at the actor, the criterion is power. Taken at the world, it is justice. The Psochic Hegemony already has an axis for that distinction. It is υ.

---

## References

Anderson, E. "Dewey's Moral Philosophy." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/dewey-moral/

Aristotle. Metaphysics, Book Θ.

Berlin, I. (1958). "Two Concepts of Liberty." Inaugural lecture, University of Oxford, 31 October 1958. Reprinted in Four Essays on Liberty (Oxford: Clarendon Press, 1969).

Carter, I. "Positive and Negative Liberty." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/liberty-positive-negative

Dewey, J. (1920). Reconstruction in Philosophy. New York: Henry Holt.

Dodig-Crnkovic, G. (2020). "The Relation between Future State Maximization and von Foerster's Ethical Imperative." Constructivist Foundations 16(1): 62–64. https://constructivist.info/16/1/062

Foerster, H. von (1973/2003). "On Constructing a Reality." In Understanding Understanding: Essays on Cybernetics and Cognition. New York: Springer, 211–227.

Guckelsberger, C., Salge, C. & Polani, D. (2020). "The Relationship of Future State Maximization and von Foerster's Ethical Imperative Through the Lens of Empowerment." Constructivist Foundations 16(1): 57–60. https://constructivist.info/16/1/057

Hamilton, J. (alisru). Zero Is A Floor, Not An Absence. Project corpus.

Hamilton, J. (alisru). Infinitesimal Reality Math (IRM), Infinity Maths v5. Project corpus.

Hamilton, J. (alisru). The Infinite Doorman Theory. Project corpus.

Hamilton, J. (alisru). Collate: Philosophy of Truth, Belief, Emotions. Project corpus.

Hamilton, J. (alisru). StateVector.cs; MEGA_CONSCIOUSNESS_PROPER. Project corpus.

Hornischer, H., Plakolb, S., Jäger, G. & Füllsack, M. (2020). "Foresight Rather than Hindsight? Future State Maximization As a Computational Interpretation of Heinz von Foerster's Ethical Imperative." Constructivist Foundations 16(1): 36–49. https://constructivist.info/16/1/036

Jonas, H. (1979/1984). The Imperative of Responsibility: In Search of an Ethics for the Technological Age. Chicago: University of Chicago Press.

Kauffman, S. (2000). Investigations. Oxford: Oxford University Press.

Klyubin, A. S., Polani, D. & Nehaniv, C. L. (2005). "Empowerment: A Universal Agent-Centric Measure of Control." Proceedings of the 2005 IEEE Congress on Evolutionary Computation, vol. 1, 128–135. https://uhra.herts.ac.uk/id/eprint/282/

Lowe, R. (2020). "Maximization of Future Internal States?" Constructivist Foundations 16(1): 60–62. https://constructivist.info/16/1/060

Mill, J. S. (1859). On Liberty. London: John W. Parker and Son.

Schwartz, B. (2004). The Paradox of Choice: Why More Is Less. New York: Ecco.

Sen, A. (1999). Development as Freedom. New York: Knopf.

Taleb, N. N. (2012). Antifragile: Things That Gain from Disorder. New York: Random House.

Turner, A. M., Smith, L., Shah, R., Critch, A. & Tadepalli, P. (2021). "Optimal Policies Tend to Seek Power." Advances in Neural Information Processing Systems 34. https://arxiv.org/abs/1912.01683

Wissner-Gross, A. D. & Freer, C. E. (2013). "Causal Entropic Forces." Physical Review Letters 110, 168702. https://doi.org/10.1103/PhysRevLett.110.168702
