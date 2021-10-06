import random
import os

def count(a):
    la = list(a)
    i = 0
    for x in la:
        i += 1
    return i

while True:
    os.system('cls')
    a = input("Voer een zin in\n")

    lijst2 = list()

    lijst = a.split(' ')
    for c in lijst:
        if count(c) <= 3:
            lijst2.append(c)
        if count(c) > 3:
            a = random.randrange(0, 15)
            if (a > 7):
                lijst2.append(c[0] + c[1] + "... " + c)
            elif (a > 5):
                lijst2.append(c[0] + c[1] + c[2] + ".. " + c)
            elif (a > 3):
                lijst2.append(c[0] + ".. " + c)
            else:
                lijst2.append(c[0] + c[1] + ".. " + c)

    b = ""
    for x in lijst2:
        b += x+" "

    input(b)