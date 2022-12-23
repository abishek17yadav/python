class A:
    def method1(self):
        print("this is method 1")

class B(A):
    def method2(self):
        print("this is method 2")

class C(B):
    def method3(self):
        print("this is method 3")

obja=A()
objb=B()
objc=C()

objc.method1()