import math

def solve(input):
    total = 0

    for line in input.splitlines():
        newLine = list(map(lambda x: int(x), list(line.split("x"))))
        newLine.sort()
        total += (2 * newLine[0] + 2 * newLine[1] + newLine[0] * newLine[1] * newLine[2])

    print(total)

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()