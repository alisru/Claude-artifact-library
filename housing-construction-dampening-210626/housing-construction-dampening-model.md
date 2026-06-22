# Construction Dampening Model: x vs y, the Investment Break-Even Question, and the General Release-Rate Pattern

## The Question

If every new house built lowers the value of all existing housing by some rate x while adding its own value y to the market, what happens if x ever catches up to y. At what point, if any, does fast enough construction break the investment scheme entirely, where existing property stops being a viable store of value.

## Definitions, As Refined Through The Conversation

S = total existing housing stock (number of properties) in the market being studied
$E = the average price across that existing stock, the norm or going rate, not a regulated floor
N = number of new properties built in the period being studied
y = the value of an individual new house, variable, y₁ → ∞ depending on what gets built
ε = price elasticity of housing supply for that specific market, the standard economic term for how much price moves for a given change in supply
x = the price drag applied to existing stock from satisfaction of demand, i.e. saturation, expressed either as a one-off percentage or as a rate over an arbitrary timeframe

## The Core Derivation

Standard supply and demand elasticity gives the percentage price change across existing stock from adding N units to a stock of S:

percent change in E = negative one divided by epsilon, multiplied by N divided by S

$$\Delta E\% = -\dfrac{1}{\varepsilon} \cdot \dfrac{N}{S}$$

This is the textbook relationship: percentage change in quantity supplied, which is N divided by S, translated into a percentage change in price through the elasticity coefficient.

Converting that into dollar terms, x per existing property becomes:

x in dollars = E multiplied by one divided by epsilon, multiplied by N divided by S

$$x = E \cdot \dfrac{1}{\varepsilon} \cdot \dfrac{N}{S}$$

The total dollar drag across the entire existing stock, meaning the aggregate amount by which the whole market's value falls, is S multiplied by that per property figure:

Total drag = S multiplied by E multiplied by one divided by epsilon multiplied by N divided by S

$$\text{Drag}_{total} = S \cdot E \cdot \dfrac{1}{\varepsilon} \cdot \dfrac{N}{S}$$

The S in the numerator and the S in the denominator cancel. What is left is:

Total drag = E multiplied by N, divided by epsilon

$$\text{Drag}_{total} = \dfrac{E \cdot N}{\varepsilon}$$

This cancellation is the important and slightly counterintuitive structural result. The total dollar drag across the whole existing market does not depend on how large the existing stock is. It falls out of the equation entirely. It only depends on the average price E, the number of new units N, and the elasticity ε. Stock size still matters for how thinly that drag is spread per individual property, a bigger stock dilutes the hit per owner, but it does not matter for the total dollars at stake market wide.

## The Break-Even Condition

Total value created by the new builds, the y side, is N multiplied by the average new build value, written as y-bar:

Total value created = N multiplied by y-bar

$$\text{Value}_{total} = N \cdot \bar{y}$$

Setting total drag equal to total value created, the point where the scheme would theoretically break:

E multiplied by N divided by epsilon = N multiplied by y-bar

$$\dfrac{E \cdot N}{\varepsilon} = N \cdot \bar{y}$$

N cancels on both sides. What remains is the actual break-even condition:

E divided by epsilon = y-bar

$$\dfrac{E}{\varepsilon} = \bar{y}$$

This says the break-even point does not depend on N at all once you simplify it fully. The question of how fast construction would need to be partly dissolves, because the N you build does not change whether the system is balanced or not, it only changes how large the swings are while staying balanced or not. What actually decides whether the scheme breaks is whether the average price of new construction, y-bar, falls to or below the existing average price divided by the elasticity coefficient, E over epsilon.

In a highly inelastic market, where epsilon is well below 1, E divided by epsilon is larger than E itself. That means new builds would need to sell for more than the existing average for the scheme to break, which is the opposite of what an oversupply glut actually looks like. Gluts clear inventory by pricing new stock at or below the existing average, not above it.

In a highly elastic market, where epsilon is above 1, E divided by epsilon drops below E, meaning the bar for y-bar to clear gets easier. New builds would not need to be unusually expensive, just not severely discounted, for the scheme to break in that market.

## Sydney, With Real Numbers

Greater Sydney existing dwelling stock, 2021 Census: 2,079,287 dwellings. Source: https://profile.id.com.au/australia/population?WebID=260

NSW mean dwelling price, September quarter 2025: $1,295,900. Source: https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/total-value-dwellings/latest-release/

This is a state-level figure rather than Sydney-specific. Sydney proper almost certainly runs higher than this NSW-wide mean, since regional NSW pulls the average down. Treat $1,295,900 as a conservative floor for E, not a precise Sydney figure.

