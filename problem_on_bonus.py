#a company decided to give bonus 0f 1000rs to employee if his service is more than five years ask user their slaryand year of service and print the net bonus amount

salary=int (input("enter the amount:"))
years=int (input("enter the number of years been:"))
 
if years>5:
    print("his net salary is:",salary+1000)
else:
    print("same salary:")
