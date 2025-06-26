marks = [3 , 4 , 5 , "Siya" , True , 69 , 25  , 12 , 7 , 345]
#PositiveIndex
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5]) #it will gives an index error

#NegstiveIndex
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

#Checking
if "4" in marks:           # in is a keyword
    print("Yes")
else:
    print("No")    
  
#Same thing applies for strings as well    
if 'ya' in "Siya":
    print("Yes")
else:
    print("No")    

print(marks) #print entire list
print(marks[:])

# JumpIndex
print(marks)
print(marks[1:10])
print(marks[1:10:3])  # 3 is a jump index
print(marks[::2])

#ListComprehension
lst1 = [i for i in range(10)]
lst2 = [i*i for i in range(10)]
lst3 = [i*i for i in range(10) if i%2==0]
print(lst1)
print(lst2)
print(lst3)

names = ["Shubham" , "Shivani" , "Nitesh" , "Naitik" , "Pransi"]
nameswith_h = [item for item in names if "h" in item]
print(nameswith_h)

names = ["Milo" , "Sarah" , "Bruno" , "Anastasia" , "Rosa"]
nameswith_o = [item for item in names if (len(item) > 4)]
print(nameswith_o)
