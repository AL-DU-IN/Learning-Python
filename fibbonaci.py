# -*- coding: utf-8 -*-
import sys
def fibonacci(n):
    fib=[0,1]
    for i in range(n):
        fib.append(fib[-2]+fib[-1])
    return fib
def main():
    m=int(raw_input("Enter the range\n"))
    print(fibonacci(m))
main()