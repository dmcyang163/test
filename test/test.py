#!/usr/bin/python
#!/usr/bin/env python

import sys
import os

print "hello"
print "123123"
print "test"
print sys.path
print os.path
print sys.argv[0]
workpath = os.path.dirname(os.path.abspath(sys.argv[0]))
print workpath

f = open("test.py")
line = f.readline()
while line:
	print line,
	line = f.readline()
f.close()

def add(a, b):
	return a+b

if __name__ == '__main__':
	print add(1,3)

