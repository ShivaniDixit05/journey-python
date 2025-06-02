a = int(input("Enter your age :"))
print("Your age is :",a)

#Conditional operators :-
# > , < , >= , <= , == , !=
# print(a > 18)
# print(a >= 18)
# print(a <= 18)
# print(a == 18)
# print(a != 18)

if (a > 18):
    print("You can drive")
else:
    print("You cannot drive")    
print("yes")    # it is not the part of else


ApplePrice = 210
Budget = 200
if (ApplePrice <= Budget):
    print("Alexa , add 1kg apples to the cart")             #space is known as indentation
else:
    print("Alexa , do not add apples to the cart")   
 
#elif 
num = int(input("Enter the number :"))
if(num < 0):
    print("Number is negative")    
elif(num == 0):
    print("Number is zero")
elif(num == 999):
    print("Number is special")
else:
    print("Number is positive")            

