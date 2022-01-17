class MyBaseClass:

    def __init__(self, name:str) -> int:
        self.name = name
        self._length = len(name) # protected
        self.__hidden = "private"

    def info(self):
        print("====\ninfo")
        print("name", self.name)
        print("length", self._length)
        print("hidden", self.__hidden)
        print()


class MyDerivedClass(MyBaseClass):

    def summary(self):
        print("====\nsummary")
        print("name", self.name)
        print("length", self._length)
        print("hidden", self.__hidden)
        print()

    pass

a = MyBaseClass("Fred")
a.info()

b = MyDerivedClass("John")
b.info()
b.summary()



