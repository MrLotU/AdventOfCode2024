from collections import Counter

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("inputs/1.txt", "r") as f:
    lines = f.read()

# lines = test_input
lines = lines.split("\n")
a = []
b = []
for l in lines:
    na, nb = l.split()
    na, nb = int(na), int(nb)
    a.append(int(na))
    b.append(int(nb))

print("---- DAY 1 PART 1 ----")

p1 = sum(map(lambda na, nb: abs(na - nb), sorted(a), sorted(b)))
print(p1)

print("---- DAY 1 PART 2 ----")

c = Counter(b)

p2 = 0
for na in a:
    p2 += na * c.get(na, 0)

print(p2)
