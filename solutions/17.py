import re

test_input = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

with open('inputs/17.txt', 'r') as f:
    lines = f.read()

# lines = test_input

initial_regs = { a: int(b) for a, b in re.findall(r'([A-C]): (\d+)', lines) }
pgm = lines.split(': ')[-1].strip().split(',')
pointer = 0
REGS = {}
print(REGS, pgm)
COMBO_MAP = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: "A",
    5: "B",
    6: "C",
    7: "Q"
}
def combo(t):
    v = COMBO_MAP[t]
    if type(v) == str:
        return REGS[v]
    return v

def adv(i): # OP 0
    REGS["A"] = int(REGS["A"] / 2**combo(i))
    return None, None

def bxl(i): # OP 1
    REGS["B"] = REGS["B"] ^ i
    return None, None

def bst(i): # OP 2
    REGS["B"] = combo(i) % 8
    return None, None

def jnz(i): # OP 3
    if REGS["A"] == 0:
        return None, None
    return i, None

def bxc(i): # OP 4
    REGS["B"] = REGS["B"] ^ REGS["C"]
    return None, None

def out(i): # OP 5
    return None, combo(i) % 8

def bdv(i): # OP 6
    REGS["B"] = int(REGS["A"] / 2**combo(i))
    return None, None

def cdv(i): # OP 7
    REGS["C"] = int(REGS["A"] / 2**combo(i))
    return None, None


OP_CODES = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}
_pgm = ','.join(pgm)
print('---- DAY 17 PART 1 ----')

def run(p, **overrides):
    global REGS
    REGS = {**initial_regs, **overrides}
    p = [int(t) for t in p]
    pointer = 0
    outputs = []
    areg = REGS['A']
    while pointer < len(p) - 1:
        op = p[pointer]
        inp = p[pointer + 1]

        jmp, o = OP_CODES[op](inp)
        if REGS['A'] != areg:
            areg = REGS['A']
        if jmp is not None:
            pointer = jmp
        else:
            pointer += 2
        if o is not None:
            outputs.append(f'{o}')
    
    return outputs

print(','.join(run(pgm)))

print('---- DAY 17 PART 2 ----')

areps = ['']
tried = []
finals = set()
for _ in range(len(pgm)):
    newareps = set()
    while len(areps):
        a_rep = areps.pop()
        for i in range(64):
            v = format(i, '03b')
            o = ','.join(run(pgm, A=int(f'0b{a_rep}{v}', 2)))
            if _pgm == o:
                finals.add(int(f'0b{a_rep}{v}', 2))
            if _pgm.endswith(o):
                newareps.add(f'{a_rep}{v}')
            
    areps = list(newareps)
    tried.extend(areps)

print(f'{min(finals):_}')

# STEPS
# 1. Set B to last 3 bits of A
# 2. Set B to B ^ 011
# 3. Set C to A // 2 ** B
# 4. Set B to B ^ C
# 5. Drop last 3 bits of A
# 6. Set B to B ^ 5
# 7. Log last 3 bits of B
# 8. Repeat