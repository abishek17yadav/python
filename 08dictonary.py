'''mydict= {
"fast": "in a quick manner",
"harry": "a cooder",
"marks" :[1,2,5],
"anotherdict":{"harry" :"player"},
1:2
}
print(mydict["fast"])
print(mydict["harry"])
print(mydict["marks"])
print(mydict["anotherdict"]["harry"])


# if u want to change anything
mydict["marks"]=[33,44,55]
print(mydict["marks"])

#properties of dictoneries
# it is unordered
# cannot content duplicate keys
# it is mutable means changable
# it is indexed



# methods in dictoneries

#1.keys - to print the keys
print(mydict.keys())  

# to print it type
print(type(mydict.keys()))

#to conver it into a list
print(type(mydict.keys()))


# 2.values  - to get the values 
print(mydict.values())

# 3.items: to print both keys and values
print(mydict.items())

#4.update : to add anything more in the dictonary
print(mydict)
updatedict={
    "abishek":"yadav"
}
mydict.update(updatedict)
print(mydict)


# 5.get  - prints value associated with value
print(mydict.get("")'''

# ------------------------------------------------------------------------------------------------------------------
# they are mutable
# it does not allows duplicate values
# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66
# }
# print(myd)


# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,   #it does not allow duplicate values
#     "age":22,
#     "percentage":88.66
# }
# print(myd)

# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66
# }
# print(len(myd))  #to find the length of the dictonary

# #get method
# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66
# }
# a=myd.get("name")   #to get any values
# print(a)

# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66

# }
# b=myd.keys()  #to print keys 
# print(b)

# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66

# }
# c=myd.values()  #to print values
# print(c)

# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66

# }
# d=myd.items()  #to print items
# print(d)


# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66

# }
# x=myd["age"]   #if u want to print any thing  put in square values 
# print(x)


# myd={
#     "name":"abishek",
#     "class":12,
#     "age":17,
#     "percentage":88.66

# }
# y=myd.update({"name":"rahul"})  #to print keys 
# print(y)






