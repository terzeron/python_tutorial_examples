#!/usr/bin/env python

def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

g = fib(40)
for result in g:
    print(result)
