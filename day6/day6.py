import re

def solve(input):

    # False means light which is turned off, True is when it is turned on
    grid = [[False for i in range(1000)] for j in range(1000)]
    count = 0

    for item in input.splitlines():
        words = re.findall(r"([A-Za-z]+)", item)
        numbers = re.findall(r"([\d]+)", item)

        # for instructions turn on and turn off
        if (words[0] == 'turn'):
            if(words[1] == "on"):
                for i in range(int(numbers[0]), int(numbers[2]) + 1):
                    for j in range(int(numbers[1]), int(numbers[3]) + 1):
                        grid[i][j] = True

            if(words[1]=="off"):
                for i in range(int(numbers[0]), int(numbers[2]) + 1):
                    for j in range(int(numbers[1]), int(numbers[3]) + 1):
                        grid[i][j] = False
        # for instruction is toggle
        else:
            for i in range(int(numbers[0]), int(numbers[2]) + 1):
                for j in range(int(numbers[1]), int(numbers[3]) + 1):
                    if (grid[i][j] == True):
                        grid[i][j] = False
                    else:
                        grid[i][j] = True

    for i in range(1000):
        for j in range(1000):
            if (grid[i][j] == True):
                count += 1

    print(count, "lights are lit")



def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()