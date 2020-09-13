# class Customer :
#     'This is Customer class'
#     def __init__(self, name, phone, address):
#         self.name = name
#         self.phone = phone
#         self.address = address
#
# john = Customer("John",1234567, "USA")
# print(john.__dict__)

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     return n**2

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     return n**2
#
# print(square.__doc__)

# print(cl.__doc__)

class B:
    name = 'B'
    def __init__(self):
        self.name = 'A'
obj=B()

print(B.__dict__)
print(obj.__dict__)