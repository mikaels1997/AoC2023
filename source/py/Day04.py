import re

def solve(path, second_part = False):
    points = 0
    remaining = {cr: 1 for cr in range(len(list(open(path))))}
    for c, line in enumerate(list(open(path))):
        winning = set(re.findall("\d+", line.split('|')[0])[1:])
        candidates = set(re.findall("\d+", line.split('|')[1]))
        matches = len(winning & candidates)
        new_cards = [i for i in range(c+1, c+1+matches)]
        for cr in new_cards:
            remaining[cr] += remaining[c]
        points += 2 ** (matches-1) * int(matches != 0)
    return int(points) if not second_part else sum(remaining.values())

print("Part 1 solution: ", solve("data/input04.txt"))
print("Part 2 solution: ", solve("data/input04.txt", True))