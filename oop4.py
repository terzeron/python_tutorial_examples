#!/usr/bin/env python

class Human:
    def __init__(self, name):
        self.name = name
        print("I'm born now")
        print("My name is '%s'" % self.name)

    def __del__(self):
        print("I'm dead now")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


if __name__ == "__main__":
    h = Human("jack")
    print(h.name)
    h.name = "john"
    print(h.name)
