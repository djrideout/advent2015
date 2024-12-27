import hashlib

def get_md5_suffix(input, zeroes):
    count = 1
    while True:
        md5 = hashlib.md5(f"{input}{count}".encode("utf-8")).hexdigest()
        if md5.startswith("0" * zeroes):
            return count
        count += 1

def main():
    input = open("input/day4.txt").read().rstrip()
    print(get_md5_suffix(input, 5))
    print(get_md5_suffix(input, 6))

if __name__ == "__main__":
    main()
