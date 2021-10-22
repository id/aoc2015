floorMap = {'(': 1, ')': -1};

def part1(data):
    res = 0;
    for c in data:
        res += floorMap.get(c);
    return res;

def part2(data):
    res = 0;
    i = 1;
    for c in data:
        res += floorMap.get(c);
        if (res == -1):
            return i;
        i += 1
    return -1;

def main():
    with open('data/01.txt') as f:
        data = f.read();
    print(part1(data));
    print(part2(data));

main();
