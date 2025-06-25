def average(a,b):
    print("The average is :" , (a+b)/2)
average(4,6)    

# --------: Default arguments :------------

def average(a = 2 , b = 4):
    print("The average is :" , (a+b)/2)
average()   #Take the value of a and b from function
average(5)    #Take the vaue of a is 5 and value of b is 4
average(b=8)  #Take the value of a is 2

def name(fname , midname = "kumar" , lastname = "Dixit"):
    print("My brother name is :", fname , midname , lastname)
name("Nitesh")    
name("Nitesh" , "Dhruv")
name("Niteh" , "Dhruv" , "Naitik")

# -------: Keyword arguments :----------
#In this type of arguments order doesn't matter

def average(a,b):
    print("The average value is : " , (a+b)/2)
average(b=10 , a=2)    #Order 


#--------: Requirement arguments :--------
#IN THIS ALL PARAMETER'S VALUES ARE REQUIERED

def average(a,b):
    print("The average valur is :" , (a+b)/2)
#average(3)    #it will give an error because the value of b is also required , here a and b are required arguments
average(4,2)

def name(Fname , MidName , LastName):
    print("Hello" , Fname , MidName , LastName)
# name("Nitesh" , "Kumar")    # it will gives an error because the value of LastName is required
name("Nitesh" , "Kumar" , "Dixit") 

#----------: Value-Length arguments :---------

def average(*numbers):  # * means tuple
    print(type(numbers))  # numbers is tuple type
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average value is :" , sum/len(numbers))
# average(5,6,7,8)

def name(**name):
    print(type(name))
    print("Hello" , name["Fname"] , name["MidName"] , name["LastName"])
name(Fname = "Naitik" , MidName = "Kumar" , LastName = "Dixit")    

# ----------: Return Statement :--------

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("The average value is :" , sum/len(numbers))
    return sum/len(numbers)
c = average(2,4,6)
print(c)
