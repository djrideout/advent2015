import re

def main():
    input = open("input/day1.txt").read()
    print(len(re.findall(r"\(", input)) - len(re.findall(r"\)", input)))
    count = 0
    for i, c in enumerate(input):
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
        if count == -1:
            print(i + 1)
            break

if __name__ == "__main__":
    main()
