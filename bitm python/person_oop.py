class Person:
    # The age and gender parameters has a default value.
    def __init__ (self, age = 18, gender = "Male" ):

        self.age = age
        self.gender= gender
    def showInfo(self, name,):
        self.name=name
        return self.name

okh=Person()

print(okh.showInfo("Rahman Bhuiyan"))

print(okh.name)

# print(okh.name)
# print(okh.age)