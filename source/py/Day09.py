import numpy as np

def solve(path, second_part = False):
    hs = [np.array([*map(int, s.split())]) for s in open(path)]
    result = sum([diff(h, 0, second_part) for h in hs])
    return result
    
def diff(mat, result, second_part):
    if any(mat) == 0:
        return 0
    d = diff(mat[1:] - mat[:-1], result, second_part)
    return mat[0] - d if second_part else mat[-1] + d

print("Part 1 solution: ", solve("data/input09.txt", False))
print("Part 2 solution: ", solve("data/input09.txt", True))
