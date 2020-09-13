# import time
# start_getattr = time.time()
# print(start_getattr )



# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"
#
# x = getattr(Person, 'age','success')
#
# print(x)



class Person:
    age = 23
    name = 'Adam'
    year=2020
obj = Person()

b=hasattr(obj, "year")
# print(hasattr(obj, "student"))
print(b)


# class Person:
#     name = 'Adam'
#     age=20
#
# p = Person()
# # chill=setattr(p, 'name', 'John')
# setattr(p, 'year', '2020')
# print(p.year)
# # print(d)


# class Coordinate:
#   x = 10
#   y = -5
#   z = 0
#
# point1 = Coordinate()
#
# chill=delattr(point1,"z")
# # print(point1.Coordinate)
# print(chill)

class chill:
    name="raihan"
    age=21

obj=chill()
# setattr(obj,"year","2020")
obj.year=2020
print(obj.year)
