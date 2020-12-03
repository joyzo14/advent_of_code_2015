import math

def solve(input):

    total = 1
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    points = {}
    points2 = {}
    points [0] = [0]
    count = 0

    for direction in input:
        if (direction == '<'):
            if (count % 2 == 0):
                x -= 1
            else:
                x2 -= 1
        elif (direction == '>'):
            if (count % 2 == 0):
                x += 1
            else:
                x2 += 1
        elif (direction == '^'):
            if (count % 2 == 0):
                y += 1
            else:
                y2 += 1
        elif (direction == 'v'):
            if (count % 2 == 0):
                y -= 1
            else:
                y2 -= 1

        if (count % 2 == 0):
            print("x a y su")
            print(x, y)
            if (x in points):
                if (y in points[x]):
                    print("a")
                    print("total is " + str(total))
                    pass
                else:
                    print("b")
                    points[x].append(y)
                    total += 1
                    print("total is " + str(total))
            else:
                print("c")
                points[x] = [y]
                total += 1
                print("total is " + str(total))
        else:
            print("x2 a y2 su")
            print(x2, y2)
            if (x2 in points):
                if (y2 in points[x2]):
                    print("a")
                    print("total is " + str(total))
                    pass
                else:
                    print("b")
                    points[x2].append(y2)
                    total += 1
                    print("total is " + str(total))
            else:
                print("c")
                points[x2] = [y2]
                total += 1
                print("total is " + str(total))

        count += 1
    print(total)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()