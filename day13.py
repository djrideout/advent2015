import re
from itertools import permutations

def max_happ(names, happs):
    max_happ = None
    for perm in permutations(names):
        total_happ = 0
        for i in range(0, len(perm)):
            name_0 = perm[i]
            name_1 = perm[0] if i == len(perm) - 1 else perm[i + 1]
            happ_0 = 0 if name_0 == "me" or name_1 == "me" else happs[(name_0, name_1)]
            happ_1 = 0 if name_0 == "me" or name_1 == "me" else happs[(name_1, name_0)]
            total_happ += happ_0 + happ_1
            if max_happ == None or total_happ > max_happ:
                max_happ = total_happ
    return max_happ

def main():
    input = open("input/day13.txt").readlines()
    regex = r"(.+) would (.+) (\d+) happiness units by sitting next to (.+)."
    names = set()
    happs = {}
    for l in input:
        name_0, change, magnitude, name_1 = re.findall(regex, l)[0]
        names.add(name_0)
        names.add(name_1)
        happs[(name_0, name_1)] = -int(magnitude) if change == "lose" else int(magnitude)
    print(max_happ(names, happs))
    names.add("me")
    print(max_happ(names, happs))

if __name__ == "__main__":
    main()
