def solve(path, second_part = False):
    limits = {"red": 12, "green": 13, "blue": 14}
    result = 0
    with open(path) as f:
        for line in f.readlines():
            game_id = int(line.split(" ")[1][:-1])
            games = line.split(':')[-1].split(';')
            invalid = False
            max_nums = {"red": 0, "green": 0, "blue": 0}
            for game in games:
                cubes = game.strip().split(',')
                for cube in cubes:
                    parsed = cube.strip().split(" ")
                    num, color = int(parsed[0]), parsed[1].strip()
                    if max_nums[color] < num:
                        max_nums[color] = num
                    if limits[color] >= num and not second_part:
                        continue
                    invalid = True
            if second_part:
                result += max_nums["red"] * max_nums["green"] * max_nums["blue"]
            if not invalid and not second_part:
                result += game_id              
    return result

print("Part 1 solution: ", solve("data/input02.txt"))
print("Part 2 solution: ", solve("data/input02.txt", True))