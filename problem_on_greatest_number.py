#take two input from user(int/float) and print nth greatest number 
user1=int(input("enter user1 number:" ))
user2=int(input("enter user2 number:"))

if user1<user2:
    print("user2 is greatest:")
elif user1>user2:
    print("user1 is smallest")        
else:
    print("user not valid")    

