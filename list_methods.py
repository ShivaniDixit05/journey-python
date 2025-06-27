l = [3 , 23 , 5, 25 , 2 , 21 , 7 , 23]
print(l)

l.append(69) #append(value) put the values at the end of the list
print(l)

l.sort()  #sort() arrange the list in ascending order
print(l)
l.sort(reverse = True) # it willarrange the list in descending order
print(l)

print(l.index(25))
print(l.count(23))

m = l.copy()
m[0] = 0
print(l)

l.insert(1 , 899)   #899 ki list me index 1 hogi
print(l)

m = [200 , 56, 35 , 22]
l.extend(m)    #open m and put m at the end of the l
print(l)

k = l + m  #merge the list
print(k)


# methods of lists are:
# append()
# sort()
# copy()
# extend()
# insert()
# index()
# count() 
