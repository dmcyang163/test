import os.path
print os.path.dirname(__file__)
dname = os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')
print dname
