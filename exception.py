#!/usr/bin/env python


int_list = [1, 2, 3]

try:
    print(int_list[5])
except IndexError as e:
    print("exception occurred")
    #raise e
else:
    print("no exception")
finally:
    print("end of try...except clause")