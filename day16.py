import re

match = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}
greater_than = {"cats", "trees"}
less_than = {"pomeranians", "goldfish"}

def range_match(key, val):
    return match[key] < int(val) if key in greater_than else \
        match[key] > int(val) if key in less_than else \
        match[key] == int(val)

def main():
    input = open("input/day16.txt").readlines()
    regex = r"Sue (\d+): (.+): (\d+), (.+): (\d+), (.+): (\d+)"
    p1_index = None
    p2_index = None
    for l in input:
        index, key_0, count_0, key_1, count_1, key_2, count_2 = re.findall(regex, l)[0]
        if match[key_0] == int(count_0) and match[key_1] == int(count_1) and match[key_2] == int(count_2):
            p1_index = index
        if range_match(key_0, count_0) and range_match(key_1, count_1) and range_match(key_2, count_2):
            p2_index = index
    print(p1_index)
    print(p2_index)

if __name__ == "__main__":
    main()
