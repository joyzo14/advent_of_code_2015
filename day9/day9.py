import re

def solve(input):

    countAllLiterals = 0
    countInMemory = 0

    for item in input.splitlines():
        countOfSlashes = item.count("\\")
        # find hexacedimal notations
        a = re.findall(r"\\[xX][0-9a-fA-F]{2}", item)

        twoSlashes = item.count("\\\\")
        countAllLiterals += len(item)
        # count all literals of word reduced of the all slashes, reduced of first and last quote '-2',
        # reduced of 2 * length of count of hex in string, because every hexadecimal notation represents single character
        countInMemory += len(item) - countOfSlashes - 2 + twoSlashes - 2*(len(a))

    print("The total number of characters of string code minus the total number of characters in memory are", countAllLiterals - countInMemory)



def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()