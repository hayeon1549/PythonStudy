import random

def genPass():
    alphabet="abcdefghijklmnopqrstuvwxyz0123456789*&%$#@"
    password=""

    for i in range(8):
        index=random.randrange(len(alphabet))
        password+=alphabet[index]
   
    return password

print(genPass())