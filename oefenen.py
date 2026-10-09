import itertools

def count_possibilities(tool):
    ### function that takes a function from itertools with OBJECTEN en K and puts out the amount of all possibilities
    counter = 0
    for combo in tool:
        counter += 1
    return counter

zak = itertools.permutations("ABC", 2)
print(count_possibilities(zak))
print(count_possibilities(zak))