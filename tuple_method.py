countries = ("Spain" , "India" , "England" , "Germany")
temp = list(countries)
temp.append("Russia")    #add item
temp.pop(3)              #remove item
temp[2] = "Finland"      #change item
countries = tuple(temp)
print(countries)

# make a list , perform operations , and again converted that list into tuple

countries1 = ("Paris" , "Bharat" , "America" , "Russia")
countries2 = ("China" , "SouthAfrica" , "Australia")
SouthEastAsia = countries1 + countries2
print(SouthEastAsia)

tuple1 = (0 , 1 , 3 , 5, 9 , 3 , 8 , 1 , 5 , 3)
res = tuple1.count(3)
print("Count of 3 in count1 is :" , res)

tuple2 = (0 , 1 , 3 , 51, 9 , 3 , 8 , 1 , 5 , 3)
res2 = tuple2.index(5)
print("Index of 3 in tuple2 is :" , res2)
res3 = tuple2.index(3 , 4 , 8)  #index(value , start , stop) #3 is a value searching for , 4 starting index , 8 ending index
print("Index of 3 in tuple2 is:" , res3)
res4 = len(tuple2)
print(res4)


#------- Methods of Tuple ------------
#1) Append
#2) Pop
#3) Count()
#4) Index()
#5) 
