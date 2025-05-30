#strings are immutable
a = "Harry".upper()
print(a)       #OR

a = "!!! Shivani !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Shivani" , "Siya"))
print(a.split(" "))
print(a.count("i"))

blogHeading = "introducTion tO jS"
print(blogHeading.capitalize())  # capitalize method converts first letter into uppercase and rest other char are change into lowercase

str1 = "Hello guyz , Welcome to our channel"
print(len(str1))
print(str1.center(50,"."))

str2 = "Welcome to console !!!"
print(str2.endswith("!!"))
print(str2.endswith("to", 4 , 10))

str3 = "He's name is Shubham . He is my man. "
print(str3.find("ishh"))   # finds index
# print(str3.index("ishh"))

str4 = "WelcomeToConsole"
print(str4.isalnum())  # including num
print(str4.isalpha())  # num are not including

str5 = "Welcome 05"
print(str5.isalpha())

str6 = "this is shivani"
print(str6.islower())

str7 = "Happy BirthDay\n"
print(str7.isprintable())
print(str7)

strA = "Welcome Ji"
print(strA.istitle())
strB = "This is Awsome"
print(strB.istitle())

str1 = "   "            # soace by using spacebar/Tab
print(str1.isspace())

str2 = "Python is an Interpreted Language"
print(str2.startswith("Python"))

str3 = "heyyyyyy"
print(str3.swapcase())

str4 = "His name is Shubham and i love him"
print(str4.title())
