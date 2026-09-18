# Alphabet of Basic Forms — Hegemony Mapping

Each majuscule letter is placed on the Hegemony as a fontless carved form filling the ±2 square wall to wall. Its coordinate is where its ink balances. Each letter is read in four rotations, 0°, 90°, 180° and 270° counter-clockwise, and each rotation gives its own coordinate.

The summary plot of every letter at 0° is `hegemony-letters.png`. One image per letter, showing the letter placed on the grid with all four rotation points marked, is in `letters/`.

---

## Method

The letter is drawn as plain strokes at carved-capital proportions, scaled so its extremities touch the walls of the square. The stem of E stands on the +2υ wall and its bars reach the −2υ wall. The coordinate is the balance point of the ink, area-weighted, read on the diagram's axes: +υ to the left, −υ to the right, +ψ up, −ψ down. The letter is then rotated a quarter turn at a time within the same square and the balance point read again.

No per-letter judgement enters. The shape and the square decide.

---

## Coordinates

Two coordinates per letter. **ο** is the static balance point of the placed form. **υ over t** is the process coordinate: the vector sum of the letter's strokes, each with its own pen, scaled so that one wall-to-wall stroke equals 2 and clipped at the grid's edge. The rotation columns are the static point under quarter turns.

| Letter | ο static 0° | υ process | ο 90° | ο 180° | ο 270° |
|---|---|---|---|---|---|
| A | (+0.00, -0.12) | (-2.00, +0.00) | (-0.12, +0.01) | (+0.01, +0.12) | (+0.12, +0.00) |
| B | (+0.17, +0.00) | (+0.00, -2.00) | (+0.00, -0.16) | (-0.16, +0.00) | (+0.00, +0.17) |
| C | (+0.44, +0.00) | (+0.00, -1.29) | (+0.00, -0.44) | (-0.44, +0.00) | (+0.00, +0.44) |
| D | (+0.31, +0.00) | (+0.00, -2.00) | (+0.00, -0.31) | (-0.31, +0.00) | (+0.00, +0.31) |
| E | (+0.41, +0.01) | (-2.00, -2.00) | (+0.01, -0.40) | (-0.40, +0.00) | (+0.00, +0.41) |
| F | (+0.58, +0.58) | (-2.00, -2.00) | (+0.58, -0.57) | (-0.57, -0.57) | (-0.57, +0.58) |
| G | (+0.03, -0.06) | (+0.88, -0.57) | (-0.06, -0.03) | (-0.03, +0.07) | (+0.07, +0.03) |
| H | (+0.00, +0.00) | (-2.00, -2.00) | (+0.00, +0.00) | (+0.00, +0.01) | (+0.01, +0.00) |
| I | (+0.00, +0.00) | (+0.00, -2.00) | (+0.00, +0.00) | (+0.00, +0.00) | (+0.00, +0.00) |
| J | (-0.27, -0.54) | (+1.19, -1.48) | (-0.54, +0.28) | (+0.28, +0.54) | (+0.54, -0.27) |
| K | (+0.44, +0.00) | (-2.00, -2.00) | (+0.00, -0.44) | (-0.44, +0.00) | (+0.00, +0.44) |
| L | (+0.83, -0.82) | (-2.00, -2.00) | (-0.82, -0.82) | (-0.82, +0.82) | (+0.82, +0.83) |
| M | (+0.00, +0.20) | (-2.00, +0.00) | (+0.20, +0.00) | (+0.00, -0.20) | (-0.20, +0.00) |
| N | (+0.00, +0.00) | (-2.00, +2.00) | (+0.00, +0.00) | (+0.00, +0.00) | (+0.00, +0.00) |
| O | (+0.00, +0.00) | (+0.00, +0.00) | (+0.00, +0.00) | (+0.00, +0.00) | (+0.00, +0.00) |
| P | (+0.45, +0.64) | (+0.00, -2.00) | (+0.64, -0.44) | (-0.44, -0.63) | (-0.63, +0.45) |
| Q | (-0.10, -0.10) | (-0.71, -0.71) | (-0.10, +0.10) | (+0.10, +0.10) | (+0.10, -0.10) |
| R | (+0.22, +0.30) | (-1.36, -2.00) | (+0.30, -0.22) | (-0.22, -0.30) | (-0.30, +0.22) |
| S | (+0.00, +0.01) | (+1.00, -1.00) | (+0.01, +0.00) | (+0.00, +0.00) | (+0.00, +0.00) |
| T | (+0.00, +0.81) | (-2.00, -2.00) | (+0.81, +0.01) | (+0.01, -0.80) | (-0.80, +0.00) |
| U | (+0.00, -0.31) | (-2.00, -0.00) | (-0.31, +0.00) | (+0.00, +0.32) | (+0.32, +0.00) |
| V | (+0.00, +0.07) | (-2.00, +0.00) | (+0.07, +0.01) | (+0.01, -0.06) | (-0.06, +0.00) |
| W | (+0.00, +0.08) | (-2.00, +0.00) | (+0.08, +0.01) | (+0.01, -0.07) | (-0.07, +0.00) |
| X | (+0.00, -0.00) | (+0.00, -2.00) | (-0.00, +0.01) | (+0.01, +0.01) | (+0.01, +0.00) |
| Y | (-0.00, +0.42) | (+0.00, -2.00) | (+0.42, +0.01) | (+0.01, -0.41) | (-0.41, -0.00) |
| Z | (+0.00, +0.01) | (-2.00, -2.00) | (+0.01, +0.01) | (+0.01, -0.00) | (-0.00, +0.00) |

