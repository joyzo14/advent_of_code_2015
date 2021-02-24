import re

def solve(input):

    count = 0

    for item in input.splitlines():
        # contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou
        numberOfVowels = len(re.findall(r"[aeiou]", item))
        if((numberOfVowels) >= 3):
            # contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd)
            if(re.search(r"(\w)\1{1,}", item) is not None):
                # does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements
                if (re.search(r"ab|cd|pq|xy", item) is None):
                    count += 1

    print("Count of nice strings is: ", count)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()