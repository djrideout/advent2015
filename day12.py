import re
import json
from functools import reduce

def get_nums(str):
    return re.findall(r"-?\d+", str)

def sum(str_nums):
    return reduce(lambda a, b: int(a) + int(b), str_nums)

def remove_reds(obj):
    for key in list(obj):
        if isinstance(obj, dict):
            if obj[key] == "red":
                return True
            if key in obj and isinstance(obj[key], dict) and remove_reds(obj[key]):
                del obj[key]
            if key in obj and isinstance(obj[key], list):
                remove_reds(obj[key])
        elif isinstance(obj, list):
            if isinstance(key, dict) and remove_reds(key):
                obj.remove(key)
            if isinstance(key, list):
                remove_reds(key)

def main():
    input = open("input/day12.txt").read().rstrip()
    print(sum(get_nums(input)))
    obj = json.loads(input)
    remove_reds(obj)
    print(sum(get_nums(json.dumps(obj))))

if __name__ == "__main__":
    main()
