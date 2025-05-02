# ---: EXPLICIT TypeCasting :---

a = "2"
b = "1"         
print(int(a) + int(b))     # string converted into integer 

# string  = "15"
# number = 7
# string_number = int(string)
# sum = number + string_number
# print("The sum of both the numbers is :" , sum)


# ---: IMPLICIT TypeCasting :---

c = 6.2
print(type(c))

d = 5
print(type(d))

c = c + d
print("Sum =",c)   # integer converted into float by itself(python)
print(type(c))
