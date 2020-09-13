# f=open('myData.py','r')
#
#
# f1=open('abc','w',encoding = 'cp1252')
#
# for data in f:
#     f1.write(data)
# f1.close()
try:
    y=open("chill.jpg.jpg","rb")
    x=open("mypic.jpg","wb")
    for i in y:
        x.write(i)
finally:
    x,y.close()


# okk=open("Hmmm.wmv","rb")
# bro=open("myvideo","wb")
# for c in okk:
#     bro.write(c)