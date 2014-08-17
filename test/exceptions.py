try:   
    a=b   
    b=c   
except Exception,e:   
    print Exception,":",e

import traceback   
try:   
    a=b   
    b=c   
except:   
    traceback.print_exc()   