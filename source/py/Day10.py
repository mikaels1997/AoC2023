mapping = {"|": "1001", "-": "0110", "L": "1100",
    "J": "1010", "7": "0011", "F": "0101", "S": "1111"
} # 0 north, 1 east, 2 south, 3 west. Reversing the bit -> changes from out- to incoming
adj_mat = [(-1, 0), (0, 1), (0, -1), (1, 0)]
dirs =  [0b1000, 0b0100, 0b0010, 0b0001]

def solve(path):
    parsed = [[*l.strip()] for l in open(path).readlines()]
    coords = {(y, x): parsed[y][x] for y in range(len(parsed)) 
              for x in range(len(parsed[0]))}
    start = [i for i in coords if coords[i]=="S"][0]
    max_dist, visited = bfs(coords, start)
    return max_dist, inside_loop(coords, visited)

def bfs(graph, node):
    q = [[node, 0]]
    visited = [node]
    size = [-1, max(list(graph.keys()))[0]+1, max(list(graph.keys()))[1]+1]
    max_dist = 0
    while len(q) > 0:
        v, dist = q.pop(0)
        max_dist = max(max_dist, dist)
        for i, a in enumerate(adj_mat):
            w = (v[0]+a[0], v[1]+a[1])
            p = graph[w] if w[0] not in size[:-1] and w[1] not in size[::2] else "."
            if p != "." and w not in visited:
                src = int(mapping[graph[v]], 2)
                trg = int(mapping[graph[w]][::-1], 2) # Reverse bit
                if src & trg & dirs[i] == 0:
                    continue # Bitwise AND to check validity
                visited.append(w)
                q.append([w, dist+1])    
    return max_dist, visited

def inside_loop(tiles, loop):
    outside = True
    count, side = 0, 0 # north: 1, south: -1, middle: 0
    intercepts = ["JL", "F7", "S|"] # Remove "S" from this list if the solution is not right
    for tile in tiles:
        if side == 0:
            if tiles[tile] in intercepts[0]:
                side = -1
            elif tiles[tile] in intercepts[1]:
                side = 1
        if tile in loop:
            if side == 1 and tiles[tile] in intercepts[0]:
                outside = not outside
            elif side == -1 and tiles[tile] in intercepts[1]:
                outside = not outside
            elif tiles[tile] in intercepts[2]:
                side = 0
                outside = not outside
        elif not outside:
            count += 1
    return count

print("Solutions: ", solve("data/input10.txt"))
