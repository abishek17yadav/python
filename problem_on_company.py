#company will give bonus base on following criteria
#time spent in company               bonus

#greater than 10 years                10%
#more than 6and less than 10            8%
#less than 6                            5%

#ask the salary and time spent by the userand print the net bonus amount accordlingly

salary=int(input("enter the salary:"))
time=int(input("enter the time spent:"))

if time>10:
    print("his net salary is:",salary+salary*1/10)
elif time>6 and time<=10:
    print("his net salary is :",salary+salary*1/8)
elif time<6:
    print("his net salary is :",salary+salary*1/5)
else:
    print("not valid")     
