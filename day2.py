import re
import math

def main():
    input = open("input/day2.txt").readlines()
    part1 = 0
    part2 = 0
    for l in input:
        side_lens = [int(d) for d in re.findall(r"[0-9]+", l)]
        areas = [
            side_lens[0] * side_lens[1],
            side_lens[0] * side_lens[2],
            side_lens[1] * side_lens[2]
        ]
        perims = [
            2 * (side_lens[0] + side_lens[1]),
            2 * (side_lens[0] + side_lens[2]),
            2 * (side_lens[1] + side_lens[2])
        ]
        part1 += 2 * sum(areas) + min(areas)
        part2 += min(perims) + math.prod(side_lens)
    print(part1)
    print(part2)

if __name__ == "__main__":
    main()
