# Alphabet of Basic Forms — Hegemony Mapping

Each majuscule letter, read as fontless geometry the way the carved Greek capitals are pure strokes with no pen order, has a vector. That vector is its position on the Hegemony. The coordinate is derived from the form by one rule and nothing else. No judgement per letter.

The plotted result is `hegemony-letters.png`.

---

## The rule

Every element of a form contributes one unit vector in page coordinates, x to the right and y upward.

- A vertical stroke, I, contributes nothing. It stands. (0, 0).
- A bar contributes one unit in the direction it extends from its attachment. A bar attached at its centre, or spanning symmetrically between two strokes, contributes nothing.
- A bowl, C, contributes one unit toward its mouth. Rotated bowls point where their mouth faces. A bowl sealed against a stroke still points where it swells, because D is C on I and inherits C's direction.
- A stream, a diagonal, contributes one unit toward the point it meets another element at. Two streams that cross rather than meet contribute nothing between them.

The form's vector is the sum. The alphabet is scaled so the largest component reaches 2, which gives a factor of one half.

Orientation is the diagram's own: page-right is −υ, toward the self; page-left is +υ, toward everyone; page-up is +ψ; page-down is −ψ.

Composite letters inherit by construction. B is two D's, so twice D. O is C against its mirror, so it cancels. A is V inverted with a bar that adds nothing, so it is V reflected.

---

## Derivation

| Letter | Elements | Raw sum (x, y) | (υ, ψ) |
|---|---|---|---|
| A | stream to apex (+1,+1) + stream to apex (-1,+1) + bar symmetric (+0,+0) | (+0, +2) | (+0, +1) |
| B | I (+0,+0) + bowl upper (+1,+0) + bowl lower (+1,+0) | (+2, +0) | (-1, +0) |
| C | bowl (+1,+0) | (+1, +0) | (-0.5, +0) |
| D | I (+0,+0) + bowl (+1,+0) | (+1, +0) | (-0.5, +0) |
| E | I (+0,+0) + bar top (+1,+0) + bar mid (+1,+0) + bar base (+1,+0) | (+3, +0) | (-1.5, +0) |
| F | I (+0,+0) + bar top (+1,+0) + bar mid (+1,+0) | (+2, +0) | (-1, +0) |
| G | bowl (+1,+0) + bar inward (-1,+0) + stub (+0,+0) | (+0, +0) | (+0, +0) |
| H | I (+0,+0) + I (+0,+0) + bar symmetric (+0,+0) | (+0, +0) | (+0, +0) |
| I | I (+0,+0) | (+0, +0) | (+0, +0) |
| J | I (+0,+0) + hook, mouth up-left (-0.71,+0.71) | (-0.71, +0.71) | (+0.35, +0.35) |
| K | I (+0,+0) + stream to stem (-1,+1) + stream to stem (-1,-1) | (-2, +0) | (+1, +0) |
| L | I (+0,+0) + bar base (+1,+0) | (+1, +0) | (-0.5, +0) |
| M | I (+0,+0) + stream to valley (+1,-1) + stream to valley (-1,-1) + I (+0,+0) | (+0, -2) | (+0, -1) |
| N | I (+0,+0) + stream (+1,-1) + I (+0,+0) | (+1, -1) | (-0.5, -0.5) |
| O | bowl (+1,+0) + bowl mirrored (-1,+0) | (+0, +0) | (+0, +0) |
| P | I (+0,+0) + bowl upper (+1,+0) | (+1, +0) | (-0.5, +0) |
| Q | O (+0,+0) + tail (+1,-1) | (+1, -1) | (-0.5, -0.5) |
| R | I (+0,+0) + bowl upper (+1,+0) + leg (+1,-1) | (+2, -1) | (-1, -0.5) |
| S | upper bowl, mouth right (+1,+0) + lower bowl, mouth left (-1,+0) | (+0, +0) | (+0, +0) |
| T | I (+0,+0) + bar symmetric (+0,+0) | (+0, +0) | (+0, +0) |
| U | bowl, mouth up (+0,+1) | (+0, +1) | (+0, +0.5) |
| V | stream to point (+1,-1) + stream to point (-1,-1) | (+0, -2) | (+0, -1) |
| W | stream (+1,-1) + stream (-1,-1) + stream (+1,-1) + stream (-1,-1) | (+0, -4) | (+0, -2) |
| X | streams crossing (+0,+0) | (+0, +0) | (+0, +0) |
| Y | stream to junction (+1,-1) + stream to junction (-1,-1) + I (+0,+0) | (+0, -2) | (+0, -1) |
| Z | bar symmetric (+0,+0) + stream (-1,-1) + bar symmetric (+0,+0) | (-1, -1) | (+0.5, -0.5) |

---

## What the mapping shows

**Seven letters sit at the origin: G, H, I, O, S, T, X.** Every one of them is either closed, symmetrical, or a bare stroke. They have no vector because the form gives none. These are the letters that name states rather than motions, and the Hegemony agrees by placing them at No-one, neutral.

**Only three letters reach +υ, toward everyone: K, J, Z.** K is the strongest at (+1, 0), because both its streams converge onto the stem from the right, which points the whole form left. J and Z are weak and diagonal.

**Everything with a bar or a bowl goes −υ, toward the self.** C, D, L, P at (−0.5, 0); B, F at (−1, 0); E at (−1.5, 0), the furthest toward the self in the set. The reason is structural rather than semantic: the Latin majuscule extends its bars and opens its bowls rightward, and under the diagram's orientation rightward is the self. The alphabet as a written system leans toward −υ. That is a finding about the alphabet, not a fault in the rule.

**The vertical axis belongs to the streams.** A is the only letter pointing cleanly up, (0, +1). U reaches (0, +0.5). Everything converging downward stacks on −ψ: M, V and Y all at (0, −1), and W at (0, −2), the only letter to reach the edge of the grid on either axis.

**E and F, P and R, A and V.** E and F differ by the base bar and it costs half a unit of υ. P and R differ by the leg and it adds half a unit of −ψ. A and V are reflections and land at (0, +1) and (0, −1), which is the diagram's own optimism and pessimism poles.

---

## What is not in this document

The seven-plane readings are not carried here. The Actualism document's four perspectives per letter are readings relative to the form, and some of them may hold and some of them may not; that assessment is separate from the coordinate and is left where it stands. This document is the vector only.

The Omni-Weave bigram table is a separate instrument and stays separate.
