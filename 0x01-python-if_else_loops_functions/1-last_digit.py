#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
if last > 5:
    print("Last digit of %d is %d and is greater than 5" % (number, last))
elif last < 6 and last != 0:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, last))
else:
    print("Last digit of %d is %d and is 0" % (number, last))
