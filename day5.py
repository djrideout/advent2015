import re

def part1(input):
    count = 0
    for l in input:
        vowels = len(re.findall(r"[aeiou]", l)) >= 3
        repeats = len(re.findall(r"(.)\1{1}", l)) > 0
        missing = len(re.findall(r"ab|cd|pq|xy", l)) == 0
        if vowels and repeats and missing:
            count += 1
    return count

def part2(input):
    count = 0
    for l in input:
        pair = len(re.findall(r"(?:(\w\w)(.*)\1)", l)) > 0
        single = len(re.findall(r"(?:(\w)(.)\1)", l)) > 0
        if pair and single:
            count += 1
    return count

def main():
    input = open("input/day5.txt").readlines()
    print(part1(input))
    print(part2(input))

if __name__ == "__main__":
    main()
