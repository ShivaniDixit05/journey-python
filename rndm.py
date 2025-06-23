import random

total = 0

while total != 2:
  die1 = random.randint(0,6)
  die2 = random.randint(0,6)
  print("Nope")
  
  total = die1 + die2

  if total == 2:
   print(total)
   print("Snake Eyes")

print("We made it!")    
