#take input from 3 people and determine the oldest and youngest
abishek=int(input("enter abishek age:"))
bishal=int(input("enter bishal age:"))
awnit=int(input("enter awnit age:"))

if abishek<=17 and abishek<=25:
    print("abishek is youngest")
elif bishal>17 and bishal<=30:
    print("bishal is oldest")
else:
    print("awnit is child")     

