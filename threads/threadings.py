# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

import threading
import time
lock = threading.Lock()
data = 8
def func():
	global data
	print '%s acquire lock...' % threading.currentThread().getName()

	if lock.acquire():
		print '%s get the lock.' % threading.currentThread().getName()
		data += 1
		time.sleep(2)
		print '%s release lock...' % threading.currentThread().getName()
		print data
		lock.release()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()