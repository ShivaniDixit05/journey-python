a = 9
b = 8
gmean1 = (a*b)/(a+b)
print(gmean1)
c = 8
d = 7
gmean2 = (c*d)/(c+d)
print(gmean2)

#.......................................

def calculateGmean(a , b):
    mean = (a*b)/(a+b)
    print(mean)        
a = 9
b = 8
calculateGmean(a,b)
if (a > b):
    print("First number is greater")
else:
    print("Second number is greater")
c = 8
d = 7
calculateGmean(c,d)  
if (c > d):
    print("First number is greater")
else:
    print("Second number is greater")    

#.......................................

def calculateGmean(a , b):  # def function_name():
    mean = (a*b)/(a+b)
    print(mean)
def isgreater(a , b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater")
def islesser(a , b):
    pass        
a = 9
b = 8
calculateGmean(a , b)
isgreater(a,b)
c = 8
d = 7
calculateGmean(c,d)
isgreater(c,d)
