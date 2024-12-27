import re
from collections import defaultdict

def main():
    input = open("input/day6.txt").readlines()
    lights = defaultdict(lambda: False)
    brightness = defaultdict(lambda: 0)
    lights_lit = 0
    total_brightness = 0
    for l in input:
        x0, y0, x1, y1 = [int(d) for d in re.findall(r"[0-9]+", l)]
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                prev_state = lights[(x, y)]
                prev_brightness = brightness[(x, y)]
                if l.startswith("turn on"):
                    lights[(x, y)] = True
                    brightness[(x, y)] += 1
                elif l.startswith("toggle"):
                    lights[(x, y)] = not lights[(x, y)]
                    brightness[(x, y)] += 2
                elif l.startswith("turn off"):
                    lights[(x, y)] = False
                    brightness[(x, y)] = max(brightness[(x, y)] - 1, 0)
                if not prev_state and lights[(x, y)]:
                    lights_lit += 1
                elif prev_state and not lights[(x, y)]:
                    lights_lit -= 1
                total_brightness += brightness[(x, y)] - prev_brightness
                
    print(lights_lit)
    print(total_brightness)

if __name__ == "__main__":
    main()
