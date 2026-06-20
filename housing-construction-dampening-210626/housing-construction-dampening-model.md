# Construction Dampening Model: x vs y, and the Investment Break-Even Question

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

LaTeX:
\Delta E\% = -\dfrac{1}{\varepsilon} \cdot \dfrac{N}{S}

This is the textbook relationship: percentage change in quantity supplied, which is N divided by S, translated into a percentage change in price through the elasticity coefficient.

Converting that into dollar terms, x per existing property becomes:

x in dollars = E multiplied by one divided by epsilon, multiplied by N divided by S

LaTeX:
x = E \cdot \dfrac{1}{\varepsilon} \cdot \dfrac{N}{S}

The total dollar drag across the entire existing stock, meaning the aggregate amount by which the whole market's value falls, is S multiplied by that per property figure:

Total drag = S multiplied by E multiplied by one divided by epsilon multiplied by N divided by S

LaTeX:
\text{Drag}_{total} = S \cdot E \cdot \dfrac{1}{\varepsilon} \cdot \dfrac{N}{S}

The S in the numerator and the S in the denominator cancel. What is left is:

Total drag = E multiplied by N, divided by epsilon

LaTeX:
\text{Drag}_{total} = \dfrac{E \cdot N}{\varepsilon}

This cancellation is the important and slightly counterintuitive structural result. The total dollar drag across the whole existing market does not depend on how large the existing stock is. It falls out of the equation entirely. It only depends on the average price E, the number of new units N, and the elasticity ε. Stock size still matters for how thinly that drag is spread per individual property, a bigger stock dilutes the hit per owner, but it does not matter for the total dollars at stake market wide.

## The Break-Even Condition

Total value created by the new builds, the y side, is N multiplied by the average new build value, written as y-bar:

Total value created = N multiplied by y-bar

LaTeX:
\text{Value}_{total} = N \cdot \bar{y}

Setting total drag equal to total value created, the point where the scheme would theoretically break:

E multiplied by N divided by epsilon = N multiplied by y-bar

LaTeX:
\dfrac{E \cdot N}{\varepsilon} = N \cdot \bar{y}

N cancels on both sides. What remains is the actual break-even condition:

E divided by epsilon = y-bar

LaTeX:
\dfrac{E}{\varepsilon} = \bar{y}

This says the break-even point does not depend on N at all once you simplify it fully. The question of how fast construction would need to be partly dissolves, because the N you build does not change whether the system is balanced or not, it only changes how large the swings are while staying balanced or not. What actually decides whether the scheme breaks is whether the average price of new construction, y-bar, falls to or below the existing average price divided by the elasticity coefficient, E over epsilon.

In a highly inelastic market, where epsilon is well below 1, E divided by epsilon is larger than E itself. That means new builds would need to sell for more than the existing average for the scheme to break, which is the opposite of what an oversupply glut actually looks like. Gluts clear inventory by pricing new stock at or below the existing average, not above it.

In a highly elastic market, where epsilon is above 1, E divided by epsilon drops below E, meaning the bar for y-bar to clear gets easier. New builds would not need to be unusually expensive, just not severely discounted, for the scheme to break in that market.

## Sydney, With Real Numbers

🌐 Greater Sydney existing dwelling stock, 2021 Census: 2,079,287 dwellings. Source: https://profile.id.com.au/australia/population?WebID=260

🌐 NSW mean dwelling price, September quarter 2025: $1,295,900. Source: https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/total-value-dwellings/latest-release/

This is a state-level figure rather than Sydney-specific. ❓ Sydney proper almost certainly runs higher than this NSW-wide mean, since regional NSW pulls the average down. Treat $1,295,900 as a conservative floor for E, not a precise Sydney figure.

🌐 Sydney housing supply elasticity, houses: 0.2. Apartments: 0.8. Source: peer reviewed estimate using LGA level annual data from 1991 to 2012, published in Applied Economics, https://www.tandfonline.com/doi/full/10.1080/00036846.2017.1307936, and the underlying UNSW thesis at https://unsworks.unsw.edu.au/entities/publication/f60a308f-20f4-479a-b0dc-69bb324edaa9

