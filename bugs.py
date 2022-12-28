# try:
#     # this block of code will run add thrown erross if there are a
# except:
#     #this will rise the error 

# else:
#     #this will execute if there are no errors

# finally:
    # this will execute regardless the result of try and except 



# try:
#     f=open("demo.py")
#     try:
#         f.write("ABC")
#     except:
#         print("error in file")
#     finally:
#         f.close()
# except:
#     print("Error in file")
a=5
if a<10:
    raise Exception("value is less than 5")