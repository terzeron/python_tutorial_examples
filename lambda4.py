#!/usr/bin/env python

from functools import reduce

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    print(reduce(lambda x, y : x + y, data))