🌐 A more recent 2025 paper using state level NSW data to 2019 found supply elasticity of 0.36 at the state level, but found housing supply effectively perfectly inelastic specifically in the metropolitan area, meaning epsilon approaching zero for Sydney itself under that model. Source: https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-8454.12372

Running the formula with S = 2,079,287, E = $1,295,900, N = 1,000, and epsilon = 0.2, the established Sydney house elasticity figure:

Total drag = E multiplied by N divided by epsilon
Total drag = 1,295,900 multiplied by 1,000, divided by 0.2
Total drag = 1,295,900,000 divided by 0.2
Total drag = 6,479,500,000

LaTeX:
\text{Drag}_{total} = \dfrac{E \cdot N}{\varepsilon} = \dfrac{1{,}295{,}900 \times 1{,}000}{0.2} = \dfrac{1{,}295{,}900{,}000}{0.2} = 6{,}479{,}500{,}000

Adding 1,000 new houses to Greater Sydney's existing stock, under this elasticity estimate, produces an aggregate drag of approximately 6.48 billion dollars spread across the entire existing 2.08 million property stock.

Spread per existing property, that total divided by S:

6,479,500,000 divided by 2,079,287 = approximately 3,116

LaTeX:
\dfrac{\text{Drag}_{total}}{S} = \dfrac{6{,}479{,}500{,}000}{2{,}079{,}287} \approx 3{,}116

So under this model, 1,000 new houses built in Sydney costs each existing property owner, on average, somewhere in the order of 3,116 dollars in price suppression. Across a portfolio of, say, 10 properties, that is roughly 31,160 dollars of suppressed value from that single year's 1,000-unit addition.

For the break-even condition, E divided by epsilon, using the same numbers:

E divided by epsilon = 1,295,900 divided by 0.2 = 6,479,500

LaTeX:
\dfrac{E}{\varepsilon} = \dfrac{1{,}295{,}900}{0.2} = 6{,}479{,}500

For the investment scheme to break under this elasticity, the average new house being built would need to sell for roughly 6.48 million dollars, about five times the existing NSW mean. That is not what oversupply looks like in practice, new builds sell at or near the existing average, sometimes below it during a glut, which is precisely why the scheme structurally does not break under normal construction dynamics, even at high volume.

❓ If the more recent 2025 paper's metro-level near-zero elasticity finding is used instead of the 0.2 figure, the one divided by epsilon term grows extremely large, meaning a given N produces a much larger total drag for the same N. This is the scenario where Sydney's notoriously constrained supply response would make each marginal unit of construction count for more in price suppression terms than in a more elastic market. It does not change the structural conclusion that total value created scales with N just as total drag does, so the break even condition, E divided by epsilon equals y-bar, still does not depend on N, it just shifts the bar for y-bar higher, making the scheme even harder to break, since E divided by a near zero epsilon approaches infinity, meaning no realistic y-bar could ever clear it.

## Why This Matters For The Original Claim

The original intuition was that if x ever caught up to y, fast enough construction would break the investment scheme entirely. The corrected model shows the comparison was framed at the wrong level. The proper comparison is not x against a single y, it is total drag, E multiplied by N over epsilon, against total value created, N multiplied by y-bar. Both sides scale with N, so N cancels, and the question collapses to a single fixed condition that does not depend on how fast or how much gets built. It depends only on whether new build prices fall low enough relative to the existing average, scaled by elasticity, which in any normal market, let alone an inelastic one like Sydney, is not something construction volume by itself can trigger.

The genuinely real and empirically supported part of the original intuition survives intact: more construction does suppress existing price growth, and an inelastic market like Sydney, where epsilon sits around 0.2 for houses, means each marginal new unit suppresses prices more than the same unit would in a more elastic market like, for comparison, Tokyo. That part of the model holds. What does not hold is the idea that this suppression effect could ever outrun the value being created by the construction itself, because both effects are driven by the same N and scale together.
