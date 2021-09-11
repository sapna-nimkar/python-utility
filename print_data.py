from random_utility import rand_mobile
from random_utility import rand_name


def print_info(array_of_array):
    for contact in array_of_array:
        print("{lname} {fname}'s mobile number is {mobile}".format(fname=contact[0],lname=contact[1],mobile=contact[2])) 

def build_phonebook(count = 1):
    phonebook = []
    for i in range(0,count):
        contact = [rand_name(),rand_name(),rand_mobile()]
        phonebook.append(contact)
    return phonebook

if __name__ == "__main__":
    phonebook = build_phonebook(5)
    print_info(phonebook)

