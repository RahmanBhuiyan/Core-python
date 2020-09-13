                             # public Access Modifier


"""
class Animal:

    # Constructor
    def __init__(self, name):
        # Animal class has one attribute: 'name'.
        self.name = name

    # Method
    def showInfo(self):
        return self.name

# Cat class extends from Animal.
class dog (Animal):

    def __init__(self, name, age, height):

        # Call to contructor of parent class (Animal)
        # to assign value to attribute 'name' of parent class.
        super().__init__(name)

        self.age = age
        self.height = height

    # Override method.
    def bro(self):

        return (self.name,
        str(self.age),
        str(self.height))


lalu=dog("lalu",1,3)

print(lalu.bro())
print(lalu.showInfo())

"""



                                  # protected Access Modifier


""""
class Animal:

    # Constructor
    def __init__(self, name):
        # Animal class has one attribute: 'name'.
        self._name = name

    # Method
    def _showInfo(self):
        return self._name

# Cat class extends from Animal.
class dog (Animal):

    def __init__(self, name, age, height):

        # Call to contructor of parent class (Animal)
        # to assign value to attribute 'name' of parent class.
        super().__init__(name)

        self._age = age
        self._height = height

    # Override method.
    def _bro(self):

        return(self._name,
        str(self._age),
        str(self._height))



lalu=dog("lalu",1,3)

print(lalu._bro())

"""







                           # private Access Modifier

""""
class Animal:

    def __init__(self,name):
        self.__name=name

    def __chill(self):
        return self.__name

class dog(Animal):
    def __init__(self,name,age):
        super.__init__(name)
        self.age=age




lalu=dog("lalu",1)
print(lalu._dog__chill())

"""

'''
class Foo:

     def __init__(self,name):
         self.__var = 3 # Not private, it's for name mangling

         self.__name=name
     def __okkh(self):
        return (self.__var ,self.__name)


class Bar(Foo):
     def __init__(self,name,age):
         super().__init__(name)

         self.__age=age

     # def chill(self):
     #     return self.__age

     def __chill(self):
         return self.__age





obj = Bar("rahman",18)

print(obj._Foo__var)


print(obj._Foo__okkh())

# print(obj.chill())

print(obj._Bar__chill())


'''

""""
# define parent class Company
class Company:
 # constructor
 def __init__(self, name, proj):
     self.name = name  # name(name of company) is public
     self._proj = proj  # proj(current project) is protected

 # public function to show the details
 def show(self):
     print("The code of the company is = ", self.ccode)


# define child class Emp
class Emp(Company):
 # constructor
 def __init__(self, eName, sal, cName, proj):
     # calling parent class constructor
     Company.__init__(self, cName, proj)
     self.name = eName  # public member variable
     self.__sal = sal  # private member variable

 # public function to show salary details
 def show_sal(self):
     print("The salary of ", self.name, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name, " is working on ", e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()

"""


class Myclass:
     def __init__(self, n):
         self.__n = n

     def __val(self):
         return self.__n


obj = Myclass(2)
obj.__n = 3
# print(obj.val_n())
print(obj._Myclass__val())
print(obj.__n)