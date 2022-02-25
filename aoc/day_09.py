from heapq import heappush, heappop, heapify
import sys

def parse_line(line):
    tokens = line.split(' ')
    return (tokens[0], tokens[2], int(tokens[4]))

def update_heap(h, c, dist):
    for i in range(len(h)):
        if (h[i][1] == c):
            h[i][0] = dist
            heapify(h)
            return
    heappush(h, (dist, c))

def distance_from(city, cities, edges, adj):
    print(f"*** {city} ***")
    h = []
    dist_to = {}
    path = {}
    for c in cities:
        dist_to[c] = sys.maxsize
    dist_to[city] = 0
    heappush(h, (0, city))
    while (len(h) > 0):
        _, c = heappop(h)
        print(f"--> {c}")
        for start,end,dist in adj.get(c, []):
            print(f"{start} -> {end} = {dist}, dist_to({start}) = {dist_to[start]}, dist_to[{end}] = {dist_to[end]}")
            if (dist_to[start] + dist < dist_to[end]):
                dist_to[end] = dist_to[start] + dist
                path[end] = (start, end, dist)
                update_heap(h, end, dist_to[end])
                print(h)
    print(path)
    return 0#sum(path.values())

def part1(edges):
    cities = set()
    adj = {}
    for edge in edges:
        cities.add(edge[0])
        cities.add(edge[1])
        if edge[0] not in adj:
            adj[edge[0]] = [edge]
        else:
            adj[edge[0]].append(edge)
    shortest = sys.maxsize
    for city in cities:
        distance = distance_from(city, cities, edges, adj)
        if (distance < shortest):
            shortest = distance
    return shortest

def part2(edges):
    return 0

def main():
    with open('data/09.txt') as f:
        edges = [parse_line(line.strip()) for line in f.readlines()]
    print(part1(edges))
    print(part2(edges))


if __name__ == "__main__":
    main()
