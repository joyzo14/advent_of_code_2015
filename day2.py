import math

def solve(input):
    total = 0

    for line in input.splitlines():
        newLine = list(map(lambda x: int(x), list(line.split("x"))))
        minimum = min(newLine[0] * newLine[1], newLine[1] * newLine[2], newLine[2] * newLine[0])
        total += (2 * newLine[0] * newLine[1] + 2 * newLine[1] * newLine[2] + 2 * newLine[2] * newLine[0] + minimum)

    print(total)

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()