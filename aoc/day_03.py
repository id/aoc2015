def move(x, y, c):
    if (c == '>'):
        return x+1, y
    if (c == '<'):
        return x-1, y
    if (c == '^'):
        return x, y+1
    if (c == 'v'):
        return x, y-1

def part1(data):
    s = set([(0,0)]);
    x,y = 0,0;
    count = 1;
    for c in data:
        x,y = move(x, y, c);
        if (not (x,y) in s):
            count += 1;
            s.add((x,y));
    return count;

def move_and_record(x, y, c, s, count):
    x,y = move(x, y, c);
    if (not (x,y) in s):
        count += 1;
        s.add((x,y));
    return x, y, count;

def part2(data):
    s = set([(0,0)]);
    x_santa, y_santa = 0,0;
    x_robot, y_robot = 0,0;
    count = 1;
    for i in range(0, len(data)-1, 2):
        x_santa, y_santa, count = move_and_record(x_santa, y_santa, data[i], s, count);
        x_robot, y_robot, count = move_and_record(x_robot, y_robot, data[i+1], s, count);
    return count;

def main():
    with open('data/03.txt') as f:
        data = f.read();
    print(part1(data));
    print(part2(data));

if __name__ == "__main__":
    main()
