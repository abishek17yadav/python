a=int (input("enter no:"))
b=int(input("enter no:"))
y=input("+,-,*,/")

def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def multiply(n1,n2):
    print(n1*n2)
def divide(n1,n2):
    print(n1/n2)  

if y=="+":
    add(a,b)    
elif y=="-":
    sub(a,b)
elif y=="*":
    multiply(a,b)
elif y=="/":
    divide(a,b)
else:
    print("nothing")                
