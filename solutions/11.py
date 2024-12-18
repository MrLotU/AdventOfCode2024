import re

test_input = '''125 17'''

with open('inputs/11.txt', 'r') as f:
    line = f.read()

# line = test_input

seen = set()

def blink(stones):
    new = []
    news = 0
    for s in stones:
        if s == '0':
            new.append('1')
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            new.append(s[:mid])
            half2 = s[mid:]
            while len(half2) > 1 and half2[0] == '0':
                half2 = half2[1:]
            new.append(half2)
        else:
            i = int(s)
            new.append(f'{i * 2024}')

    for n in new:
        if n in seen:
            continue
        seen.add(n)
        # print(n)
        news += 1
        # print('New number')
    print(f"Added {news} new numbers")
    return new

print('---- DAY 11 PART 1 ----')

_s = line.split()
for i in range(25):
    _s = blink(_s)

print(len(_s))

print('---- DAY 11 PART 2 ----')

for i in range(10):
    _s = blink(_s)
    print(i)

print(len(_s))
print(len(seen))