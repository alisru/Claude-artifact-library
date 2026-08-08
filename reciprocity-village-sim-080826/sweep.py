import random, importlib, statistics
import village_sim as vs

def sweep(amb, seeds=12):
    hq_conv, frontier_share, debts, tool_tot = [], [], [], []
    for s in range(seeds):
        random.seed(s)
        v = vs.run(amb)
        hq = [f'{z}|q1.5' for z in ['Home Field','Near Wood','Deep Forest','Black Ridge']]
        e = vs.variance([v.profile_series[3][k] for k in hq])
        l = vs.variance([v.profile_series[-1][k] for k in hq])
        hq_conv.append(1 if l < e else 0)
        prof = v.quality_profile()
        safe = prof[('Home Field',1.0)][2] + prof[('Near Wood',1.0)][2]
        danger = prof[('Deep Forest',1.0)][2] + prof[('Black Ridge',1.0)][2]
        frontier_share.append(danger - safe)   # >0 means frontier better preserved
        debts.append(v.log[-1]['debt'])
        tool_tot.append(sum(v.log[-1]['tools'].values()))
    return hq_conv, frontier_share, debts, tool_tot

for name, amb in [('restrained',0.4), ('moderate',1.0), ('ego-driven',2.2)]:
    c, f, d, t = sweep(amb)
    print(f'{name:<12} hq-converged {sum(c)}/{len(c)}  '
          f'frontier-minus-safe median {statistics.median(f):+.2f}  '
          f'debt median {statistics.median(d):.0f}  '
          f'tools median {statistics.median(t):.1f}')
