#generate a random number of variable length
import random

numb = ""
def randnum(length):
    for i in range(length-1):
        numb = numb + str(random.randint(0,i))
    return numb


if __name__ == "__main__":
    length = 9
    print(randnum(length))

