import random
import string

length = input('Input the length of password: > ')


lower = string.ascii_lowercase
# upper = string.ascii_uppercase
num = string.digits
# symbols = string.punctuation

all = lower + num

temp = random.sample(all, int(length))

p = open('pass.txt', 'w+')
password = ''.join(temp)
p.write(password)
print(password)
p.close()
