#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num1 = number * -1
    num1 = num1 % 10
    num1 = num1 * -1
else:
    num1 = number % 10
print("Last digit of {}".format(number), end=' ')
if num1 > 5:
    print("is {} and is greater than 5".format(num1))
elif num1 == 0:
    print("is {} and is 0".format(num1))
elif num1 < 6 and num1 != 0:
    print("is {} and is less than 6 and not 0".format(num1))
