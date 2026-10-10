"""
Verify the four basic counting rules from combinatorics with code.

For a set of n objects and samples of size k, this script enumerates every
possible outcome with itertools and checks that the count matches the
closed-form formula from the math module:

    ordered,   with replacement     -> product        n^k
    ordered,   without replacement  -> permutations   n! / (n-k)!
    unordered, without replacement  -> combinations   C(n, k)
    unordered, with replacement     -> combinations   C(n+k-1, k)

Each check is an assert, so changing OBJECTS or K immediately shows whether
formula and enumeration still agree.

Based on the sampling table in Blitzstein & Hwang, Introduction to
Probability (ch. 1).
"""

import itertools
import math

OBJECTS = "ABCDE"
K = 3

# FORMULAS
formula_permutations = math.perm(len(OBJECTS), K)
formula_product = len(OBJECTS) ** K
formula_combination = math.comb(len(OBJECTS), K)
formula_combination_with_repetition = math.comb(len(OBJECTS) + K - 1, K)

# Itertools
iter_comb = itertools.combinations(OBJECTS, K)
iter_comb_with_repeat = itertools.combinations_with_replacement(OBJECTS, K)
iter_product = itertools.product(OBJECTS, repeat=K)
iter_perm = itertools.permutations(OBJECTS, K)

# functions:
def count_possibilities(tool):
    """ Function that calculates all the possibilities and counts the number of them
    
    In: an iterator tool function
    returns a integer (count of the possibilities)
    """
    counter = 0
    for combo in tool:
        counter += 1
    return counter

def assert_itertools_equals_formula(iter_tool, category_name, formula_possibility):
    """ Function that uses assert to check that the itertools give the same result as the formula written with math.

    in: the specific itertool function, the name for the type of sampling category (products e.g.), and the possibilities that was written with the math module.
       e.g.: assert_itertools_equals_formula(iter_comb, "combinations", formula_combination)
    returns: nothing if it works and an AssertionError if it goes wrong with a message written in an f-string
    """

    iter_result = count_possibilities(iter_tool)
    assert iter_result == formula_possibility, f"{category_name}: telling {iter_result}, formule {formula_possibility}"



# no order + no repeats, combinations can be any order.
assert_itertools_equals_formula(iter_comb, "combinations", formula_combination + 1)

# combinations can be any order, so no order + repeat (bc replacement)
assert_itertools_equals_formula(iter_comb_with_repeat, "combinations with repetition", formula_combination_with_repetition) # 35

# product is repeat + order
assert_itertools_equals_formula(iter_product, "product", formula_product) # 125

#no repeat + order
assert_itertools_equals_formula(iter_perm, "permutation", formula_permutations) # 60

print("Everything is correct!")
