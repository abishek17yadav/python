# fibonacci series  = 0,1,1,2,3,5,8,13,21,24
# here 0 and 1 are fix
# the third num is sum of first two and sooo on for all.....

def fibonacci_seq(n):
    a=0#1st number
    b=1#2nd number
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c=a+b 
            a=b  
            b=c 
            print(b,end=" ")


fibonacci_seq(30)