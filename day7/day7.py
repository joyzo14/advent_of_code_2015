import re

def solve(input):

    instructions = []

    for item in input.splitlines():
        # for example gj RSHIFT 1 -> hc
        if ("RSHIFT" in item):
            a = re.search(r"(\S*) (\S*) (\d*) -> (\S*)", item)
            instructions.append([a.group(2), a.group(1), a.group(3), a.group(4)])

        # for example jk LSHIFT 15 -> jo
        elif ("LSHIFT" in item):
            a = re.search(r"(\S*) (\S*) (\d*) -> (\S*)", item)
            instructions.append([a.group(2), a.group(1), a.group(3), a.group(4)])

        # for example lf AND lq -> ls
        elif ("AND" in item):
            a = re.search(r"([a-z1-9]*) (\S*) ([a-z1-9]*) -> (\S*)", item)
            instructions.append([a.group(2), a.group(1), a.group(3), a.group(4)])

        # for example jn OR jo -> jp
        elif ("OR" in item):
            a = re.search(r"([a-z1-9]*) (\S*) ([a-z1-9]*) -> (\S*)", item)
            instructions.append([a.group(2), a.group(1), a.group(3), a.group(4)])

        # for example NOT ls -> lt
        elif ("NOT" in item):
            a = re.search(r"(\S*) (\S*) -> (\S*)", item)
            instructions.append([a.group(1), a.group(2), a.group(3)])

        # for example 19138 -> b
        elif (any(i.isdigit() for i in item)):
            a = re.search(r"(\d*) -> (\S*)", item)
            instructions.append([a.group(1), a.group(2)])

        # for example lx -> a
        else:
            a = re.search(r"(\S*) -> (\S*)", item)
            instructions.append([a.group(1), a.group(2)])
            print(item)

    def calculateSignal(wire, listOfInstructions):



    print(calculateSignal("a", instructions))



def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()