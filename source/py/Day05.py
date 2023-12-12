def solve(path, second_part = False):
    parsed = [x.split("\n") for x in open(path).read().split("\n\n")]
    nums = [(int(x)) for x in parsed[0][0].split(" ")[1:]]
    if not second_part:
        nums = set([(x, x) for x in nums])
    if second_part:
        nums = set([(nums[c], nums[c]+nums[c+1]) for c in range(0, len(nums)//2+1, 2)])
    mappings = [[*map(str.split, x[1:])] for x in parsed[1:]]
    for mapping in mappings:
        ins = []
        for m in mapping:
            dest = int(m[0])
            m = [*map(int, m)]
            m = [m[1], m[1]+m[2]-1]
            outs = []
            for num in nums:
                spans = join_spans(set([num[:]]), m, dest)
                ins += spans[1]
                outs += spans[0]
            nums = outs
        nums = set(nums) | set(ins)
    return min(min(nums))

def join_spans(seeds, src, dest):
    outs = []
    ins = []
    for seed in seeds:
        intrs = [max(src[0], seed[0]), min(src[1], seed[1])]
        offset = (intrs[0]-src[0]+dest, intrs[1]-src[0]+dest)
        if offset[0] <= offset[1]:
            ins.append(offset)
        if seed[0] < src[0]:
            outs.append((seed[0], min(seed[1], src[0])))
        if seed[1] > src[1]:
            outs.append((max(seed[0], src[1]), seed[1]))
    return outs, ins
    
print("Part 1 solution: ", solve("data/input05.txt", False))
print("Part 2 solution: ", solve("data/input05.txt", True))