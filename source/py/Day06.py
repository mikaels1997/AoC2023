import math

'''
    The question can be directly formalized via maths since it forms the following inequality: 
        D < cT - c^2, (D,T,c ∈ Z+) where
            c: Boat waiting time. A variable.
            D: Record distance. A constant.
            T: Race time. A constant.
    The roots of the following quadratic equation needs to be found:
        -c^2 + Tc - D = 0
    The integers between (not including) the roots are the winning values.
'''
def solve(path, second_part = False):
    parsed = [*map(lambda x: str.split(x)[1:], list(open(path)))]
    parsed = [[int(''.join(p))] for p in parsed] if second_part else parsed
    result = 1
    for i in range(len(parsed[0])):
        t, d = int(parsed[0][i]), int(parsed[1][i])
        upper = math.floor(1/2 * (t + math.sqrt(t**2-4*d)) - 0.01)
        lower = math.ceil(1/2 * (t - math.sqrt(t**2-4*d)) + 0.01)
        result *= upper - lower + 1
    return result
    
print("Part 1 solution: ", solve("data/input06.txt", False))
print("Part 2 solution: ", solve("data/input06.txt", True))