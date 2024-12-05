import re
from functools import cmp_to_key

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("inputs/5.txt", "r") as f:
    lines = f.read()

# lines = test_input

rules, instructions = [x.split("\n") for x in lines.split("\n\n")]
rules = [(int(a), int(b)) for a, b in [t.split("|") for t in rules]]
instructions = [[int(x) for x in t.split(",")] for t in instructions]

wrongs = []
print("---- DAY 5 PART 1 ----")
val = 0
for inst in instructions:
    passes = True
    for a, b in rules:
        if a not in inst or b not in inst:
            continue
        if inst.index(a) > inst.index(b):
            passes = False
    if passes:
        val += inst[len(inst) // 2]
    else:
        wrongs.append(inst)

print(val)

print("---- DAY 5 PART 2 ----")


def check_rules(a, b):
    for r in rules:
        if a in r and b in r:
            if a == r[0]:
                return -1
            else:
                return 1


val = 0

for wrong in wrongs:
    new = sorted(wrong, key=cmp_to_key(check_rules))
    val += new[len(new) // 2]

print(val)
