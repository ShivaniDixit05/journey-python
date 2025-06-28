# tup = (1) #this is an integer type
# tup = (1,)#this is an tuple type

tup = (1 , 2 , 5 ,3 , "Red" , True)
# tup[0] = 90   #tuple object doesnot support item assignment
# print(type(tup) , tup)
# print(len(tup))

# #tupleIndex
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])
# print(tup[5])
# print(tup[6]) it will gives an error
# print(tup[-1])

if 5 in tup:
    print("Yes 5 is present in this tuple")
else:
    print("No")

tup2 = tup[1:4]    
print(tup2)
