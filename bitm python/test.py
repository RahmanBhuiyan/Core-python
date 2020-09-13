# a = {}
# print(type(a))
# a=set()
# print(type(a))

# my_dict = {'name': 'Jack', 'age': 26}
# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict.get('address'))

# my_dict = {'name': 'Jack', 'age': 26}
# my_dict['age'] = 27
# print(my_dict)
# my_dict['address'] = 'Downtown'
# print(my_dict)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
squares.clear()
print(squares)
del 3
print(squares)
