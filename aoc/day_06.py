import operator
import numpy as np

ON = 1
TOGGLE = 2
OFF = -1

def parse_line(s):
    tokens = s.split(' ')
    if (tokens[0] == 'toggle'):
        op = TOGGLE
        del tokens[0]
    elif (tokens[0] == 'turn'):
        del tokens[0]
        if (tokens[0] == 'on'):
            op = ON
        else:
            op = OFF
        del tokens[0]
    [x1,y1] = [int(val) for val in tokens[0].split(',')]
    del tokens[0]
    del tokens[0]
    [x2,y2] = [int(val) for val in tokens[0].split(',')]
    return (op, (x1,y1), (x2,y2))

def part1(data):
    grid = [0] * 1000
    ops = [None,
           operator.__or__,
           operator.__xor__,
           operator.__and__]
    base = (1<<1000)-1
    for op,(x1,y1),(x2,y2) in data:
        # 1s where we need to flip/enable bits
        mask = ((1<<y2+1)-1) ^ ((1<<y1)-1)
        if (op == OFF):
            # flip 1s to 0s
            mask ^= base
        for i in range(x1,x2+1):
            grid[i] = ops[op](grid[i], mask)

    count = 0
    for line in grid:
        count += line.bit_count()
    return count

def part2(data):
    # can't use bits anymore
    lights = np.zeros((1000,1000), dtype=int)
    for op,(x1,y1),(x2,y2) in data:
        lights[x1:x2+1, y1:y2+1] += op
        lights[lights < 0] = 0

    return sum(sum(lights))

def main():
    data = [];
    with open('data/06.txt') as f:
        data = [parse_line(l) for l in f.readlines()]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
