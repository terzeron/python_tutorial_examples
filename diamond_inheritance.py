#!/usr/bin/env python

class A():
    def greet(self):
        print("hello A")

class B(A):
    def greet(self):
        print("hello B")

class C(A):
    def greet(self):
        print("hello C")

class D(B, C):
    #def greet(self):
        #print("hello D")
    pass

d = D()
d.greet()
print(D.__mro__)
