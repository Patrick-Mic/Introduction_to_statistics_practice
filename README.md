# Introduction to Statistics — Practice

Code exercises alongside *Introduction to Probability* (Blitzstein & Hwang)
and the Harvard Stat 110 lectures. The goal: check my understanding of the
theory by computing things two ways (formula vs. brute-force enumeration)
and seeing whether they agree.

## Sampling table checker

Choosing k objects from n, there are four cases depending on whether
**order matters** and whether **replacement is allowed**:

|                    | Order matters        | Order doesn't matter |
|--------------------|----------------------|----------------------|
| **With replacement**    | n^k                  | C(n+k−1, k)          |
| **Without replacement** | n! / (n−k)!          | C(n, k)              |

The script enumerates every outcome with `itertools` and asserts that the
count equals the formula. For n = 5, k = 3 that gives 125, 60, 35 and 10.

## How to run

Requires Python 3.8+ (for `math.perm` and `math.comb`). No external packages.

    python stat110_lecture_1_sampling_table.py

Prints `Everything is correct!` if all four checks pass; otherwise raises an
`AssertionError` that names the failing case and shows both numbers.

## What I learned
 - How to work according to the DRY-technique.
 - How to use assert and how it works and that it does not return anything but it raises an error when a check fails.
 - The differences between the possibilities when you do or don't consider replacement and order