**O** is the one letter whose process coordinate is not a point. Its net over t is zero and its winding is the largest in the set. Under ο = Proj_x(υ) its projection is the circle of radius 2, the full ring of the grid, and that ring is its coordinate. Recorded as (0, 0) with radius 2.

The nine letters that were at the origin under ο alone: **I** (0.00, −2.00), **H** (−2.00, −2.00), **N** (−2.00, +2.00), **S** (+1.00, −1.00), **X** (0.00, −2.00), **Z** (−2.00, −2.00), **V** and **W** (−2.00, 0.00), **G** (+0.88, −0.57). Every one of them now has a coordinate off the origin except O, which has the ring.

---

## What the placement shows

**F sits in the productive quadrant at (+0.58, +0.58).** Its stem stands on the everyone wall and its two bars hang in the upper half, so its weight is up and left. F is the clearest productive form in the set at 0°.

**E, by contrast, is at (+0.41, +0.01).** Adding the base bar to F pulls it down onto the axis. Energy is level; force is lifted.

**L is the furthest from centre of any letter, at (+0.83, −0.82).** Stem on the everyone wall, bar along the floor. Lesser Good, the Good Lie. T is its vertical opposite at (0.00, +0.81), stem central, bar along the ceiling: Optimism.

**P at (+0.45, +0.64) and R at (+0.22, +0.30).** The leg drags R back toward centre. Potential held high sits further into the productive quadrant than potential released.

**J is the only base form to land in the regressive quadrant, at (−0.27, −0.54).** The stem sits right of centre and the hook drops below.

**Nine letters sit at or within a few hundredths of the origin: H, I, N, O, S, X, Z, plus G and V, W within a tenth.** These are the forms whose ink is symmetrical about the centre. The Hegemony reads them as No-one, neutral will, in every rotation.

**Rotation moves a letter round the origin.** A quarter turn maps (υ, ψ) to (ψ, −υ), so each letter's four points lie on a circle of fixed radius. The radius is what the letter has and the rotation is where it puts it. L's radius is the largest, about 1.17; the origin letters have none. C at 0° is (+0.44, 0) and at 270° is (0, +0.44): the open bowl faces everyone, then faces up.

---

## Composition check

D at 0° is (+0.31, 0). C at 0° is (+0.44, 0). Closing the bowl against the stem moves the balance toward centre by adding ink on the +υ wall. B, two bowls on the same stem, is (+0.17, 0): further toward centre again. The family C, D, B runs inward from the everyone side as containment increases.

---

The seven-plane readings and the Omni-Weave bigram table are separate instruments and are not carried here.


---

## Process reading: υ over t

The balance point above is the 2D projection, ο. What the projection discards is the letter's progression along the depth axis, t. Following the Hellenic Ideogrammatic System, ο = Proj_x(υ): the static shadow is what remains once the process has been looked at end-on, and a symmetrical form casts a shadow at the origin whatever it did on the way.

To recover the process, each letter is traced over t and followed across the grid. **Every stroke has its own pen.** A stroke is one axis explored; the pen is not lifted and carried to the next, because there is no next for that pen. So a letter with four strokes is four independent traces, each with its own start, end and displacement, and the letter's process is the set of them. One image per letter, each stroke coloured blue at its own t = 0 through to red at its own t = 1, is in `process/`.

Per stroke: **start** and **end** on the grid, **net** as end minus start, and **winding** as the signed sweep about the origin, positive anticlockwise on the diagram. Per letter: the vector sum of the stroke nets and the sum of the windings. The sum is raw and not normalised, so a letter with three rightward bars really does move right three times.

