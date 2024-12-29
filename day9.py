from itertools import permutations

def main():
    input = open("input/day9.txt").readlines()
    cities = set()
    dists = {}
    for l in input:
        left, dist = l.rstrip().split(" = ")
        dist = int(dist)
        src, dest = left.split(" to ")
        cities.add(src)
        cities.add(dest)
        dists[(src, dest)] = dist
        dists[(dest, src)] = dist
    min_dist = None
    max_dist = None
    for perm in permutations(cities):
        total_dist = 0
        for i in range(0, len(perm) - 1):
            total_dist += dists[(perm[i], perm[i + 1])]
        if min_dist == None or total_dist < min_dist:
            min_dist = total_dist
        if max_dist == None or total_dist > max_dist:
            max_dist = total_dist
    print(min_dist)
    print(max_dist)

if __name__ == "__main__":
    main()
