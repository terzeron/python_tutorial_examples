#!/usr/bin/env python

class Human:
    def __init__(self, name):
        self.name = name
        print("I'm born now")
        print("My name is '%s'" % self.name)

    def __del__(self):
        print("I'm dead now")


h = Human("jack")
