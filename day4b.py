import hashlib

def solve(input):


    for i in range(0, 999999999999999):
        # concatenate zeros to string number, if number is less than 100000
        number = str(i)
        str2hash = "iwrupvqb" + number
        result = hashlib.md5(str2hash.encode())

        if(result.hexdigest()[:6]=="000000"):
            print("The hexadecimal equivalent of hash is : ", end="")
            print(str2hash)

            # printing the equivalent hexadecimal value.
            print("Hash which, in hexadecimal, start with at least five zeroes: ")
            print(result.hexdigest())
            print("My puzzle answer is: ", number)
            break


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()