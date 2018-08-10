#!/usr/bin/env python

age_map = { 'john': 10, 'rob': 20 }
print(age_map)
print(age_map['john'])
age_map['mike'] = 45
print(age_map)

#print(age_map['phil']) # exception
if 'phil' in age_map:
    print(age_map['phil'])