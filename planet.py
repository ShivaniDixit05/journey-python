Earth_Weight = float(input("Enter your the Earth weight : "))
palnet_number = int(input("Enter the planet number(1-7) : "))

if palnet_number == 1:
  relative_gravity = 0.38
  destination_weight = Earth_Weight * relative_gravity
  print(destination_weight)
elif palnet_number == 2:
  relative_gravity = 0.91
  destination_weight = Earth_Weight * relative_gravity 
  print(destination_weight)
elif palnet_number == 3:
  relative_gravity = 0.38
  destination_weight = Earth_Weight * relative_gravity
  print(destination_weight) 
elif palnet_number == 4:
  relative_gravity = 2.53
  destination_weight = Earth_Weight * relative_gravity
  print(destination_weight)
elif palnet_number == 5:
  relative_gravity = 1.07
  destination_weight = Earth_Weight * relative_gravity
  print(destination_weight)      
elif palnet_number == 6:
  relative_gravity = 0.89
  destination_weight = Earth_Weight * relative_gravity 
  print(destination_weight)
elif palnet_number == 7:
  relative_gravity = 1.14
  destination_weight = Earth_Weight * relative_gravity
  print(destination_weight)
else:
  print("You entered Invalid planet number")     
