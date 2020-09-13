# class person:
#     okk="chap niban na bai"
#
# bro=person()
# print(person.okk)
#
# bro.okk="chap nita paran"
# print(bro.okk)
#
# person.okk="bala lagar na"
#
# print(person.okk)

# class me:
#
#     def bro(self):
#         print("shob thik haa")
# my=me()
# print(my.bro())

# class mobile:
#     def __init__(self):
#         self.modle="walton ef9"
#
#     def show_modle(self,p):
#         self.pice=p
#         print(self.modle,self.pice)
#
# bro=mobile()
# bro.show_modle(4500)


class mobile :
    def __init__(self):
        self.modle="primo ef9"

    def show_modle(self,p):
        self.prize=p
        print("modle:",self.modle)
walton=mobile()
print(walton.show_modle(5))
linux=mobile()
print(linux.show_modle(20))
