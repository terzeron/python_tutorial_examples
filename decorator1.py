#!/usr/bin/env python

def parent(func):
    def wrapper_func():
        print("going in to parent()")
        func()
        print("going out from parent()")
    return wrapper_func

def child1():
    print("in child1()")

def child2():
    print("in child2()")

parent(child1)()
parent(child2)()


