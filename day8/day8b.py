
def solve(input):

    countAllLiterals = 0
    countEncodeCharacters = 0

    for item in input.splitlines():
        countOfSlashes = item.count("\\")
        countOfQuotes = item.count("\"")

        countAllLiterals += len(item)
        # plus 2 is for first and last added quote
        countEncodeCharacters += len(item) + countOfSlashes + countOfQuotes + 2
        print(len(item) + countOfSlashes + countOfQuotes + 2)

    print("The total number of characters to represent the newly encoded strings minus the number of characters of code"
          " in each original string literal is", countEncodeCharacters - countAllLiterals)



def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()