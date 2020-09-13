
try:
    m=open('chill.py','r',encoding = 'cp1252')
    m.tell()
    print(m.read())
finally:
    m.close()
for ohh in m:
    print(ohh,end='')




