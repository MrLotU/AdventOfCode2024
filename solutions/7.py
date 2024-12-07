import re
from itertools import product
import operator

p1_ops = {"+": operator.add, "*": operator.mul}
p2_ops = {**p1_ops, "||": lambda x, y: int(f"{x}{y}")}

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open("inputs/7.txt", "r") as f:
    lines = f.read()

# lines = test_input
lines = lines.split("\n")

print("---- DAY 7 PART 1 ----")
p1 = 0
p2 = 0


def can_solve(ans, nums, ops):
    gaps = len(nums) - 1
    combos = product(ops.keys(), repeat=gaps)

    for c in combos:
        f = nums[0]
        for i, _ in enumerate(nums):
            if i == 0:
                continue
            f = ops[c[i - 1]](f, nums[i])
        if f == ans:
            return True


for line in lines:
    res, nums = line.split(": ")
    res = int(res)
    nums = [int(x) for x in nums.split()]

    if can_solve(res, nums, p1_ops):
        p1 += int(res)

    if can_solve(res, nums, p2_ops):
        p2 += int(res)

print(p1)
print("---- DAY 7 PART 2 ----")
print(p2)
