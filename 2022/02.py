def win(opponent, me) -> int:
    # Rock - A - X - lose
    # Paper - B - Y - draw
    # Scissors - C - Z - win
    sum = 0
    won = False
    tie = False
    vals = {'X': 1, 'Y': 2, 'Z': 3}
    op = {'A': 'X', 'B': 'Y', 'C': 'Z'}

    if me == 'X':  # lose
        if opponent == 'A':
            sum += vals['Z']
        elif opponent == 'B':
            sum += vals['X']
        elif opponent == 'C':
            sum += vals['Y']
        won = False

    elif me == 'Y':
        sum += vals[op[opponent]]
        sum += 3

    else:
        if opponent == 'A':
            sum += vals['Y']
        elif opponent == 'B':
            sum += vals['Z']
        elif opponent == 'C':
            sum += vals['X']
        sum += 6
    return sum


with open('./', 'r') as f:
    lines = [line.strip() for line in f]

res = 0
for val in lines:
    if val:
        res += win(val[0], val[2])

        print(val[0], "  ", val[2])
print(res)
