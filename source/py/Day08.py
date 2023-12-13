import re
import math

def solve(path, second_part = False):
    parsed = open(path).readlines()
    ints = parsed[0].strip()
    routes = {x[0]: x[1:] for x in [*map(lambda x: re.findall("\w+", x), parsed[2:])]}
    nodes = [r for r in list(routes.keys()) if r[-1]=="A"] if second_part else ["AAA"]
    start_nodes = nodes.copy()
    z_steps = []
    steps = 0
    while len([n for n in nodes if n[-1]!="Z"]) > 0:
        for d in ints:
            steps += 1
            for i in range(len(nodes)):
                if d == 'R':
                    nodes[i] = routes[nodes[i]][1]
                elif d == 'L':
                    nodes[i] = routes[nodes[i]][0]
                if nodes[i][-1] == 'Z':
                    z_steps.append(steps)
        if second_part and len(z_steps) >= len(start_nodes):
            lcm = math.lcm(*z_steps)
            return lcm
    return steps
    
print("Part 1 solution: ", solve("data/input08.txt", False))
print("Part 2 solution: ", solve("data/input08.txt", True))