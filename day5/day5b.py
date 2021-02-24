import re

def solve(input):

    count = 0
    # if contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps)
    firstCondition = False
    # if contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa
    secondCondition = False

    for item in input.splitlines():

        # cycle for checking if first condition is met
        for i in range(len(item) - 3):
            for j in range(i, len(item) - 3):
                if((item[0 + i: 2 + i]) == (item[2 + j: 4 + j])):
                    firstCondition = True
                    break

        # if first condition is met, cycle for checking if second condition is met
        if (firstCondition):
            for i in range(len(item) - 2):
                if ((item[0 + i]) == (item[2 + i])):
                    secondCondition = True
                    break

        # if both condition are met, count ++
        if (firstCondition & secondCondition):
            count += 1

        # reset both conditions
        firstCondition = False
        secondCondition = False

    print("Count of nice strings is: ", count)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()