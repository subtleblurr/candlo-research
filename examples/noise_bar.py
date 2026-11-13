"""Reproduce the multiple-testing numbers used in the Candlo research essays.

For n independent tests of worthless ideas, with a two-sided 5% cutoff on the t-score:
  - the chance that at least one lands beyond +/-1.96 by luck alone
  - the Sidak-corrected cutoff that keeps the family-wide false-positive rate at 5%

Run:  python3 examples/noise_bar.py
Standard library only.
"""
from statistics import NormalDist

ALPHA = 0.05
nd = NormalDist()
single_cut = nd.inv_cdf(1 - ALPHA / 2)  # about 1.96


def chance_at_least_one(n: int) -> float:
    return 1 - (1 - ALPHA) ** n


def sidak_cut(n: int) -> float:
    per_test_alpha = 1 - (1 - ALPHA) ** (1 / n)
    return nd.inv_cdf(1 - per_test_alpha / 2)


if __name__ == "__main__":
    print(f"single-test two-sided cutoff: +/-{single_cut:.2f}")
    print(f"{'tests':>6} {'P(at least one beyond +/-1.96)':>32} {'Sidak bar':>10}")
    for n in (1, 5, 10, 22, 40, 83):
        print(f"{n:>6} {chance_at_least_one(n):>31.1%} {sidak_cut(n):>10.2f}")
