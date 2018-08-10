#!/usr/bin/env python

class ParentClass():
    None


class ChildClass(ParentClass):
    def method1(self):
        print("hello world")

instance = ChildClass()
instance.method1()
