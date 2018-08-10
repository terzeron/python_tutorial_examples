#!/usr/bin/env python

def sub_gen():
    yield "child"
    yield "next child"

def gen():
    yield "left"
    yield from sub_gen()
    #for result in sub_gen():
    #    print(result)
    yield "right"

g = gen()
for result in g:
    print(result)
