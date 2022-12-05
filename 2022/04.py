with open('./input4.txt', 'r') as f:
    lines = [line.strip() for line in f]
res = 0
for val in lines:
    if not val:
        continue
    dash = val.split('-')
    comma = dash[1].split(',')
    r1 = dash[0]
    e1 = comma[1]
    r2 = comma[0]
    e2 = dash[2]

    s1, s2 = set(), set()
    for i in range(int(r1), int(r2) + 1):
        s1.add(i)
    for i in range(int(e1), int(e2) + 1):
        s2.add(i)
    # if s1.issubset(s2) or s2.issubset(s1):
    #    res += 1
    m = min(len(s1), len(s2))
    for val in s1:
        if val in s2:
            res += 1
            break

    #print(r1, " ", r2, " ", e1, " ", e2)
print(res)
