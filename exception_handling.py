a = input("Enter the number : ")
print(f"Multiplication table of {a} is : ")

for i in range (1 , 11):
    print(f"{int(a)} X {i} = {int(a)*i}")

print("Some imp lines of code")
print("end of program")    


# in this if i gave input as a string then it does not throw an error

a = input("Enter the number : ")
print(f"Multiplication table of {a} is : ")

# if you want to run whole code without any error you can use try

try:
 for i in range (1 , 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
   print("Sorry some Error occur")
   print("Invalid Input!")

print("Some imp lines of code")
print("end of program")       


# like this we can handle so many errors
try:
  num = int(input("Enter the number : "))
  a = [6 , 3]
  print(a[num])
except ValueError:
  print("Number entered is not an integer")
except IndexError:
  print("Index Error")    
