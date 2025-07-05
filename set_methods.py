s1 = {2 , 3 , 5 , 6 , 3}
s2 = {3 , 8 , 9}
print(s1.union(s2))
print(s1 , s2)

s1.update(s2)   # values of s2 are updated in s1
print(s1 , s2)  

#The union() method returns a new set whereas update() method adds item into the existing set from another set.

# ---Union--- [A U B]

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.union(cities2)
print(cities3)

# ---union_Update---

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.update(cities2)
print(cities)

# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

# ---Intersection--- [A int B]

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.intersection(cities2)
print(cities3)

# ---INtersection_Update--- 

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.intersection_update(cities2)
print(cities)

# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets

# ---symmetric_difference--- [(A U B) - (A int B)]

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# ---Symmetric_difference_update---

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.symmetric_difference_update(cities2)
print(cities)

# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 

# ---difference---  [A-B]

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.difference(cities2)
print(cities3)

# ---difference_update---

cities = {"Jaipur" , "Udaipur" , "Jaisalmer" , "Jodhpur"}
cities2 = {"Kota" , "Jaisalmer" , "Ajmer"}
cities3 = cities.difference_update(cities2)
print(cities)

# ---isdisjint--- [A not intersection B]

# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)
print(cities3) # false

cities = {"Tokyo1", "Madrid1", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)
print(cities3) # true

# ---issuperset---

# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

cities = {"Seoul" , "Tokyo" , "Berlin" , "Amer"}
cities2 = {"Tokyo" , "Seoul"}
cities3 = cities.issuperset(cities2)
print(cities3)  # true

cities = {"Seoul" , "Tokyo" , "Berlin" , "Amer"}
cities2 = {"Kabul" , "Ajmer"}
cities3 = cities.issuperset(cities2)
print(cities3)  # false

#---issubset---

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
cities2 = {"Ajmer" , "Kota"}
cities3 = cities2.issubset(cities)
print(cities3)

#---ADD---

# add only takes one argument

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
cities.add("Udaipur")
print(cities)

#---update---

#update can add more than one item at a time

cities = {"Udaipur" , "Rajsamand" , "Ajmer"}
cities2 = {"Jabalpur" , "Panna" , "Ajaygarh"}
cities3 = cities.update(cities2)
print(cities)

#---Remove/Disacrd---

# , if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
cities.remove("Bundi")
print(cities)

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
cities.remove("Banswara") # throws an error
cities.discard("Banswara")  # skip the error and continue to execute the code
print(cities)

#---pop()---

# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
item =cities.pop()
print(cities)
print(item)

#---del()---

# del is not a method, rather it is a keyword which deletes the set entirely.

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
del cities
print(cities)

# What if we don’t want to delete the entire set, we just want to delete all items within that set?

#---clear()---

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
cities.clear()
print(cities)

cities = {"Jaisalmer" , "Ajmer" , "Kota" , "Bundi" , "Jodhpur"}
if "Kota" in cities:
    print("Yes it is!")
else:
    print("Nope!!!!!")    
