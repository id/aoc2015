import hashlib

def part1(data):
    i = 0
    while True:
        hash = hashlib.md5(f"{data}{i}".encode("utf-8")).hexdigest()
        if (hash.startswith('00000')):
            break
        i += 1
    return i

def part2(data):
    i = 0
    while True:
        hash = hashlib.md5(f"{data}{i}".encode("utf-8")).hexdigest()
        if (hash.startswith('000000')):
            break
        i += 1
    return i

def main():
    with open('data/04.txt') as f:
        data = f.read().rstrip('\n')
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
