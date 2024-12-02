import re

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("inputs/2.txt", "r") as f:
    lines = f.read()

# lines = test_input
lines = lines.split("\n")

print("---- DAY 2 PART 1 ----")


def is_safe(nums):
    in_order = sorted(nums)
    other = in_order[::-1]
    if nums != in_order and nums != other:
        return False

    for i, num in enumerate(nums[:-1]):
        diff = abs(num - nums[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


safe = 0

for line in lines:
    nums = [int(x) for x in re.findall(r"\d+", line)]
    if is_safe(nums):
        safe += 1

print(safe)

print("---- DAY 2 PART 2 ----")

safe = 0

for line in lines:
    nums = [int(x) for x in re.findall(r"\d+", line)]
    if is_safe(nums):
        safe += 1
        continue

    for idx, _ in enumerate(nums):
        if is_safe(nums[:idx] + nums[idx + 1:]):
            safe += 1
            break

print(safe)
