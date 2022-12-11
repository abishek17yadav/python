#write a program to display all prime numbers within a range 
start=int(input("enter the start of range:"))
end=int(input("enter the end of range:"))
for val in range(start,end+1):
    if val>1:
        for n in range(2,val):
            if (val%n)== 0: break
else:
    print(val)    
