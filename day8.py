import json

def main():
    input = open("input/day8.txt").readlines()
    part1 = 0
    part2 = 0
    for l in input:
        line = l.rstrip()
        decoded = bytes(line, "utf-8").decode("unicode_escape")
        encoded = json.dumps(line)
        part1 += len(line) - len(decoded) + 2
        part2 += len(encoded) - len(line)
    print(part1)
    print(part2)

if __name__ == "__main__":
    main()
