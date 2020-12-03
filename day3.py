import math

def solve(input):

    total = 1
    x = 0
    y = 0
    points = {}
    points [0] = [0]

    for direction in input:
        if (direction == '<'):
            x -= 1
        elif (direction == '>'):
            x += 1
        elif (direction == '^'):
            y += 1
        elif (direction == 'v'):
            y -= 1

        print(x, y)
        if (x in points):
            if(y in points[x]):
                print("a")
                print("total is " + str(total))
                pass
            else:
                print("b")
                points[x].append(y)
                total += 1
                print("total is "+ str(total))
        else:
            print("c")
            points[x] = [y]
            total += 1
            print("total is " + str(total))

    print(total)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()