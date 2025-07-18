# NORMAL CODE :

marks = [12 , 45 , 32 , 98 , 45 , 1 , 4 , 36]

index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("Harry , Awesome!")
    index += 1    

# ENUMERATE :

marks = [12 , 45 , 32 , 98 , 45 , 1 , 4 , 36] 

for index , mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Harry,Awesome !!!")


# Changing the start index

fruits = ["Mango" , "Grapes" , "Watermelon" , "BlackBerry"]

for index , fruit in enumerate(fruits , start = 1):
    print(index , fruit )

fruits = ["Banana" , "Sapodilla" , "Cherry" , "Apple" , "Pappaya"]

for index , fruit in enumerate(fruits):
    print(f"{index + 1} : {fruit}")

#  tuple

a = ("Red" , "Blue" , " Green" , "Pink" , "Yellow")

for index , color in enumerate(a , start = 1):
    print(index , color)

# string

s = "Hello Sarr 🤗"    

for index , string in enumerate(s):
    print(index , string)
