# class AgeException(Exception):
#     def __init__(self, msg, age ):
#         super().__init__(msg)
#         self.age = age
#
# class TooYoungException(AgeException):
#     def __init__(self, msg, age):
#         super().__init__(msg, age)
#
# class TooOldException(AgeException):
#     def __init__(self, msg, age):
#         super().__init__(msg, age)
#
#     # Function to check age, it may raise exception.
#     def checkAge(age):
#         if (age < 18):
#             # If age is less than 18, an exception will be thrown.
#             # This function ends here.
#             raise TooYoungException("Age " + str(age) + " too young", age)
#
#         elif(age > 40):
#             # If age greater than 40, an exception will be thrown.
#             # This function ends here.
#             raise TooOldException("Age " + str(age) + " too old", age);
#         # If age is between 18-40.
#         # This code will be execute.
#             print("Age " + str(age) + " OK!");


class AgeException:

    def __init__(self, age):
        self.age = age
        # super.__init__(age)
class TooYoungException:
    def __init__(self ,age):
        super().__init__( age)

class TooOldException:

    def __init__(self ,age):
        super().__init__( age)

def checkAge(age):
    if (age < 18):
        # If age is less than 18, an exception will be thrown.
        # This function ends here.
        # raise TooYoungException("Age " + str(age) + " too young", age)
        return age

    elif (age > 40):
        # If age greater than 40, an exception will be thrown.
        # This function ends here.
        # raise TooOldException("Age " + str(age) + " too old", age);
        return age


bro=AgeException(19)

print(bro.TooYoungException)
#
# try :
#     bro.checkAge()
#
# except TooYoungException as e :
#     print("You are too young, not pass!")
#     print("Cause message: ", str(e))
#     print("Invalid age: ", e.age)
#
# except TooOldException as e :
#
#     print ("You are too old, not pass!")
#     print ("Cause message: ", str(e) )
#     print("Invalid age: ", e.age)
