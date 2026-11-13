# Candlo research notes: how many backtested strategies survive

Methodology notes and a small reproducible example behind the research essays at https://candlohq.com/essays. Documentation only. No strategy code and no data are published here.

## What was tested

83 trading strategies in total, on my own backtests:

- 62 intraday strategies I designed and scored on MNQ sessions (rounds 3 and 4 of the series, 22 plus 40)
- 21 earlier intraday and swing tests

Data:

- Intraday: 1,254 MNQ sessions (1,041 with full context data)
- Swing: 10.6 years of QQQ daily bars, 2016-01-04 to 2026-08-21 (2,674 bars)

Rules applied to every strategy:

- Split: parameters fit on the first 60% of the data, scored on the last 40% (cut at 2024-12-05). A strategy has to work on both halves.
- Risk model: 1 ATR stop and a 1.5R target, the same for every strategy
- Costs: 0.01% round trip on the swing tests
- Score: a t-statistic per half

## Result

2 of 83 passed. Both are provisional:

- Neither came from the search. Both were rules that existed before it began (the 09:30 opening range break and a published three-down-days swing effect).
- The 62 designed intraday strategies produced 116 t-scores with mean +0.06 and standard deviation 0.96. Pure noise would give 0.00 and 1.00. None of the 116 went above +3.
- A later test of the ORB as I trade it (1.0x range stop, 1.5R target, 0.07% to 0.65% range filter) on 16.2 years of NQ 5-minute bars, 2,862 trades, came out at profit factor 0.99 after costs, permutation p 0.398. Different rules and a longer sample than the first result.
- The held-out half has been checked 62 times, so it is no longer a clean test set.
- The swing result is QQQ, not futures, and it returned +109% over a period where buy and hold returned +552%.

All figures are hypothetical backtests on historical data. Educational only, not investment advice.

## Reproduce the multiple-testing numbers

```bash
python3 examples/noise_bar.py
```

Standard library only. For n independent worthless ideas and a two-sided 5% cutoff it prints the chance that at least one lands beyond +/-1.96 by luck (67.6% for 22 tests) and the Sidak-corrected bar that holds the family-wide false-positive rate at 5% (3.04 for 22 tests, 3.22 for 40).

## Checklist

[CHECKLIST.md](CHECKLIST.md) is the seven-check list used before trusting any backtest result.

## Read the full write-ups

- https://candlohq.com/essays/83-strategies
- https://candlohq.com/essays/what-noise-looks-like
- https://candlohq.com/essays/opening-range
- https://candlohq.com/essays/the-only-hour
- https://candlohq.com/essays/three-down-days
- https://candlohq.com/essays/backtest-checklist

Text is CC BY 4.0 (see LICENSE). The script is MIT (examples/LICENSE-MIT).