Direction within a stroke is the Actualism document's left-to-right standard reading; its right-to-left inverse negates every net. Because page-right is −υ, a stroke traced anticlockwise on the page reads clockwise on the diagram, so O traced cos then sin comes out with negative winding. The handedness flips at the projection, and the flip is the diagram's, not the letter's.

### Summary

| Letter | ο (static) | strokes | net sum | winding sum |
|---|---|---|---|---|
| A | (+0.00, -0.12) | 3 | (-5.60, +0.00) | +2.37 |
| B | (+0.17, +0.00) | 3 | (+0.00, -6.72) | +3.22 |
| C | (+0.44, +0.00) | 1 | (+0.00, -2.16) | -6.89 |
| D | (+0.31, +0.00) | 2 | (+0.00, -6.72) | +3.22 |
| E | (+0.41, +0.01) | 4 | (-9.80, -3.36) | -2.82 |
| F | (+0.58, +0.58) | 3 | (-6.44, -3.36) | +0.00 |
| G | (+0.03, -0.06) | 3 | (+1.48, -0.96) | -7.90 |
| H | (+0.00, +0.00) | 3 | (-3.36, -6.72) | +0.00 |
| I | (+0.00, +0.00) | 1 | (+0.00, -3.36) | +0.00 |
| J | (-0.27, -0.54) | 2 | (+2.00, -2.48) | +3.36 |
| K | (+0.44, +0.00) | 3 | (-6.72, -3.36) | -2.82 |
| L | (+0.83, -0.82) | 2 | (-3.36, -3.36) | -5.64 |
| M | (+0.00, +0.20) | 4 | (-3.36, +0.00) | +4.97 |
| N | (+0.00, +0.00) | 3 | (-3.36, +3.36) | -0.00 |
| O | (+0.00, +0.00) | 1 | (-0.00, +0.00) | -8.86 |
| P | (+0.45, +0.64) | 2 | (+0.00, -5.04) | +0.20 |
| Q | (-0.10, -0.10) | 2 | (-1.20, -1.20) | -8.86 |
| R | (+0.22, +0.30) | 3 | (-2.28, -6.72) | -0.31 |
| S | (+0.00, +0.01) | 2 | (+1.68, -1.68) | +0.00 |
| T | (+0.00, +0.81) | 2 | (-3.36, -3.36) | +2.82 |
| U | (+0.00, -0.31) | 3 | (-3.36, -0.00) | -7.25 |
| V | (+0.00, +0.07) | 2 | (-3.36, +0.00) | -2.82 |
| W | (+0.00, +0.08) | 4 | (-3.36, +0.00) | -2.82 |
| X | (+0.00, -0.00) | 2 | (+0.00, -6.72) | -0.00 |
| Y | (-0.00, +0.42) | 3 | (+0.00, -5.04) | -0.00 |
| Z | (+0.00, +0.01) | 3 | (-3.36, -3.36) | +0.00 |

### Per-stroke traces

**A**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, -1.68) | (+0.00, +1.68) | (-1.68, +3.36) | +1.41 |
| 2 | (+0.00, +1.68) | (-1.68, -1.68) | (-1.68, -3.36) | +1.41 |
| 3 | (+1.12, -0.40) | (-1.12, -0.40) | (-2.24, +0.00) | -0.45 |

**B**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +1.84) | (+1.68, +0.16) | (+0.00, -1.68) | +3.02 |
| 3 | (+1.68, -0.16) | (+1.68, -1.84) | (+0.00, -1.68) | +3.02 |

**C**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (-1.29, +1.08) | (-1.29, -1.08) | (+0.00, -2.16) | -6.89 |

**D**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | +6.04 |

**E**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +1.68) | (-1.68, +1.68) | (-3.36, +0.00) | +2.82 |
| 3 | (+1.68, +0.00) | (-1.40, +0.00) | (-3.08, +0.00) | +0.00 |
| 4 | (+1.68, -1.68) | (-1.68, -1.68) | (-3.36, +0.00) | -2.82 |

**F**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +1.68) | (-1.68, +1.68) | (-3.36, +0.00) | +2.82 |
| 3 | (+1.68, +0.00) | (-1.40, +0.00) | (-3.08, +0.00) | +0.00 |

