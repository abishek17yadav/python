# how to calculate avg marks
# methods
class student:
    numberofsubject=5 
    def __init__(self,marks1,marks2,marks3):
        self.web=marks1
        self.python=marks2
        self.math=marks3
    def avg(self):
        print((self.web+self.python+self.math)/3)

    # def getmarks(self):   
    #     return self.math    #accessor

    # def setmarks(self,marks):  #mutators
    #     self.math=marks
    @classmethod
    def classmethodexample(cls):
        return cls.numberofsubject
    @staticmethod
    def staticmethodexample():
        print("this is an example of static method")



student1=student(10,10,10)        
student2=student(9,9,9)        
student3=student(10,9,8)


print(student.classmethodexample())
student.staticmethodexample()
student1.avg()
student2.avg()
student3.avg()

