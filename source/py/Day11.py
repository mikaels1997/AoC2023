import numpy as np

def solve(path, second_part = False):
    gal = np.array([0,0])
    space = open(path).readlines()
    cols = {c: 0 for c in range(len(space[0].strip()))}
    empty_r = []
    for r in range(len(space)):
        if space[r].strip().replace('.', '') == '':
            empty_r.append(r)
        for c in range(len(cols)):
            if space[r][c] == "#":
                gal = np.vstack([gal, [r, c]])
            elif space[r][c] == ".":
                cols[c] += 1
    empty_r = np.array(empty_r)
    empty_c = np.array([x for x in cols if cols[x]==len(space)])
    result = 0
    h = lambda t, c: 1e6*sum(c<t)-sum(c<t) if second_part else sum(c<t)
    gal = np.array([[g[0] + h(g[0], empty_r), g[1] + h(g[1], empty_c)] for g in gal[1:]])
    result = sum([sum(abs(gal[:,1] - g[1]) + abs(gal[:,0] - g[0])) for g in gal])
    return int(result/2)

print("Part 1 solution: ", solve("data/input11.txt", False))
print("Part 2 solution: ", solve("data/input11.txt", True))