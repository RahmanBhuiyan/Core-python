class Animal :
    def __init__(self, name):
        self.name=name

    def showInfo(self):
        print("I'm " + self.name)

    def move(self):
        print("moving ...")