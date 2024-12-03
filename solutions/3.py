import re

# test_input = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
test_input = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
with open('inputs/3.txt', 'r') as f:
    lines = f.read()

# lines = test_input
# lines = lines.split('\n')

print('---- DAY 3 PART 1 ----')
def get_valids(s):
    return re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', s)

print(sum([int(a) * int(b) for a,b in get_valids(lines)]))

print('---- DAY 3 PART 2 ----')

do = True
left = lines

ans = 0

while len(left) > 0:
    m = "don't()" if do else 'do()'
    try:
        idx = left.index(m)
    except:
        idx = -1
    if do:
        ans += sum([int(a) * int(b) for a,b in get_valids(left[:idx])])
    if idx == -1:
        break
    left = left[idx + 1:]
    do = not do
    
print(ans)