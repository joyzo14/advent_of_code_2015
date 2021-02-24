import re

def solve(input):

    # 0 means light which is turned off
    grid = [[0 for i in range(1000)] for j in range(1000)]
    count = 0

    for item in input.splitlines():
        words = re.findall(r"([A-Za-z]+)", item)
        numbers = re.findall(r"([\d]+)", item)

        # for instructions turn on and turn off
        if (words[0] == 'turn'):
            if(words[1] == "on"):
                for i in range(int(numbers[0]), int(numbers[2]) + 1):
                    for j in range(int(numbers[1]), int(numbers[3]) + 1):
                        grid[i][j] += 1

            if(words[1]=="off"):
                for i in range(int(numbers[0]), int(numbers[2]) + 1):
                    for j in range(int(numbers[1]), int(numbers[3]) + 1):
                        # check if value on this coordinates is greater than 0, because we can't go to negative number
                        if(grid[i][j]) > 0:
                            grid[i][j] -= 1
        # for instruction is toggle
        else:
            for i in range(int(numbers[0]), int(numbers[2]) + 1):
                for j in range(int(numbers[1]), int(numbers[3]) + 1):
                    grid[i][j] += 2

    for i in range(1000):
        for j in range(1000):
            count += grid[i][j]

    print(count, "lights are lit")



def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()