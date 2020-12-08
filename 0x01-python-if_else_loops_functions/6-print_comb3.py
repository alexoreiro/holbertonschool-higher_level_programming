#!/usr/bin/python3
for n in range(90):
    if n // 10 < n % 10:
        print("{:d}{:d}".format(n // 10, n % 10), end="")
        if n != 89:
            print(", ", end="")
        else:
                print("")
