from collections import defaultdict

def main():
    input = open("input/day3.txt").read()
    part1_houses = defaultdict(lambda: 0)
    part2_houses = defaultdict(lambda: 0)
    part1_houses[(0, 0)] = 1
    part2_houses[(0, 0)] = 2
    x = [0, 0, 0]
    y = [0, 0, 0]
    for i, c in enumerate(input):
        match c:
            case "<": x[2] -= 1; x[i % 2] -= 1
            case "^": y[2] -= 1; y[i % 2] -= 1
            case "v": y[2] += 1; y[i % 2] += 1
            case ">": x[2] += 1; x[i % 2] += 1
        part1_houses[(x[2], y[2])] += 1
        part2_houses[(x[i % 2], y[i % 2])] += 1
    print(len(part1_houses))
    print(len(part2_houses))

if __name__ == "__main__":
    main()