Sydney housing supply elasticity, houses: 0.2. Apartments: 0.8. Source: peer reviewed estimate using LGA level annual data from 1991 to 2012, published in Applied Economics, https://www.tandfonline.com/doi/full/10.1080/00036846.2017.1307936, and the underlying UNSW thesis at https://unsworks.unsw.edu.au/entities/publication/f60a308f-20f4-479a-b0dc-69bb324edaa9

A more recent 2025 paper using state level NSW data to 2019 found supply elasticity of 0.36 at the state level, but found housing supply effectively perfectly inelastic specifically in the metropolitan area, meaning epsilon approaching zero for Sydney itself under that model. Source: https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-8454.12372

Running the formula with S = 2,079,287, E = $1,295,900, N = 1,000, and epsilon = 0.2, the established Sydney house elasticity figure:

Total drag = E multiplied by N divided by epsilon
Total drag = 1,295,900 multiplied by 1,000, divided by 0.2
Total drag = 1,295,900,000 divided by 0.2
Total drag = 6,479,500,000

$$\text{Drag}_{total} = \dfrac{E \cdot N}{\varepsilon} = \dfrac{1{,}295{,}900 \times 1{,}000}{0.2} = \dfrac{1{,}295{,}900{,}000}{0.2} = 6{,}479{,}500{,}000$$

Adding 1,000 new houses to Greater Sydney's existing stock, under this elasticity estimate, produces an aggregate drag of approximately 6.48 billion dollars spread across the entire existing 2.08 million property stock.

Spread per existing property, that total divided by S:

6,479,500,000 divided by 2,079,287 = approximately 3,116

$$\dfrac{\text{Drag}_{total}}{S} = \dfrac{6{,}479{,}500{,}000}{2{,}079{,}287} \approx 3{,}116$$

So under this model, 1,000 new houses built in Sydney costs each existing property owner, on average, somewhere in the order of 3,116 dollars in price suppression. Across a portfolio of, say, 10 properties, that is roughly 31,160 dollars of suppressed value from that single year's 1,000-unit addition.

For the break-even condition, E divided by epsilon, using the same numbers:

E divided by epsilon = 1,295,900 divided by 0.2 = 6,479,500

$$\dfrac{E}{\varepsilon} = \dfrac{1{,}295{,}900}{0.2} = 6{,}479{,}500$$

For the investment scheme to break under this elasticity, the average new house being built would need to sell for roughly 6.48 million dollars, about five times the existing NSW mean. That is not what oversupply looks like in practice, new builds sell at or near the existing average, sometimes below it during a glut, which is precisely why the scheme structurally does not break under normal construction dynamics, even at high volume.

If the more recent 2025 paper's metro-level near-zero elasticity finding is used instead of the 0.2 figure, the one divided by epsilon term grows extremely large, meaning a given N produces a much larger total drag for the same N. This is the scenario where Sydney's notoriously constrained supply response would make each marginal unit of construction count for more in price suppression terms than in a more elastic market. It does not change the structural conclusion that total value created scales with N just as total drag does, so the break even condition, E divided by epsilon equals y-bar, still does not depend on N, it just shifts the bar for y-bar higher, making the scheme even harder to break, since E divided by a near zero epsilon approaches infinity, meaning no realistic y-bar could ever clear it.

## Why This Matters For The Original Claim

The original intuition was that if x ever caught up to y, fast enough construction would break the investment scheme entirely. The corrected model shows the comparison was framed at the wrong level. The proper comparison is not x against a single y, it is total drag, E multiplied by N over epsilon, against total value created, N multiplied by y-bar. Both sides scale with N, so N cancels, and the question collapses to a single fixed condition that does not depend on how fast or how much gets built. It depends only on whether new build prices fall low enough relative to the existing average, scaled by elasticity, which in any normal market, let alone an inelastic one like Sydney, is not something construction volume by itself can trigger.

The genuinely real and empirically supported part of the original intuition survives intact: more construction does suppress existing price growth, and an inelastic market like Sydney, where epsilon sits around 0.2 for houses, means each marginal new unit suppresses prices more than the same unit would in a more elastic market like, for comparison, Tokyo. That part of the model holds. What does not hold is the idea that this suppression effect could ever outrun the value being created by the construction itself, because both effects are driven by the same N and scale together.

## Extension: y-bar As A Function Of N, Not A Constant

