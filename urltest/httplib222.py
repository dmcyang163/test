# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python


import httplib  
conn = httplib.HTTPConnection("www.csdn.net")  
conn.request('get', '/')  
print conn.getresponse().read()  
conn.close()  