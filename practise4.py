class vehicle:
    def category(self):
        print("This is a category of vehicle")
    
    def go(self):
        print("i am fast")


class car1(vehicle):
    def sizeParameter(self):
        print("i am small in size")
class car2(vehicle):
    pass
class bus(vehicle):
    def go(self):
        print("I am very large")

objvehicle =vehicle()
objcar1 = car1()
objcar2 = car2()
objbus = bus()

objvehicle.category()
objvehicle.go()
objcar1.category()
objcar1.go()
objcar2.category()
objcar2.go()
objbus.category()
objbus.go()
