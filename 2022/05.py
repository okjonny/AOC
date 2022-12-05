import re

with open('./input5.txt', 'r') as f:
    lines = [line.strip() for line in f]
res = 0

stacks = {}
for i in range(1, 10):
    stacks[i] = []

stacks[1].append('B')
stacks[1].append('W')
stacks[1].append('N')

stacks[2].append('L')
stacks[2].append('Z')
stacks[2].append('S')
stacks[2].append('P')
stacks[2].append('T')
stacks[2].append('D')
stacks[2].append('M')
stacks[2].append('B')

stacks[3].append('Q')
stacks[3].append('H')
stacks[3].append('Z')
stacks[3].append('W')
stacks[3].append('R')

stacks[4].append('W')
stacks[4].append('D')
stacks[4].append('V')
stacks[4].append('J')
stacks[4].append('Z')
stacks[4].append('R')


stacks[5].append('S')
stacks[5].append('H')
stacks[5].append('M')
stacks[5].append('B')

stacks[6].append('L')
stacks[6].append('G')
stacks[6].append('N')
stacks[6].append('J')
stacks[6].append('H')
stacks[6].append('V')
stacks[6].append('P')
stacks[6].append('B')

stacks[7].append('J')
stacks[7].append('Q')
stacks[7].append('Z')
stacks[7].append('F')
stacks[7].append('H')
stacks[7].append('D')
stacks[7].append('L')
stacks[7].append('S')


stacks[8].append('W')
stacks[8].append('S')
stacks[8].append('F')
stacks[8].append('J')
stacks[8].append('G')
stacks[8].append('Q')
stacks[8].append('B')


stacks[9].append('Z')
stacks[9].append('W')
stacks[9].append('M')
stacks[9].append('S')
stacks[9].append('C')
stacks[9].append('D')
stacks[9].append('J')


for val in lines:
    if not val or "move" not in val:
        continue
    nums = re.findall(r'\d+', val)
    removeFromStack = []
    #print(move, from_, to)
    move, from_, to = int(nums[0]), int(nums[1]), int(nums[2])
    # for i in range(move):
    #    removeFromStack.append(stacks[from_].pop())
    removeFromStack = stacks[from_][-move:]
    # print(removeFromStack)
    del stacks[from_][-move:]
    # print(removeFromStack)
    for val in removeFromStack:
        stacks[to].append(val)
    # print(stacks[to])
    # print(nums)
#    for char in val:
#        print(char)
#        if char.isdigit():
#            count += 1
#            if count == 1:
#                move = int(char)
#            elif count == 2:
#                from_ = int(char)
#            elif count == 3:
#                to = int(char)
#                removeFromStack = []
#                #print(move, from_, to)
#                for i in range(move):
#                    removeFromStack.append(stacks[from_].pop())
#                # print(removeFromStack)
#                for val in removeFromStack:
#                    stacks[to].append(val)
res = []
for k, v in stacks.items():
    res.append(v.pop())
print(res)
