#!/usr/bin/env python


class Human:
    def __init__(self, name):
        self._name = name
        print("I'm born now")
        print("My name is '%s'" % self._name)

    def __del__(self):
        print("I'm dead now")


if __name__ == "__main__":
    h = Human("jack")
    print(h._name)
    h._name = "john"
    print(h._name)
