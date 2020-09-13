f=open('myData.py','r')


f1=open('abc','w',encoding = 'cp1252')

for data in f:
    f1.write(data)
f1.close()

import os