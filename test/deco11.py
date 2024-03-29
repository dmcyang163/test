# -*- coding:utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python
import time
import inspect

def foo(a, b):
    print 'in foo()', a, b
 
# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
     
     
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper(a, b):
        start = time.clock()
        func(a, b)
        end =time.clock()
        print 'used:', end - start
     
    # 将包装后的函数返回
    return wrapper
 
foo = timeit(foo)
foo(1, 2)

print inspect.getargspec(foo)