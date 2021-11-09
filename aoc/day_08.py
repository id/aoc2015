def parse_line(s):
    mem_chars = 0
    i = 0
    while (i < len(s)):
        if (s[i] == '"'):
            i += 1
        elif (s[i] == '\\'):
            if (i+1 < len(s) and s[i+1] == 'x'):
                i += 4
                mem_chars += 1
            else:
                i += 2
                mem_chars += 1
        else:
            i += 1
            mem_chars += 1

    return mem_chars

def part1(data):
    code_chars = 0
    mem_chars = 0
    for line in data:
        code_chars += len(line)
        mem_chars += parse_line(line)
    return code_chars - mem_chars

def parse_line2(s):
    encoded_chars = len(s) + 4
    i = 1
    while (i < len(s)-1):
        if (s[i] == '"' or s[i] == '\\'):
            encoded_chars += 1
        i += 1

    return encoded_chars

def part2(data):
    code_chars = 0
    encoded_chars = 0
    for line in data:
        code_chars += len(line)
        encoded_chars += parse_line2(line)
    return encoded_chars - code_chars

def main():
    data = [];
    with open('data/08.txt') as f:
        data = [line.strip() for line in f.readlines()]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
