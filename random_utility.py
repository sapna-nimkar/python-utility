#generate a random number of variable length
import random


def randnum(length=1):
    numb = ""
    for i in range(length):
        numb = numb + str(random.randint(0,9))
    return numb


if __name__ == "__main__":
    length = 9
    print(randnum(length))
    print(randnum())

