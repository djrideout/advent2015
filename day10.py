from itertools import groupby

def main():
    seq = open("input/day10.txt").read().rstrip()
    for i in range(0, 50):
        if i == 40:
            print(len(seq))
        next = ""
        for k, g in groupby(seq):
            next += str(len(list(g))) + k
        seq = next
    print(len(seq))

if __name__ == "__main__":
    main()
