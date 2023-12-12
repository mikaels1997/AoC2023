def solve(path, second_part = False):
    parsed = [x.split("\n") for x in open(path).read().split("\n\n")]
    nums = [(int(x)) for x in parsed[0][0].split(" ")[1:]]
    if not second_part:
        nums = set([(x, x) for x in nums])
    if second_part:
        nums = set([(nums[c], nums[c]+nums[c+1]) for c in range(0, len(nums)//2+1, 2)])
    mappings = [[*map(str.split, x[1:])] for x in parsed[1:]]
    for mapping in mappings:
        in_spans = []
        for submap in mapping:
            dest = int(submap[0])
            submap = [*map(int, submap)]
            submap = [submap[1], submap[1]+submap[2]-1]
            out_spans = []
            for num in nums:
                spans = join_spans(set([num[:]]), submap, dest)
                in_spans += spans[1]
                out_spans += spans[0]
            nums = out_spans
        nums = set(nums) | set(in_spans)
    return min(min(nums))

def join_spans(seeds, source, dest_base):
    outs = []
    ins = []
    for seed_span in seeds:
        intrs = [max(source[0], seed_span[0]), min(source[1], seed_span[1])]
        offset = (intrs[0]-source[0]+dest_base, intrs[1]-source[0]+dest_base)
        if offset[0] <= offset[1]:
            ins.append(offset)
        if seed_span[0] < source[0]:
            outs.append((seed_span[0], min(seed_span[1], source[0])))
        if seed_span[1] > source[1]:
            outs.append((max(seed_span[0], source[1]), seed_span[1]))
    return outs, ins
    
print("Part 1 solution: ", solve("data/input05.txt", False))
print("Part 2 solution: ", solve("data/input05.txt", True))