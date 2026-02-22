# METAL PRICE ANALYSIS

## Project Description:
We are going to explore predictive indicators for various metals with a focus on titanium. This would involve
using financial metrics like daily moving average (DMA), Pearson correlation coefficient, and time-shifted
data (ex. Does past 5 days of copper prices help us predict next day’s silver- is some metal’s historical price a
leading indicator for another metal?). Metal prices are also related to energy prices. We will add other pricing
data as available and relevant based on our research.

Metal prices are determined  by variable and fixed costs. The key input of metal production is energy,
for example; if we are able to follow energy prices trends such as gas, electricity or coal therefore 
we could assume that these prices will impact the final price of the metal because in order to produce
a metal, energy input is needed.

Depending on the manufacturing process of the region, some metals are produced by a form of burning coal while 
others by electrical induction which means melting with a magnetic field.

There are many other costs of production that we can use to analyze the final price of metals in the market
so this project is an exploratory tool to identify the most influential and accurate inputs.

## What is the code for?
We are turning the data into a chart easy to visualize, in this case we are using
candlestick charts. The daily data is transformed into a visualized structure.

We use daily commodity data for copper, gold, silver and oil.
For titanium we use monthly prices because Titanium is not traded as a non tangible asset
in contrast with the rest. 
The trade if titanium is done in the traditional supply chain physical market. We 
load the datasets into the program.

The code uses some functions such as general index list for calculating the moving averages prices and the fit polynomials to analyze commodities and metals price trends.

Polynomials are used to describe the trends of commodities and the metal markets, as an example,  a linear polynomial  offers us the general trajectory, a quadratic and cubic polynomial will show us the ups and downs giving a better resolution therefore the understanding of price behaviours. We found that the use of the cubic polynomial its a better approach in this context.

Even thought the resolution of the cubic polynomial is better, it is valuable to zoom out to see the trends and to reduce the noise so this is what linear and quadratic polynomials do.

The code is also using quadratic regressions for linear, quadratic and cubic curves that represent the estimations of the coefficients that shape the curves. A regression is simply the process to assign coefficients to the curves or to predict the curves. In the context of this project, it means to predict commodity prices with regression, a coefficient is simply a parameter that indicates the shape of the curve, for example in a linear equation given by y = mx + b    m is the coefficient that controls the slope of the curve, similar case for a quadratic and cubic curve. With regression we can create the logic of "given today, give me tomorrow".

With regression we can create the logic of "given today, give me tomorrow". We are using Torch package for neural networks.

**The final flow overview is as follow:** 

- Raw data
- Arrangement of data
- Calculation of moving averages
- Calculation of polynomial equations with regression (linear, quadratic, cubic)
- Use of neural networks
- Next period predictions








## Team Members:
Edward Wei,
Adrian Ambriz


