import re
from math import prod

# Get all permutations of k positive integers that sum to the given positive integer
# https://stackoverflow.com/a/74454054
def perms(sum, k):
    if k < 1:
        return []
    if k == 1:
        return [(sum,)]
    if k == 2:
        return [(i,sum-i) for i in range(1, sum-k+2)]
    return [tup[:-1] + ab for tup in perms(sum, k-1) for ab in perms(tup[-1], 2)]

def main():
    input = open("input/day15.txt").readlines()
    ingredients = []
    for l in input:
        ingredients.append(list(map(lambda n: int(n), re.findall(r"-?\d+", l))))
    max_product = None
    max_with_calories = None
    for perm in perms(100, 4):
        calories = max(sum(perm[i] * ingredients[i][4] for i in range(4)), 0)
        product = prod(max(sum(perm[i] * ingredients[i][prop_index] for i in range(4)), 0) for prop_index in range(4))
        if max_product == None or product > max_product:
            max_product = product
        if calories == 500 and (max_with_calories == None or product > max_with_calories):
            max_with_calories = product
    print(max_product)
    print(max_with_calories)

if __name__ == "__main__":
    main()
