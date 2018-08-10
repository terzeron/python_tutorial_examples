#!/usr/bin/env python

class MyClass():
    def __init__(self):
        print("MyClass()")

    def greet(self):
        print("hello")


if __name__ == "__main__":
    mc = MyClass() 
    mc.greet()
