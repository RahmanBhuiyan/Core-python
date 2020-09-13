import mysql.connector as mysqal

# bro=mysql.connector.connect(host="localhost",database="customer" ,user="root",passwd="")

db=mysqal.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer"

)
print(db)