def solve(path, second_part = False):
    parsed = open(path).read().replace("\n", " ").split(" ")
    hs, bs = parsed[::2], parsed[1::2]
    cards = "23456789TJQKA" if not second_part else "J23456789TQKA"
    c_values = {c: i for i, c in enumerate(cards)}
    rankings = {i: [] for i in range(1, 8)}
    types = ["11", "21", "22", "31", "32", "41", "50"]
    for h in hs:
        jokers = h.count("J")
        cts = {v: 0 for v in cards}
        for c in h:
            cts[c] += 1
        if second_part:
            del cts["J"]
            cts[max(cts, key=cts.get)] += jokers
        t = ''.join(map(str, sorted(cts.values(), reverse=True)[:2]))
        rankings[types.index(t)+1].append(h)
    sorted_hands = []
    for r in rankings:
        rankings[r].sort(key=lambda v: [c_values[v[i]] for i in range(len(v))])
        sorted_hands.extend(rankings[r])
    result = sum([int(bs[hs.index(c)])*(i+1) for i, c in enumerate(sorted_hands)])
    return result
    
print("Part 1 solution: ", solve("data/input07.txt", False))
print("Part 2 solution: ", solve("data/input07.txt", True))