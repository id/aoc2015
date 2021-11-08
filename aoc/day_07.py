import re
import sys
import collections

regex = re.compile(r'(([a-z]+|\d+)\s)?(NOT|RSHIFT|LSHIFT|AND|OR)?\s?([a-z]+|\d+) -> ([a-z]+)')

ops = {'AND': lambda x, y: x & y,
       'OR': lambda x, y: x | y,
       'NOT': lambda x: ~x & 65535,
       'LSHIFT': lambda x, y: x << y,
       'RSHIFT': lambda x, y: x >> y,
       None: None}

class Vertex:
    def __init__(self, name = None, op = None, signal = None, arg = None):
        self.name = name
        self.op = ops[op]
        self.op_s = op
        self.signal = signal
        self.arg = arg
        self.in_wires = []
        self.out_wires = []

    def __repr__(self):
        attributes = []
        if (self.name): attributes.append(f"{self.name}")
        if (self.op): attributes.append(f"op={self.op_s}")
        if (self.signal is not None): attributes.append(f"signal={self.signal}")
        if (self.arg): attributes.append(f"arg={self.arg}")
        if (self.in_wires):
            in_s = ','.join([w.to_str() for w in self.in_wires])
            attributes.append(f"in={in_s}")
        if (self.out_wires):
            out_s = ','.join([w.to_str() for w in self.out_wires])
            attributes.append(f"out={out_s}")
        return f"<{', '.join(attributes)}>"

    def to_str(self):
        if (self.name):
            return self.name
        return self.op_s;

    def add_input(self, v):
        self.in_wires.append(v)

    def add_output(self, v):
        self.out_wires.append(v)

    def calc_signal(self):
        if (not self.op and self.arg is not None):
            self.signal = self.arg
            return True
        elif (not self.op and len(self.in_wires) == 1 and self.in_wires[0].signal is not None):
            self.signal = self.in_wires[0].signal
            return True
        elif (self.op and len(self.in_wires) == 1
              and self.in_wires[0].signal is not None
              and not self.arg is not None):
            self.signal = self.op(self.in_wires[0].signal)
            return True
        elif (self.op and len(self.in_wires) == 1
              and self.in_wires[0].signal is not None
              and self.arg is not None):
            self.signal = self.op(self.in_wires[0].signal, self.arg)
            return True
        elif (self.op and len(self.in_wires) == 2
              and self.in_wires[0].signal is not None
              and self.in_wires[1].signal is not None):
            self.signal = self.op(self.in_wires[0].signal, self.in_wires[1].signal)
            return True
        return False

def parse_data(data):
    g = {}
    known_signals = []

    for line in data:
        m = regex.match(line)
        try:
            (_, left, op, right, out) = m.groups()
        except:
            print(line)
        if (out not in g):
            g[out] = Vertex(name=out)
        if (left == None and op == None and right.isdigit()):
            g[out].signal = int(right)
            known_signals.append(g[out])
        if (op):
            v_op = Vertex(op=op)
            v_op.add_output(g[out])
            g[out].add_input(v_op)
            if (op == 'NOT'):
                if (right not in g):
                    g[right] = Vertex(name=right)
                g[right].add_output(v_op)
                v_op.add_input(g[right])
            elif (op == 'LSHIFT' or op == 'RSHIFT'):
                v_op.arg = int(right)
                if (left not in g):
                    g[left] = Vertex(name=left)
                g[left].add_output(v_op)
                v_op.add_input(g[left])
            elif (op == 'AND' or op == 'OR'):
                if (left.isdigit()):
                    v_op.arg = int(left)
                else:
                    if (left not in g):
                        g[left] = Vertex(name=left)
                    g[left].add_output(v_op)
                    v_op.add_input(g[left])

                if (right not in g):
                    g[right] = Vertex(name=right)
                g[right].add_output(v_op)
                v_op.add_input(g[right])
        else:
            if (right not in g):
                g[right] = Vertex(name=right)
            g[right].add_output(g[out])
            g[out].add_input(g[right])

    return g, known_signals

def solve(g, known_signals):
    q = collections.deque(known_signals)
    while (len(q) > 0):
        v = q.popleft()
        for w in v.out_wires:
            if (w.signal is None and w.calc_signal()):
                q.append(w)

def part1(data, target):
    g, known_signals = parse_data(data)
    solve(g, known_signals)
    return g.get(target).signal

def part2(data, target):
    b_signal = part1(data, target)
    g, known_signals = parse_data(data)
    g['b'].signal = b_signal
    solve(g, known_signals)
    return g.get(target).signal

def main():
    data = [];
    with open('data/07.txt') as f:
        data = [l.strip() for l in f.readlines()]
    print(part1(data, 'a'))
    print(part2(data, 'a'))


if __name__ == "__main__":
    main()
