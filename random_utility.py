#generate a random number of variable length
import random
import string


def randnum(length=1):
    numb = ""
    for i in range(length):
        numb = numb + str(random.randint(0,9))
    return numb

def rand_mobile():
    return "9"+randnum(9)

def rand_name():
    name = random.choice(string.ascii_uppercase)
    for i in range(random.randint(3,6)):
        name = name + random.choice(string.ascii_lowercase)
    return name



if __name__ == "__main__":
    print("directly executed from terminal")
    length = 9
    print(randnum(length))
    print(randnum())
    print(rand_mobile())
else:
    print("Importing Random_utility file")

