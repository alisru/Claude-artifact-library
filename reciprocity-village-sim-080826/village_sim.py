"""
Reciprocity Village Simulation
Prices every resource through the Universal Force Equation of Price.

Price = (P_you/P_soc) * [ S*U / (Rn*(1-Ra)) ] * (P_other/P_soc)
      = m1 * R * m2

Author framework: Al-Is-Ru / Descend - Spear - Through
Simulation implementation: Claude
"""

import math
import random
import json

random.seed(7)

ALPHA = 0.9   # weight on objective Need
BETA  = 0.1   # weight on subjective Want (alpha >> beta)

# ---------------------------------------------------------------
# Normalisation helpers. Everything lives on the absolute [0,2] scale.
# ---------------------------------------------------------------

def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def n_over_zero(numer, denom, eps=1e-9):
    """Boundary axiom: n/0 -> n+1 rather than infinity.
    Finite social rejection, not an unpayable infinity."""
    if denom <= eps:
        return numer + 1.0
    val = numer / denom
    ceiling = numer + 1.0
    # the axiom sets the hard ceiling; approach it, never exceed it
    return min(val, ceiling)


# ---------------------------------------------------------------
# Resource nodes: a (zone, quality) pair
# ---------------------------------------------------------------

class Node:
    def __init__(self, kind, zone_name, danger, quality, stock, regen, alt_count):
        self.kind = kind              # 'food' | 'wood' | 'ore'
        self.zone = zone_name
        self.danger = danger          # [0,2] normalised difficulty of the zone
        self.quality = quality        # 0.5 low, 1.0 mid, 1.5 high (yield multiplier)
        self.stock = stock
        self.stock0 = stock
        self.regen = regen            # units restored per tick
        self.alt_count = alt_count    # how many substitute sources exist

    # --- Reality Tensor components -----------------------------

    def S(self):
        """Systemic scarcity, normalised, S >= 1, ceiling 2.0"""
        depletion = 1.0 - (self.stock / max(self.stock0, 1e-9))
        return clamp(1.0 + depletion, 1.0, 2.0)

    def Rn(self, tools):
        """Renewability. High Rn dampens price. Normalised to [0,2]."""
        base = self.regen / max(self.stock0 * 0.05, 1e-9)
        return clamp(base, 0.05, 2.0)

    def difficulty(self, tools):
        """Absolute difficulty to acquire the ALTERNATIVE:
        integrates physical danger, caloric cost, and time investment.
        Tools reduce it."""
        tool_f = tools.difficulty_reduction(self.kind)
        d = (self.danger * 1.0) + (self.danger * 0.5) + (self.danger * 0.5)
        return max(0.05, d * tool_f)

    def Ra(self, tools):
        """Resistance to alternatives, bounded [0,1).
        Substitutability = available alternative resource / absolute difficulty.
        Ra -> 1 as substitution becomes impossible."""
        sub = self.alt_count / self.difficulty(tools)
        return clamp(1.0 / (1.0 + sub), 0.0, 0.999)

    def reality_tensor(self, U, tools):
        """R = S*U / (Rn*(1-Ra))  -- the invariant. Not set by either party."""
        S = self.S()
        Rn = self.Rn(tools)
        Ra = self.Ra(tools)
        denom = Rn * (1.0 - Ra)
        return n_over_zero(S * U, denom)

    def effort_cost(self, tools):
        """What it costs the gatherer to work this node (risk + time)."""
        tool_f = tools.difficulty_reduction(self.kind)
        return (0.4 + self.danger) * tool_f

    def yield_per_trip(self, tools):
        return tools.gather_rate(self.kind) * self.quality


# ---------------------------------------------------------------
# Tools: raise gathering rate, lower difficulty, usually both
# ---------------------------------------------------------------

class Toolset:
    def __init__(self):
        self.level = {'food': 0, 'wood': 0, 'ore': 0}

    def gather_rate(self, kind):
        return 1.0 + 0.35 * self.level[kind]

    def difficulty_reduction(self, kind):
        return max(0.25, 1.0 - 0.12 * self.level[kind])

    def invent(self, kind):
        self.level[kind] += 1


# ---------------------------------------------------------------
# The Village
# ---------------------------------------------------------------

