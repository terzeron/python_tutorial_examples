#!/usr/bin/env python

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

for i in range(40):
    print(fib(i))
