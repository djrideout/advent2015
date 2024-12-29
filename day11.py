def password_to_int(string):
    out = 0
    for i, c in enumerate(string[::-1]):
        out += (ord(c) - 97) * pow(26, i)
    return out

def test_and_output_password(num):
    out = ""
    digits = []
    no_iol = True
    has_increase = False
    pair_indices = []
    i = 0
    while num > 0:
        digit = num % 26
        digits.insert(0, int(digit))
        no_iol &= digit != 9 and digit != 15 and digit != 12
        if len(digits) >= 3 and digits[1] == digits[0] + 1 and digits[2] == digits[0] + 2:
            has_increase = True
        if len(digits) >= 2 and digits[1] == digits[0] and (len(pair_indices) == 0 or i - pair_indices[0] > 1):
            pair_indices.insert(0, i)
        out += chr(int(digit) + 97)
        num = (num - digit) / 26
        i += 1
    return (out[::-1], no_iol and has_increase and len(pair_indices) > 1)

def main():
    input = open("input/day11.txt").read().rstrip()
    remaining = 2
    num = password_to_int(input) + 1
    while remaining > 0:
        string, is_valid = test_and_output_password(num)
        if is_valid:
            remaining -= 1
            print(string)
        num += 1

if __name__ == "__main__":
    main()
