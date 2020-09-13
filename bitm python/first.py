class Dog:
    species='This is class attributes'
    # class attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
# 1st obj
buddy = Dog("lalu", 6)
print(buddy.species)
buddy.species = 'this is test'
print(buddy.species)

# 2nd obj
lalu = Dog("lalu-2", 6)
print(lalu.species)

class cat:
    species='This is class attributes'


babal = cat()
print(babal.species)

print(cat().species)














#
# print(buddy.age)
# a = buddy.counter=1
# print(a)
# cc = Dog("Buddy", 9)
# print(cc.counter)
# dd = Dog("Buddy", 9)
# print(dd.counter)