The model above treats x as derived from epsilon, N, and S, but treats y-bar, the average value of the new builds themselves, as a fixed external input. That is incomplete. In reality, a developer or producer releasing N units into the market is not just dragging the price of existing stock, they are also competing against their own batch. Selling more units this period means accepting a lower clearing price on those same units, not just on the stock already standing. This is documented in real estate economics as the absorption rate problem: a landowner releasing lots faster gets lower price growth on the lots they are currently selling, because the price gain available to them is market demand growth minus their own price-suppressing effect from flooding the market. The optimal release rate balances the gain from selling now against the price erosion caused by selling too much, too fast, into a market of finite depth.

This is empirically visible in current data, not just theoretical. Builders in early 2026 have been holding new-build prices roughly flat only by actively discounting and offering incentives to keep absorption steady, while resale prices on existing stock were separately slipping. Separately, new-home median sale prices fell eight percent year over year in late 2025 data, with a quarter of new homes selling under three hundred thousand dollars, the largest share in that low price bracket since 2021, specifically because builders kept discounting and offering rate buydowns to move volume rather than let inventory sit.

Folding this into the model, y-bar becomes a declining function of N, written y-bar of N, rather than a constant. The break-even condition becomes:

$$\dfrac{E \cdot N}{\varepsilon} = N \cdot \bar{y}(N)$$

N no longer cancels cleanly, since y-bar is itself a function of N. Dividing through still leaves N embedded on the right side:

$$\dfrac{E}{\varepsilon} = \bar{y}(N)$$

This looks identical in form to the original break-even condition, but its meaning has changed. It is no longer a fixed threshold that y-bar either clears or does not, it is a condition to solve for N, since y-bar of N drifts downward as N rises. Fast enough, sustained enough release could in principle push y-bar of N down toward E over epsilon from above. Whether that threshold is ever actually reached, or whether y-bar of N asymptotes to some floor above it, depends on the shape of the decay function itself, which depends on financing costs, holding costs, land tax exposure, and the producer's own time horizon for realizing returns. That shape is not something this document can responsibly assign a number to without a Sydney-specific empirical estimate of how new-build pricing degrades with release volume, which is a different and less established body of research than the supply elasticity figures used for x.

## Generalization: This Is A Release-Rate Model, Not A Housing Model

The coupled structure above, drag on existing stock plus self-cannibalization on the new release, both driven by the same release rate N into a market of finite absorptive capacity, is not specific to housing. It is the general problem facing any actor who controls the rate at which new units enter a market where new and existing units sit on a shared, substitutable quality and price gradient.

The condition for the effect to apply is not whether units are literally new or used. It is whether units across that gradient are close enough substitutes, within a real buyer's actual consideration set, that releasing more supply at one point on the gradient pulls demand away from other points on it. A house built in 1995 and a house built in 2026 compete for some of the same buyers despite the age gap. A 2019 iPhone in good condition and a current model compete for some of the same buyers despite the generational gap. The structural mechanic is identical in both cases: a finite pool of demand, a continuum of quality-differentiated units competing within it, and a controller of release rate whose output decisions affect prices across the whole gradient at once, not just at the point they are releasing into.

This pattern shows up wherever a producer or coordinated producer class controls release timing into a market with these properties. Diamond markets operated for decades on exactly this logic, with deliberate restriction of release volume specifically because flooding supply would simultaneously depress prices on newly mined stones and on every previously sold stone held by owners and dealers, since both compete in the same substitutable market. Oil production quotas under OPEC function the same way, output restriction exists because unrestricted pumping would crater the price of both the marginal barrel being produced and the value of reserves already held. Limited production runs in collectibles, sneakers, trading cards, and art prints work on a smaller version of the same mechanic, scarcity is manufactured because uncontrolled release would discount the new run while simultaneously devaluing every unit from prior runs still held by collectors, since both compete for the same buyer base.

Where the effect does not apply is where units genuinely are not substitutes within any real buyer's consideration set, where the good is not durable or storable so there is no meaningful existing stock to drag, or where demand is effectively unbounded relative to any realistic release rate so the market never approaches its absorptive ceiling. Outside those edge cases, any actor injecting continual supply into a high demand, constrained supply environment, where new and existing units are points on the same gradient rather than separate markets, faces this same coupled two-sided pricing structure. Housing is simply the instance this document happened to model in detail, the structure itself is general.

## The Price Floor: How Far Can Existing Stock Actually Fall?

The break-even condition established earlier solves for what new builds would need to cost for the system to reach equilibrium. Inverting it to solve for E instead gives the floor price of existing stock, the level at which the drag x applies to existing stock exactly equals the value y-bar that new construction adds back in:

$$E_{floor} = \bar{y} \cdot \varepsilon$$

The existing stock price floor is the average new-build clearing price multiplied by the elasticity coefficient. For Sydney houses, with ε = 0.2 and treating ȳ as approximating the current NSW mean of $1,295,900:

