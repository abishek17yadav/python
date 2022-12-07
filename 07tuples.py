'''#t=(1,2,3,4,5)
#print(t[0])



#tuple- store multiple items in a single variable 
# non homogeneous
# ordered  - they will not suggle
# immutable- you cannot add or remove or you cann not change anything
# it also allows duplicate values
# done by paranthesis()


#tuples - you cannot change any data in a tuple

# to print 1 element in a tuple
# t1=()
# t1=(1)
# t1=(1,)
# print(t1) 

t=(1,2,4,5,1)

#methods in tuple 
#--it will count how namy times 1 is there

#count-it will count how namy times 1 is there
print(t.count(1))

#index- it will say on which number the index is
print(t.index(5))'''

# len - to print the length
# my=(1,2,3,45,)
# print(len(my))


#t1=("car","bike","boat","jet")  # if u want the any value of tuple do:
# print(t1[1])
# print(t1[3:])
# list1=list(t1)   # to convert a tuple to list
# list1.append("cycle")
# t2=tuple(list1)
# print(t2) # to do list to tupple  

# list1=list(t1)   
# list1.reverse()  to reverse the tuple
# t2=tuple(list1)
# print(t2) 

# t=("abishek",)   # if u want to print abishek put , and do as below mentioned 
# print(tuple(t))




# list1=list(t1)   
# list1.pop(2)  # it willl delete the index 2
# t2=tuple(list1)
# print(t2) 


# t3=(1,2,3,[6,7],4,5)  # to print the index 
# print(t3[3][0])


# swapping - the tuple
# tup1=(30,40)
# tup2=(10,20)
# tup1,tup2=tup2,tup1
# print(tup1)
# print(tup2)


#pacing and unpackking of tuples
#-------------------------------------
# tuple1=(1,2,3)
# (one,two,three)=tuple1
# print(one)

# tuple2=("car","bike","boat")
# (item1,item2,item3)=tuple2
# print(item1)


# p=(10,20,30,40)
# (a,b,c,d)=p
# print(a)
# print(b)
# print(c)
# print(d)

# a=(1,2,3)  #add two tuples
# b=("a","b")
# print(a+b)

#tuples - store multiple items in a single variable
# non homogeneous
# ordered
#unchangable / immutable
# allows duplicate value


# myTuple = (1,2,3,4,4)
# print(len(myTuple))
# print(myTuple)


# tuple1 = ("apple",1, 1.1)
# print(tuple1)


# tuple1 = ("car", "bike", "boat", "jet")
# print(tuple1[:3])

# tuple1 = ("car", "bike", "boat", "jet")
# list1 =  list(tuple1)
# list1.append("cycle")
# tuple2 = tuple(list1)
# print(tuple2)

# tuple1 = (10,20,30,40,50)
# #reverse it

# tuple1 = ("apple", "orange", "pineapple")
# del tuple1
# print(tuple1)


# tuple1 = (1,2,3,[6,7],4,5)
# print(tuple1[3][0], tuple1[4])

# tuple1 = (10,20)
# tuple2 = (30, 40)

#swap the tuples
#output - 
# tuple1 : (30,40)
# tuple2 : (10, 20)


#packing and unpacking
# tuple1 = (1,2,3)
# (one, two, three) = tuple1

# print(one)
# print(two)
# print(three)


# tuple1 = ("car", "bike", "boat", "cycle")
# (item1, *item2) = tuple1

# print(item1)
# print(item2)


#write a program to unpack folowwing tuple into 4 variables

# tuple1 = (10,20,30,40,20)
#count and print occurences of 20


# i = 0
# while i < len(tuple1):
#     print(tuple1[i])
#     i += 1














