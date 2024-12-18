import re
import sympy

test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

with open("inputs/13.txt", "r") as f:
    lines = f.read()

# lines = test_input
sections = lines.split("\n\n")


def solve(ax, ay, bx, by, px, py):
    for a in range(100):
        for b in range(100):
            if ax * a + bx * b == px and ay * a + by * b == py:
                return a * 3 + b


def solvetwo(ax, ay, bx, by, px, py):
    px = px + 10000000000000
    py = py + 10000000000000
    A = sympy.Symbol("A")
    B = sympy.Symbol("B")

    res = sympy.solve(
        [sympy.Eq(ax * A + bx * B, px), sympy.Eq(ay * A + by * B, py)], A, B
    )
    a, b = int(res[A]), int(res[B])
    if ax * a + bx * b == px and ay * a + by * b == py:
        return int(a * 3 + b)


print("---- DAY 13 PART 1 ----")
val = 0
val2 = 0

for sec in sections:
    args = [
        int(t)
        for t in re.findall(
            r"X\+(\d+), Y\+(\d+)\s.+X\+(\d+), Y\+(\d+)\s.+X=(\d+), Y=(\d+)", sec, re.M
        )[0]
    ]
    x = solve(*args)
    p2 = solvetwo(*args)
    if x is not None:
        val += x
    if p2 is not None:
        val2 += p2

print(val)
print("---- DAY 13 PART 2 ----")
print(val2)
