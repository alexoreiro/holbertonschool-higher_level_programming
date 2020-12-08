#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        print("{:s}".format(chr(c)), end="")
    else:
        print("{:s}".format(chr(c - 32)), end="")
