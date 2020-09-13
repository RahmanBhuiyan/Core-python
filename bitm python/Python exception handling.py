# print ("Three")
# # This division no problem.
# value = 10 / 2
# print ("Two")
# # This division no problem.
# value = 10 / 1
# print ("One")


# d = 0
# # This division has problem, divided by 0.
# # An error has occurred here.
#
#
# try:
#     # This division has problem, divided by 0.
#     # An error has occurred here (ZeroDivisionError).
#     value = 10 / d
#     print ("value = ", value)
#
# except ZeroDivisionError as e :
#     print("Error: ", str(e))
#     print("Ignore to continue ...")
# print ("Let's go!")



# x=10/0
# print(x)
# x=10/1
# print("two")
d=0
try :
    # This division has problem, divided by 0.
    # An error has occurred here (ZeroDivisionError).

    x=10 / d
    print("value = ",x)

except ZeroDivisionError as chill:
    print("Error: ", chill)
    print("Ignore to continue ...")