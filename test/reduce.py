#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def add(x,y):
    return x+y
 
print reduce(add,range(1,11),100)

print map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])