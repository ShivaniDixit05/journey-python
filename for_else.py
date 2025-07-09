# else will be execute after the loop is successfully finished

for i in range(6):
    print(i)
else:
    print("Sorry no i")    

# else condition will not executed because of break

for i in range(5):
    print(i)
    if i == 4:
     break
else:
    print("Sorry no i")   # else does not execute


i = 0
while i < 7:
   print(i)
   i = i + 1
   if i == 4:
      break
else:
   print("sorry no i")   


for x in range (5):
    print("iteration no {} in forloop".format(x+1))
else:
    print("else block in loop")    
print("Out of loop")    
