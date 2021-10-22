from functools import reduce

def surface(acc, dimensions):
    [l,w,h] = dimensions;
    surfaces = [l*w, w*h, h*l];
    return acc + reduce(lambda acc, v: acc + 2*v, surfaces, 0) + min(surfaces);

def part1(data):
    return reduce(surface, data, 0);

def ribbon(acc, dimensions):
    [l,w,h] = dimensions;
    [x,y] = sorted(dimensions)[0:2];
    return acc + x*2 + y*2 + l*w*h;

def part2(data):
    return reduce(ribbon, data, 0);

def main():
    data = [];
    with open('data/02.txt') as f:
        for line in f.readlines():
            lwh = [int(x) for x in line.split('x')];
            data.append(lwh);
    print(part1(data));
    print(part2(data));

main();
