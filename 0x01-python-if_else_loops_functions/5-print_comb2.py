#!/usr/bin/python3
for n in range(100):
    if n != 99:
        print("{:d}{:d}, ".format(n // 10, n % 10), end="")
    else:
        print("{:d}".format(n))
