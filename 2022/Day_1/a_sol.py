
f = open("./a_input.txt", 'r')
sum = 0
max_cal = float('-inf')
elves_sum = []
while True:
    try:
        line = f.readline().strip()
        sum += float(line)
    except ValueError:
        elves_sum.append(sum)
        s = sorted(elves_sum, reverse=True)
        max_cal = max(max_cal, sum)
        top3 = s[:3]
        result = 0
        for num in top3:
            result += num
        print(result)
        #total = sum(top3)
        # if sum == 64098.0:
        #    print(total)
        sum = 0
f.close()
