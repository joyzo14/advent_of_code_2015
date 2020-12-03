def solve(input):
    count = 0

    for k in input:
        if k == "(":
            count += 1
        else:
            count -= 1

    print(count)

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()