class Village:
    def __init__(self, ambition=1.0):
        self.pop = 20.0
        self.tools = Toolset()
        self.stores = {'food': 40.0, 'wood': 25.0, 'ore': 5.0}
        self.processing_capacity = 12.0   # units it can actually service per tick
        self.debt = 0.0
        self.reality_gap = 0.0            # accumulated transactional debt vs true price
        self.ambition = ambition          # desired-size multiplier: imagination + ego
        self.price_lie = 1.0              # manipulation factor applied to posted prices
        self.log = []
        self.first_half_depleted = {}   # (zone, quality) -> tick it fell below 50%
        self.profile_series = []

        self.nodes = self._build_world()

    def _build_world(self):
        zones = [
            ('Home Field',  0.25, 6),
            ('Near Wood',   0.75, 4),
            ('Deep Forest', 1.25, 2),
            ('Black Ridge', 1.75, 1),
        ]
        qualities = [('low', 0.5), ('mid', 1.0), ('high', 1.5)]
        nodes = []
        for kind in ('food', 'wood', 'ore'):
            for zname, danger, alts in zones:
                for qname, q in qualities:
                    # High quality is scarce and slow to renew in safe zones.
                    # Low quality is abundant and renews fast everywhere.
                    scarcity_bias = {0.5: 1.0, 1.0: 0.55, 1.5: 0.25}[q]
                    danger_bias = 0.6 + 0.5 * danger
                    stock = 120.0 * scarcity_bias * danger_bias
                    regen = (3.2 * scarcity_bias) * (1.0 + 0.2 * danger)
                    nodes.append(Node(kind, zname, danger, q, stock, regen, alts))
        return nodes

    # --- Need / Want -> transactional mass ---------------------

    def need(self, kind):
        """N = proximity to a failure state. [0,2]."""
        required = {'food': self.pop * 0.9, 'wood': self.pop * 0.4, 'ore': self.pop * 0.15}[kind]
        have = self.stores[kind]
        shortfall = clamp(1.0 - (have / max(required, 1e-9)), -1.0, 1.0)
        return clamp(1.0 + shortfall, 0.0, 2.0)

    def want(self, kind):
        """W = subjective preference. Ambition inflates want, not need."""
        return clamp(0.4 * self.ambition, 0.0, 2.0)

    def pressure(self, kind):
        return ALPHA * self.need(kind) + BETA * self.want(kind)

    def p_soc(self, kind):
        """Social baseline pressure for the good."""
        return {'food': 1.0, 'wood': 0.8, 'ore': 0.6}[kind]

    def urgency(self, kind):
        """U: velocity modifier on the acquisition WINDOW for this specific good.
        Asymptotes to 1.0 when there is no hard window."""
        n = self.need(kind)
        if n <= 1.0:
            return 1.0
        return clamp(1.0 + (n - 1.0) * 1.0, 1.0, 2.0)

    # --- Price ------------------------------------------------

    def geometric_price(self, node):
        """The true two-body price. No manipulation."""
        U = self.urgency(node.kind)
        R = node.reality_tensor(U, self.tools)
        m1 = self.pressure(node.kind) / self.p_soc(node.kind)      # village as buyer
        m2 = clamp(0.35 + node.effort_cost(self.tools) * 0.5, 0.0, 2.0)  # gatherer as seller
        if m1 <= 1e-9 or m2 <= 1e-9:
            return 0.0   # two-body requirement: no unilateral pricing
        return m1 * R * m2

    def posted_price(self, node):
        """What the village actually publishes. Diverges from geometric under debt."""
        return self.geometric_price(node) * self.price_lie

    # --- The four states --------------------------------------

    def actual_ideal(self):
        """What the village CAN produce-service right now: instant-processing state."""
        return self.processing_capacity

    def actual_desired(self):
        """What it actually needs to not decay: real subsistence throughput."""
        return self.pop * 0.55

    def desired_size(self):
        """What it WANTS to be. Bounded by imagination and ego, not by capacity."""
        return self.pop * (1.0 + 0.06 * self.ambition)

    def true_ideal(self):
        """Unbounded potential. Reported as the headroom the village never touches."""
        return float('inf')

    # --- One tick ---------------------------------------------

    def step(self, t):
        # 1. Gatherers pick nodes by net return: value of yield minus effort.
        # Labour is bounded by organisation, not by headcount. Debt-financed
        # population adds mouths, not effective gatherers.
        trips = int(min(self.pop * 0.6, 25 + 2 * sum(self.tools.level.values())))
        harvested = {'food': 0.0, 'wood': 0.0, 'ore': 0.0}
        extraction_by_zone = {}

        for _ in range(trips):
            best, best_score = None, -1e9
            for nd in self.nodes:
                if nd.stock < 1.0:
                    continue
                gp = self.posted_price(nd)
                score = gp * nd.yield_per_trip(self.tools) - nd.effort_cost(self.tools)
                if score > best_score:
                    best, best_score = nd, score
            if best is None:
                continue
            take = min(best.yield_per_trip(self.tools) * 1.0, best.stock)
            best.stock -= take
            harvested[best.kind] += take * best.quality
            key = (best.zone, best.quality)
            extraction_by_zone[key] = extraction_by_zone.get(key, 0.0) + take

        # 1b. Record the first time each (zone, quality) class falls below half.
        for nd in self.nodes:
            key = (nd.zone, nd.quality)
            if key not in self.first_half_depleted and nd.stock < nd.stock0 * 0.5:
                self.first_half_depleted[key] = t

        # 2. Regeneration
        for nd in self.nodes:
            nd.stock = min(nd.stock0, nd.stock + nd.regen)

        # 3. Processing gates everything. Growth is tied to throughput, not intake.
        raw_in = sum(harvested.values())
        processed = min(raw_in, self.processing_capacity)
        unprocessed = raw_in - processed

        for k in self.stores:
            self.stores[k] += harvested[k] * (processed / max(raw_in, 1e-9))
            self.stores[k] -= {'food': self.pop * 0.5, 'wood': self.pop * 0.2, 'ore': self.pop * 0.05}[k]
            self.stores[k] = max(0.0, self.stores[k])

        # 4. Growth from processing throughput alone
        real_growth = 0.05 * processed - 0.02 * self.pop
        desired_growth = self.desired_size() - self.pop

        # 5. The gap. Anything wanted beyond throughput is financed, not earned.
        gap = max(0.0, desired_growth - real_growth)
        if gap > 0:
            self.debt += gap * 2.5
            # the cover: suppress posted prices to make the shortfall invisible
            self.price_lie = clamp(self.price_lie - 0.02 * gap, 0.25, 1.0)
        else:
            self.price_lie = clamp(self.price_lie + 0.01, 0.25, 1.0)
            self.debt = max(0.0, self.debt - 0.5)

        # accumulated divergence between posted and geometric price
        div = sum(abs(self.geometric_price(n) * (1 - self.price_lie)) for n in self.nodes)
        self.reality_gap += div / len(self.nodes)

        # population moves toward desired, but only debt-financed beyond real growth
        self.pop += real_growth + gap * 0.8
        self.pop = max(5.0, self.pop)

        # 6. Invention: surplus funds tools. Raises rate AND cuts difficulty.
        if processed > self.actual_desired() * 1.05 and random.random() < 0.30:
            kind = random.choice(['food', 'wood', 'ore'])
            if self.tools.level[kind] < 8:
                self.tools.invent(kind)

        # 7. Processing capacity grows with pop and tools, but slower than ambition
        self.processing_capacity = 12.0 + 0.25 * self.pop + 1.5 * sum(self.tools.level.values())

        self.log.append({
            't': t,
            'pop': round(self.pop, 2),
            'processed': round(processed, 2),
            'unprocessed': round(unprocessed, 2),
            'debt': round(self.debt, 2),
            'price_lie': round(self.price_lie, 3),
            'reality_gap': round(self.reality_gap, 2),
            'actual_ideal': round(self.actual_ideal(), 2),
            'actual_desired': round(self.actual_desired(), 2),
            'desired_size': round(self.desired_size(), 2),
            'tools': dict(self.tools.level),
        })
        self.profile_series.append({f'{k[0]}|q{k[1]}': round(v[2], 3)
                                    for k, v in self.quality_profile().items()})

    def quality_profile(self):
        """Remaining stock share by (zone, quality). Tests the equalisation prediction."""
        out = {}
        for nd in self.nodes:
            key = (nd.zone, nd.quality)
            a, b = out.get(key, (0.0, 0.0))
            out[key] = (a + nd.stock, b + nd.stock0)
        return {k: (v[0], v[1], v[0] / max(v[1], 1e-9)) for k, v in out.items()}


