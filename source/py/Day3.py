import re

def solve(path, second_part = False):
    result = 0
    symbol_num_dict = {}
    with open(path) as f:
        prev_nums, prev_syms, added_num_infos = [], [], []
        for r, line in enumerate(f.readlines()):
            num_inds = [[[r, x.start(), x.end(), 0], int(x.group())] for x in re.finditer("\d+", line)] # [[[0, 0, 3], 467], [[0, 5, 8], 114]]
            symbol_inds = [[r, i] for i in range(len(line.strip())) if line[i] != "." 
                           and not line[i].isnumeric() and (not second_part or line[i] == "*")]
            for i in symbol_inds + prev_syms:
                for n in num_inds + prev_nums:
                    if n[0][1] - 1 <= i[1] <= n[0][2] and n[0] not in added_num_infos:
                        if tuple(i) not in symbol_num_dict:
                            symbol_num_dict[tuple(i)] = []
                        symbol_num_dict[tuple(i)].append(n)
                        result += n[1]
                        added_num_infos.append(n[0])
            prev_nums = num_inds
            prev_syms = symbol_inds
    if second_part:
        result = 0
        for sym in symbol_num_dict:
            if len(symbol_num_dict[sym]) == 2:
                result += symbol_num_dict[sym][0][1] * symbol_num_dict[sym][1][1]
    return result

if __name__ == "__main__":
    print("Part 1 solution: ", solve("data/input03.txt"))
    print("Part 2 solution: ", solve("data/input03.txt", True))