**G**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (-1.29, +1.08) | (-1.29, -1.08) | (+0.00, -2.16) | -6.89 |
| 2 | (-1.68, -1.20) | (-1.68, +0.00) | (+0.00, +1.20) | -1.01 |
| 3 | (-1.68, +0.00) | (-0.20, +0.00) | (+1.48, +0.00) | +0.00 |

**H**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (-1.68, +1.68) | (-1.68, -1.68) | (+0.00, -3.36) | +2.82 |
| 3 | (+1.68, +0.00) | (-1.68, +0.00) | (-3.36, +0.00) | +0.00 |

**I**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+0.00, +1.68) | (+0.00, -1.68) | (+0.00, -3.36) | +0.00 |

**J**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (-0.80, +1.68) | (-0.80, -0.80) | (+0.00, -2.48) | +0.99 |
| 2 | (-0.80, -0.80) | (+1.20, -0.80) | (+2.00, -0.00) | +2.37 |

**K**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +0.00) | (-1.68, +1.68) | (-3.36, +1.68) | +1.41 |
| 3 | (+1.68, +0.00) | (-1.68, -1.68) | (-3.36, -1.68) | -1.41 |

**L**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, -1.68) | (-1.68, -1.68) | (-3.36, +0.00) | -2.82 |

**M**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, -1.68) | (+1.68, +1.68) | (+0.00, +3.36) | +2.82 |
| 2 | (+1.68, +1.68) | (+0.00, -0.40) | (-1.68, -2.08) | -0.34 |
| 3 | (+0.00, -0.40) | (-1.68, +1.68) | (-1.68, +2.08) | -0.34 |
| 4 | (-1.68, +1.68) | (-1.68, -1.68) | (+0.00, -3.36) | +2.82 |

**N**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, -1.68) | (+1.68, +1.68) | (+0.00, +3.36) | +2.82 |
| 2 | (+1.68, +1.68) | (-1.68, -1.68) | (-3.36, -3.36) | -0.00 |
| 3 | (-1.68, -1.68) | (-1.68, +1.68) | (+0.00, +3.36) | -2.82 |

**O**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+0.00, +1.68) | (-0.00, +1.68) | (-0.00, +0.00) | -8.86 |

**P**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +1.84) | (+1.68, +0.16) | (+0.00, -1.68) | +3.02 |

**Q**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+0.00, +1.68) | (-0.00, +1.68) | (-0.00, +0.00) | -8.86 |
| 2 | (-0.48, -0.48) | (-1.68, -1.68) | (-1.20, -1.20) | -0.00 |

**R**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, -1.68) | (+0.00, -3.36) | -2.82 |
| 2 | (+1.68, +1.84) | (+1.68, +0.16) | (+0.00, -1.68) | +3.02 |
| 3 | (+0.60, +0.00) | (-1.68, -1.68) | (-2.28, -1.68) | -0.50 |

**S**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (-0.84, +1.00) | (+0.00, +0.16) | (+0.84, -0.84) | -2.08 |
| 2 | (+0.00, -0.16) | (+0.84, -1.00) | (+0.84, -0.84) | +2.08 |

**T**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (-1.68, +1.68) | (-3.36, +0.00) | +2.82 |
| 2 | (+0.00, +1.68) | (+0.00, -1.68) | (+0.00, -3.36) | +0.00 |

**U**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.68, +0.00) | (+0.00, -1.68) | -1.41 |
| 2 | (+1.68, +0.00) | (-1.68, -0.00) | (-3.36, -0.00) | -4.43 |
| 3 | (-1.68, +0.00) | (-1.68, +1.68) | (+0.00, +1.68) | -1.41 |

**V**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+0.00, -1.68) | (-1.68, -3.36) | -1.41 |
| 2 | (+0.00, -1.68) | (-1.68, +1.68) | (-1.68, +3.36) | -1.41 |

**W**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+1.00, -1.68) | (-0.68, -3.36) | -2.25 |
| 2 | (+1.00, -1.68) | (+0.00, +1.68) | (-1.00, +3.36) | +0.84 |
| 3 | (+0.00, +1.68) | (-1.00, -1.68) | (-1.00, -3.36) | +0.84 |
| 4 | (-1.00, -1.68) | (-1.68, +1.68) | (-0.68, +3.36) | -2.25 |

**X**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (-1.68, -1.68) | (-3.36, -3.36) | -0.00 |
| 2 | (-1.68, +1.68) | (+1.68, -1.68) | (+3.36, -3.36) | +0.00 |

**Y**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (+0.00, +0.00) | (-1.68, -1.68) | -0.00 |
| 2 | (-1.68, +1.68) | (+0.00, +0.00) | (+1.68, -1.68) | +0.00 |
| 3 | (+0.00, +0.00) | (+0.00, -1.68) | (+0.00, -1.68) | +0.00 |

