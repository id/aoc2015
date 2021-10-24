vowels = 'aeiou'

def has_3_vowels(s):
    n_vowels = 0
    for c in s:
        if c in vowels:
            n_vowels += 1
    return n_vowels >= 3

def has_double_letter(s):
    for i in range(len(s)-1):
        if (s[i] == s[i+1]):
            return True
    return False

def has_banned_pairs(s):
    banned = ['ab', 'cd', 'pq', 'xy']
    for b in banned:
        if b in s:
            return True
    return False

def is_nice(s):
    return has_3_vowels(s) and has_double_letter(s) and not has_banned_pairs(s)

def part1(data):
    count = 0
    for s in data:
        if is_nice(s):
            count += 1
    return count

def has_pair_of_two(s):
    i = 0
    while (i < len(s)-1):
        pair = s[i:i+2]
        j = i+2
        while (j < len(s)):
            if (s[j:j+2] == pair):
                return True
            j += 1
        i += 1
    return False

def one_letter_repeats(s):
    i = 0
    while (i < len(s)-2):
        if (s[i] == s[i+2]):
            return True
        i += 1
    return False

def is_nice_v2(s):
    return has_pair_of_two(s) and one_letter_repeats(s)

def part2(data):
    count = 0
    for s in data:
        if is_nice_v2(s):
            count += 1
    return count

def main():
    data = [];
    with open('data/05.txt') as f:
        data = f.readlines()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
