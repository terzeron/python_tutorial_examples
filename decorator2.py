#!/usr/bin/env python


def parent(func):
    def wrapper_func():
        print("going in to parent()")
        func()
        print("going out from parent()")
    return wrapper_func

@parent
def child1():
    print("in child1()")

@parent
def child2():
    print("in child2()")


child1()
child2()