$$E_{floor} = 1{,}295{,}900 \times 0.2 = 259{,}180$$

Sydney house prices would need to fall to approximately $259,000 before construction dampening is fully offset by the value new builds add back. That is roughly an 80% nominal collapse from current levels. This is why prices cannot meaningfully fall under normal market conditions: the gap between current E and E_floor is structurally enormous precisely because ε is so small. A more inelastic market produces a lower floor as a fraction of current prices, because each new unit does more damage to existing prices relative to what it adds back, setting the equilibrium point correspondingly lower.

Under the 2025 paper's near-zero metropolitan elasticity finding, E_floor approaches zero entirely. In a perfectly inelastic market, no amount of construction ever adds enough value back to offset the drag it applies, meaning the floor is theoretically unbounded to the downside from the dampening mechanism alone. Practical floors still exist, set by land cost, construction cost, and financing, but the dampening model itself offers no resistance. This is the structural explanation for why highly constrained inner-city markets behave as if prices have a one-way ratchet: the mathematical floor sits so far below any realistic trading range that the mechanism never comes close to binding.

### Sub-case: A 50% Price Fall

If E falls 50% from the current NSW mean, E becomes $647,950. The naive reading is that this halves the distance to the floor. It does not, because ȳ moves with E. New-build pricing tracks the existing market: developers will not build at a loss and cannot command a premium in a falling market, so ȳ compresses alongside E, and E_floor, being ȳ × ε, falls proportionally too. The floor is not a fixed nominal number, it is a fraction of wherever the market currently sits, and it rescales downward with the market rather than staying anchored.

The condition where a 50% fall does close the gap to the floor is when construction costs set a hard nominal floor on ȳ that does not compress at the same rate existing stock does. Land acquisition, materials, and labour costs are stickier than resale prices in a sharp downturn. If E falls 50% but construction cost floors prevent ȳ from falling more than, say, 20%, the gap between E and ȳ narrows and the break-even condition E/ε = ȳ can be approached from below for the first time. In that scenario, developers stop building, not because the model breaks, but because margins are gone, which is the real-world mechanism: construction halts in a downturn not because of abstract equilibrium math but because ȳ can no longer cover cost of production. That halt then removes the supply-side dampening force entirely, allowing E to stabilise or recover, which is the self-correcting mechanism that prevents the floor from ever being reached in practice.

$$\text{Gap to floor} = E - E_{floor} = E - \bar{y} \cdot \varepsilon$$

In a downturn with sticky construction costs, as E falls faster than ȳ:

$$\text{Gap narrows as } \Delta E > \Delta \bar{y}$$

The gap approaching zero is the signal that development becomes unviable, triggering the supply halt that arrests the fall.

### Sub-case: Affordability-Locked New Stock

If a portion of new builds are locked into an affordability model, government-mandated price caps, shared equity schemes, or community land trusts, they enter the existing stock at ȳ_affordable, which is fixed below market rather than tracking E. This changes the model structure in two ways simultaneously.

First, the drag x still applies to the full existing stock unchanged. Every affordable unit added still satisfies demand and suppresses E via the elasticity mechanism, regardless of what it sold for.

Second, the value-add side is now a weighted average across market-rate and affordable tranches:

$$\bar{y}_{weighted} = \frac{N_{market} \cdot \bar{y}_{market} + N_{affordable} \cdot \bar{y}_{affordable}}{N_{total}}$$

Since ȳ_affordable is fixed below E while ȳ_market tracks E, the weighted average ȳ is pulled down relative to a pure market-rate build program of the same N. The break-even condition becomes:

$$\dfrac{E}{\varepsilon} = \bar{y}_{weighted}$$

With ȳ_weighted now below ȳ_market, the right-hand side is easier to reach from below, meaning the floor condition is closer to binding than under pure market-rate construction. Affordable housing mandates at scale are therefore a structural lever that pushes a market toward the floor condition faster than volume alone could, because they decouple the value-add of new stock from the price level of existing stock while leaving the drag mechanism fully intact.

There is a second-order effect compounding this. Affordable units entering the pool also pull E itself down compositionally, since they are now part of the average the pool is priced at. This in turn lowers E_floor (since E_floor = ȳ_weighted × ε), but it lowers E faster than it lowers E_floor, because E is being dragged by both the affordability discount and the supply dampening effect simultaneously while E_floor only moves with ȳ_weighted. The gap between E and E_floor compresses from both sides at once. A large enough affordable housing program, sustained long enough, could in principle be self-reinforcing in this compression, driving the market toward a structurally lower equilibrium rather than simply suppressing growth at the current level.
