import math
import re
from collections import defaultdict

def distance_travelled(seconds, reindeer):
    distance = 0
    speed = int(reindeer[1])
    fly_time = int(reindeer[2])
    rest_time = int(reindeer[3])
    cycle_time = fly_time + rest_time
    full_cycles = math.floor(seconds / cycle_time)
    full_cycle_seconds = full_cycles * cycle_time
    distance += speed * fly_time * full_cycles
    seconds -= full_cycle_seconds
    if seconds < fly_time:
        distance += speed * seconds
    else:
        distance += speed * fly_time
    return distance

def main():
    total_time = 2503
    input = open("input/day14.txt").readlines()
    regex = r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)"
    reindeers = {}
    max_distance = None
    for l in input:
        reindeer = re.findall(regex, l)[0]
        reindeers[reindeer[0]] = reindeer
        distance = distance_travelled(total_time, reindeer)
        if max_distance == None or distance > max_distance:
            max_distance = distance
    points = defaultdict(lambda: 0)
    for t in range(1, total_time + 1):
        max_distance = None
        in_lead = []
        for name in reindeers:
            distance = distance_travelled(t, reindeers[name])
            if max_distance == None or distance > max_distance:
                in_lead = [name]
                max_distance = distance
            elif distance == max_distance:
                in_lead.append(name)
        for name in in_lead:
            points[name] += 1
    print(max_distance)
    print(max(list(points.values())))

if __name__ == "__main__":
    main()
