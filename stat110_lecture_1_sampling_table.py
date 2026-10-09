#"Ik heb een klein Python-script geschreven dat de vier basisregels uit de combinatoriek controleert. 
# Het somt met itertools alle uitkomsten letterlijk op en vergelijkt dat aantal met de wiskundige formule. 
# Met assert-checks test het script zichzelf: verander ik de input, dan zie ik direct of formule en telling nog overeenkomen.
# Zo verifieer ik mijn begrip van de theorie met code, in plaats van alleen te vertrouwen op wat ik heb gelezen."


import itertools
import math

OBJECTEN = "ABCDE"
K = 3

# FORMULAS
formula_permutations = math.perm(len(OBJECTEN), K)
formula_product = len(OBJECTEN) ** K
formula_combination = math.comb(len(OBJECTEN), K)
formula_combination_with_repetition = math.comb(len(OBJECTEN) + K - 1, K)

# Itertools
iter_comb = itertools.combinations(OBJECTEN, K)
iter_comb_with_repeat = itertools.combinations_with_replacement(OBJECTEN, K)
iter_product = itertools.product(OBJECTEN, repeat=K)
iter_perm = itertools.permutations(OBJECTEN, K)

def count_possibilities(tool):
    """ function that gives calculates all the possibilities and counts the number of them
    
    tool: een itertool function (iterator)
    returns een counter met de hoeveelheid mogelijkheden
    """
    counter = 0
    for combo in tool:
        counter += 1
    return counter

# no order + no repeats, combinations can be any order.
count_combination = count_possibilities(iter_comb)
assert count_combination == formula_combination, f"combinations: telling {count_combination}, formule {formula_combination}"

# combinations can be any order, so no order + repeat (bc replacement)
count_comb_with_repeat = count_possibilities(iter_comb_with_repeat)
assert count_comb_with_repeat == formula_combination_with_repetition, f"combinations with repetition: telling {count_comb_with_repeat}, formule {formula_combination_with_repetition}"

# product is repeat + order
count_product = count_possibilities(iter_product)
assert count_product == formula_product, f"products: telling {count_product}, formule {formula_product}"

#no repeat + order
count_perm = count_possibilities(iter_perm)
assert count_perm == formula_permutations, f"permutations: telling {count_perm}, formule {formula_permutations}"

print("Everything is correct!")