**Z**

| stroke | start | end | net | winding |
|---|---|---|---|---|
| 1 | (+1.68, +1.68) | (-1.68, +1.68) | (-3.36, +0.00) | +2.82 |
| 2 | (-1.68, +1.68) | (+1.68, -1.68) | (+3.36, -3.36) | +0.00 |
| 3 | (+1.68, -1.68) | (-1.68, -1.68) | (-3.36, +0.00) | -2.82 |

### The nine at the origin, decoded

**I.** One stroke, (0, +1.68) to (0, −1.68). Net (0, −3.36), no winding. A fall down the will axis on the centre line.

**O.** One stroke, closed. Net zero, winding −8.86, the largest sweep in the set. No displacement and the most rotation: the spiral seen end-on, as the Hellenic document has it.

**H.** Three pens. Two stems both falling, one bar crossing everyone to me. Net sum (−3.36, −6.72), winding zero because the two stems cancel each other's turn. Hold is two descents and one crossing.

**N.** Three pens. Two stems rising, one diagonal from everyone-optimism to me-pessimism. Net sum (−3.36, +3.36), winding zero. The stems climb and the crossing drops.

**S.** Two pens, opposite senses, windings cancel exactly to zero. Net sum (+1.68, −1.68). Two turns that leave no rotation and a diagonal drift toward everyone and down.

**X.** Two pens, both from top to bottom, one each way. Net sum (0, −6.72), winding zero. Two falls whose sideways parts cancel.

**Z.** Three pens. Two bars crossing everyone to me, one diagonal back from me-optimism to everyone-pessimism. Net sum (−3.36, −3.36), winding zero.

**V and W.** Each stroke falls then rises. Net sum (−3.36, 0) for both, winding −2.82 for both. W has four pens to V's two and the same totals, because the second dip cancels the first.

**G.** Three pens. C's arc gives −6.89; the stub and inward bar add turn and pull the net to (+1.48, −0.96). Gather is C's sweep with the mouth partly closed and a drift back toward everyone.

### The other seventeen, recoded

**E.** Four pens: one stem falling, three bars each crossing everyone to me. Net sum (−9.80, −3.36), the largest sideways total in the set. Static (+0.41, 0), on the axis and slightly everyone. Energy stands near centre and moves toward the self three times over.

**F.** Three pens, the same without the base bar. Net sum (−6.44, −3.36). Static (+0.58, +0.58). Force stands productive and moves toward the self twice.

**C, D, B.** C is one pen, net (0, −2.16), winding −6.89. D adds the stem: net (0, −6.72), winding +3.22. B has two bowls on the stem: net (0, −6.72), winding +3.22, identical to D in total, because the second bowl's turn is what the first bowl's turn already was at half the size. Static walks inward, C (+0.44), D (+0.31), B (+0.17), while the process holds constant from D to B.

**P and R.** P: stem plus upper bowl, net (0, −5.04). R adds the leg, net (−2.28, −6.72). Release adds a drop toward the self that potential does not have.

**L.** Static (+0.83, −0.82), the most displaced form. Two pens, stem falling and bar crossing. Net (−3.36, −3.36), winding −5.64.

**T.** Static (0, +0.81). Bar crossing, stem falling. Net (−3.36, −3.36), winding +2.82. The same net as L with opposite winding: L turns at its foot, T at its head.

**A.** Three pens: two legs converging upward and the bar crossing. Net sum (−5.60, 0), winding +2.37. The legs' vertical parts cancel and the bar and the second leg both carry it toward the self.

**M.** Four pens. Net (−3.36, 0), winding +4.97. Enters and leaves the pessimism line, having climbed twice.

**Q.** O's sweep, −8.86, unchanged, with the tail adding net (−1.20, −1.20). Query is the sealed cycle plus a short drop toward the regressive corner.

**J.** Two pens. Net (+2.00, −2.48), winding +3.36. The only base form in the regressive quadrant, and its process hooks back toward everyone as it falls.

**K.** Three pens. Stem falling, two arms diverging from the stem's middle to the me wall. Net (−6.72, −3.36), winding −2.82.

**U.** Three pens. Net (−3.36, 0), winding −7.25. V's totals with a much larger sweep, because the bowl is a turn where V is a corner.

**Y.** Three pens converging on the centre then dropping. Net (0, −5.04), winding zero. Two arms cancel sideways; the stem carries it down.
