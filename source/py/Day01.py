import re

num_dict = {"one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def solve(path, second_part=False):
    result = 0
    with open(path) as f:
        for line in f.readlines():
            if not second_part:
                nums = re.sub('\D', '', line)
                result += int(nums[0] + nums[-1])
            else:
                nums = re.findall(r"(?=("+'|'.join(num_dict.keys())+'|[\d]'+r"))", line)
                first_num = nums[0] if nums[0].isnumeric() else num_dict[nums[0]]
                last_num = nums[-1] if nums[-1].isnumeric() else num_dict[nums[-1]]
                result += int(first_num + last_num)
    return result

print("Part 1 solution: ", solve("data/input01.txt"))
print("Part 2 solution: ", solve("data/input01.txt", True))