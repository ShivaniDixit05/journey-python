# letter = "My name is {} and i am from {}"
letter = "My name is {1} and i am from {0}"
name = "shivani"
country = "India"

# print(letter.format(country , name))  #problem of arrangement
print(letter.format(name , country))
                
            #   *****

name = "Siya"
country = "India"
print(f"Hey! My name is {name} and i am from {country}")




txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.044567999))
            
            # *****

price = 49.04567999
txt = f"For only {price:2f} dollars!"
print(txt)

#Multiplication as a string

multi = f"{ 2 * 30}"          #Print as string
print(type(multi))
print(multi)
