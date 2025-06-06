height = int(input("Enter your height :"))
credits = int(input("Enter your credits :"))

if height >= 137 and credits >= 10:
  print("ENJOY YOUR RIDE!")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")  
else:
  print("you do not have either requirements")  
