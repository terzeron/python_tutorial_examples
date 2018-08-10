#!/usr/bin/env python

def grep(pattern):
    while True:
        line = yield
        if pattern in line:
            print(line)

c = grep("aaa")
next(c)
c.send("hello world")
c.send("bbb aaa ccc")
c.close()
