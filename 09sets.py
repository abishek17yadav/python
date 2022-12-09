'''# a={1,3,4,5,1} #here you cannot have repetative items it will print same and not repeate it
# print(type(a))
# print(a)

#sets  is a collection of non repetative ,does not have repetative items


#to create a empty set
b= set()
print(type(b))


#u cannot add list in a set,also dictonary
#methods in sets

#1.add   - to add any thing in the  set ,you can add any number.
b.add(17)
b.add(24)
#u can add tuple in a set
b.add((4,5,6))
print(b)

#properties
# are unordered
# un indexed
# cannot change any item in a set
#cannot contain duplicate values


# 2. lenth mehod   - prints the lenth of this set
print (len(b))


#3.remove- to remove 5 from set b 
# b.remove(5)
# print(b)

# pop
# print(b.pop())
# print(b)


#s.clear
#s.union
#s.intersection'''



#-----------------------------------------------

#  set- store multiple values in single variable
# unordered
# done by   "{  }"
#unchangeable
# cannot add duplicate values


# -------------------------------------------------------------------------------------------------------
# set1={"car","boat","train"} 
# set2={1,2,3}
# set1.remove("car") # to remove anything from set
# print(set1)

# set1={"car","boat","train"} 
# set2={1,2,3}
# set1.add("cycle")# to add anything from set
# print(set1)

# set1={"car","boat","train"} 
# set2={1,2,3,4}
# set3={4,5,6,7}
# o=set2.union(set3)   #to do union
# print(o)

# set1={"car","boat","train"} 
# set2={1,2,3,4}
# set3={4,5,6,7}
# o=set2.intersection(set3)   #to do intersection
# print(o)

# set1={"car","boat","train"} 
# set2={1,2,3,4}
# set3={4,5,6,7}
# o=set2.union(set3)   #to do symmetric difference
# o2=set2.symmetric_difference(set3)
# print(o)

# set1={"car","boat","train"} 
# set2={1,2,3,4}
# set3={4,5,6,7}
# o=set2.update(set3)   #to do update
# print(o)



