class A:
    def __init__(self):
        print("this is init of method of a")
        
    def method1(self):
        print("this is method 1")

class B(A):
    def __init__(self):
        super().__init__()#if u want to print both a and b
        print("this is init of method of b")
    def method2(self):
        print("this is method 2")

class C(B,A):
    def method3(self):
        print("this is method 3")

# obja=A()
objb=B()
# objc=C()
# objc.method1()