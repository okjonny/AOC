def distinctChars(dChars: int):
    with open('./input06.txt', 'r') as f:
        nonempty = filter(str.rstrip, f)
        for line in nonempty:
            s = set()
            for idx in range(len(line)):
                val = set(line[idx:idx+dChars])
                if len(val) == dChars:
                    return f'{idx + dChars}'
            return 'No solution'


if __name__ == "__main__":
    print('[A]:', distinctChars(4))
    print('[B]:', distinctChars(14))
