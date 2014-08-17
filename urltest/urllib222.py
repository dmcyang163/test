# encoding: UTF-8
#!/usr/bin/python
#!/usr/bin/env python
import sys 
import inspect 
reload(sys) 
sys.setdefaultencoding('utf8') 



import urllib2

response = urllib2.urlopen('http://www.baidu.com/')  
html = response.read()

print html

print inspect.getargspec(response.read)