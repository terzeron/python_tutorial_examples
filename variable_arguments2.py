#!/usr/bin/env python

def filter_by_key(key, **kwargs):
    for k, v in kwargs.items():
        if k == key:
            return v

print(filter_by_key("a", b=4, a=5, c=1))

