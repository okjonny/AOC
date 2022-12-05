with open('./input3.txt', 'r') as f:
    lines = [line.strip() for line in f]
sum = 0
lineCount = 0

w1, w2, w3 = "", "", ""
for val in lines:
    if not val:
        continue
    lineCount += 1
    abc = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
           'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    ABC = {'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
           'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    s1, s2, s3 = set(), set(), set()
    if lineCount == 1:
        w1 = val
        continue
    elif lineCount == 2:
        w2 = val
        continue
    elif lineCount == 3:
        print(w1)
        w3 = val
        for v in w1:
            s1.add(v)
        for v in w2:
            s2.add(v)
        for v in w3:
            s3.add(v)

        m = min(len(w1), len(w2))
        m = min(m, len(w3))
        for val in s1:
            if val in s2:
                if val in s3:
                    if val in abc:
                        sum += abc[val]
                    else:
                        sum += ABC[val]
        lineCount = 0
print(sum)
