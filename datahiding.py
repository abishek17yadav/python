class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
# accees-

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

person1=person("abishek",18)
print(person1._person__name)