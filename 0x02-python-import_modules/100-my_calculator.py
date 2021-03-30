#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    ac = len(argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        n1 = int(argv[1])
        op = argv[2]
        n2 = int(argv[3])
        if op != '+' and op != '-' and op != '*' and op != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif op == '+':
            print("{:d} {} {:d} = {:d}".format(n1, op, n2, add(n1, n2)))
        elif op == '-':
            print("{:d} {} {:d} = {:d}".format(n1, op, n2, sub(n1, n2)))
        elif op == '*':
            print("{:d} {} {:d} = {:d}".format(n1, op, n2, mul(n1, n2)))
        elif op == '/':
            print("{:d} {} {:d} = {:d}".format(n1, op, n2, div(n1, n2)))
