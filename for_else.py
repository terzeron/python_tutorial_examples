#!/usr/bin/env python

list = [1, 2, 3, 4, 5]
for item in list:
    if item > 4:
        print("%d: greater than 4" % (item))
        break
else:
    print("not greater than 6")
