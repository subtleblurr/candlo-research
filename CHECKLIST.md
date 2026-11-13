# Backtest checklist: seven checks before you trust a result

Every check below comes from something I got wrong or nearly got wrong in my own
testing. The numbers are from the other essays in this series, which have the full
data. Run these before you believe any backtest, yours or someone else's.

---

## 1. Count the denominator

How many strategies did you try before this one? Include the ones you dropped after
ten minutes. I tested 83 and 2 survived. A backtest without the number of attempts
behind it can't be interpreted at all.

→ Full data: [I Backtested 83 Trading Strategies](https://candlohq.com/essays/83-strategies)

## 2. Move the bar with the number of attempts

A t-score beyond ±2 is the bar most people use. It assumes you ran one test. In a
single round of 22 strategies there was about a 68% chance that at least one landed
beyond ±1.96 by luck alone. For 22 tests the bar is roughly ±3.04.

→ Full data: [How To Tell If Your Backtest Is Luck](https://candlohq.com/essays/what-noise-looks-like)

## 3. Sweep your most arbitrary parameter

Take the setting you can't justify. Run it at 0.6x, 0.8x, 1.2x, 1.5x, 2x and 3x.
A cliff on either side means you fit noise. A gentle slope means you may have
something. It takes about ten minutes.

→ Full data: [Is My Opening Range Breakout Overfit?](https://candlohq.com/essays/opening-range)

## 4. Require both halves

Split your data. Fit on one part and score on the other. If a strategy fails one half
and scores well on the other, that is not half a result. Both halves or nothing.

## 5. Count how often you looked at the test half

Every look uses it up. My held-out half has now been queried 62 times, so it is no
longer a clean test. Anything that scores well on it from here has to be discounted.

## 6. Check the time of day

The same rules moved from the 09:30 open to 14:00 lost money, with the same data and
the same risk model. A result that only works in one window needs a reason you can
state without mentioning the backtest.

→ Full data: [The Same Strategy, Four Hours Later, Loses Money](https://candlohq.com/essays/the-only-hour)

## 7. Compare it to buy and hold

A strategy that survives out of sample can still lose to simply holding. The swing
setup I found returned +109% over a period where buying and holding returned +552%.
It wins on risk, not on dollars. Say which one you are claiming.

→ Full data: [I Found A Strategy That Works](https://candlohq.com/essays/three-down-days)

---

These are results on historical data and limits of my own testing. They are not
investment advice.
