# -*- coding:utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python
import sys #  模块，sys指向这个模块对象
import inspect
def foo(): pass # 函数，foo指向这个函数对象
 
class Cat(object): # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name
    def sayHi(self): #  实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!' # 访问名为name的字段，使用实例.name访问
cat = Cat('kitty')
 
print cat.name # 访问实例属性
cat.sayHi() # 调用实例方法
 
print dir(cat) # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'): # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger') # same as: a.name = 'tiger'
print getattr(cat, 'name') # same as: print a.name
 
getattr(cat, 'sayHi')() # same as: cat.sayHi()

def foo():
    n = 1
    def bar():
        print n # 引用非全局的外部变量n，构造一个闭包
    n = 2
    return bar
 
closure = foo()

print closure.func_closure