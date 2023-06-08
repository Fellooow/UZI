# from random import *
# # import string
# import time
#
# # user_pass = ''
# file = open("pass.txt", "r")
# user_pass = file.read()
# file.close()
#
# # print(user_pass)
# # time_start = time.process_time()
# # alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л',
# #             'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
# #             'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#             'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# t1 = time.time()
# # start = time.time()
# # counter = 1
# '''
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# num = string.digits
# # symbols = string.punctuation
#
# all = lower + upper + num
# '''
# guess = ''
#
# while guess != user_pass:
#     guess = ''
#     for letter in range(len(user_pass)):
#         guess_letter = alphabet[randint(0, 35)]
#         guess = str(guess_letter) + str(guess)
#     print(guess)
# # time_stop = time.process_time()
#
# print('Time to brute-force password: ', time.time()-t1)
# print('Your password is: ', guess)

import string
from itertools import product
from time import time
from numpy import loadtxt

def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False


def bruteforce(password, max_nchar=8):

    print('1) Comparing with most common passwords')
    common_pass = loadtxt('probable passwords.txt', dtype=str)
    cp = [c for c in common_pass if c == password]

    if len(cp) == 1:
        print('\nPassword:', cp)
        return cp

    print('2) Digits cartesian product')
    for i in range(1, 9):
        generator = product(string.digits, repeat=int(i))
        print("\t..%d digit" % i)
        p = product_loop(password, generator)
        if p is not False:
            return p

    print('3) Digits + ASCII lowercase')
    for i in range(1, max_nchar + 1):
        print("\t..%d char" % i)
        generator = product(string.digits + string.ascii_lowercase,
                            repeat=int(i))
        p = product_loop(password, generator)
        if p is not False:
            return p

    print('4) Digits + ASCII lower / upper + punctuation')

    # Same as possible_char = string.printable[:-5]
    all_char = string.digits + string.ascii_letters + string.punctuation

    for i in range(1, max_nchar + 1):
        print("\t..%d char" % i)
        generator = product(all_char, repeat=int(i))
        p = product_loop(password, generator)
        if p is not False:
            return p


start = time()
bruteforce('6zwh3lyrv0')  # Try with '123456' or '751345' or 'test2018'
end = time()
print('Total time: %.2f seconds' % (end - start))
