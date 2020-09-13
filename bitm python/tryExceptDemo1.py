import ageexception
from ageexception import AgeException
from ageexception import TooYoungException
from ageexception import TooOldException


print ("Start Recruiting ...")

age = 11

print ("Check your Age ", age)

try :

    ageexception.checkAge(age)
    print ("You pass!")

except TooYoungException as e :

    print("You are too young, not pass!")
    print("Cause message: ", str(e) )
    print("Invalid age: ", e.age)

except TooOldException as e :

    print ("You are too old, not pass!")
    print ("Cause message: ", str(e) )
    print("Invalid age: ", e.age)
