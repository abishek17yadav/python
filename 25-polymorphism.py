#polymorpism-poly means many and morf means forms= many forms

# a="hello"
# print(len(a))

# b=[1,2,3,4,5]
# print(f"length of list is {len(b)}")

# class rect:
#     def calculatearea(self,length,breadth):
#         return length*breadth

#     def calculatearea(self,length):
#         return length*length

# rectangle=rect
# print(rectangle.calculatearea(2,3))

# class bird:
#     def catagery(self):
#         print("i can fly")
# class sparrow:
#     def sizeparameter(self):
#         print("i am small in size")
# class crow:
#     pass
# class ostrich:
#     pass


# objbird=bird
# objsparrow=sparrow
# objcrow=crow
# objostrich=ostrich

class Bird:
    def category(self):
        print("This is a category of bird")
    
    def fly(self):
        print("I can fly")


class Sparrow(Bird):
    def sizeParameter(self):
        print("i am small in size")
class Crow(Bird):
    pass
class Ostrich(Bird):
    def fly(self):
        print("I cannot fly, sorry")

objBird = Bird()
objSparrow = Sparrow()
objCrow = Crow()
objOstrich = Ostrich()

objBird.category()
objBird.fly()
objCrow.category()
objCrow.fly()
objSparrow.category()
objSparrow.fly()
objOstrich.category()
objOstrich.fly()