def run(ambition, ticks=60):
    v = Village(ambition=ambition)
    for t in range(ticks):
        v.step(t)
    return v


def variance(vals):
    m = sum(vals) / len(vals)
    return sum((x - m) ** 2 for x in vals) / len(vals)


def report(name, v):
    print(f'\n=== {name.upper()} ===')
    last = v.log[-1]
    print(f"pop {last['pop']}  processed/tick {last['processed']}  "
          f"debt {last['debt']}  posted-price factor {last['price_lie']}  "
          f"reality gap {last['reality_gap']}")
    print(f"actual ideal (can service) {last['actual_ideal']}  |  "
          f"actual desired (needs) {last['actual_desired']}  |  "
          f"desired size (ego) {last['desired_size']}")
    print(f"tools {last['tools']}")

    print('\n depletion order (tick each class first fell below 50%):')
    order = sorted(v.first_half_depleted.items(), key=lambda kv: kv[1])
    for (zone, q), tick in order:
        print(f'   t={tick:>3}  {zone:<12} quality {q}')

    prof = v.quality_profile()
    print('\n remaining stock fraction by zone and quality:')
    for zone in ['Home Field', 'Near Wood', 'Deep Forest', 'Black Ridge']:
        row = [f'q{q}:{prof[(zone, q)][2]:.2f}' for q in (0.5, 1.0, 1.5)]
        print(f'   {zone:<12} ' + '  '.join(row))

    # equalisation test: does variance in high-quality availability across
    # danger zones shrink over time?
    hq_keys = [f'{z}|q1.5' for z in ['Home Field', 'Near Wood', 'Deep Forest', 'Black Ridge']]
    early = variance([v.profile_series[3][k] for k in hq_keys])
    late = variance([v.profile_series[-1][k] for k in hq_keys])
    print(f'\n high-quality cross-zone variance: early {early:.4f} -> late {late:.4f}  '
          f'({"converging" if late < early else "diverging"})')


if __name__ == '__main__':
    for name, amb in [('restrained', 0.4), ('moderate', 1.0), ('ego-driven', 2.2)]:
        report(name, run(amb))
