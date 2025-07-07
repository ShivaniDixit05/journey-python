emp_info = {"name" : "Siya" , "Age" : 19 , "Gender" : "Female"}
print(emp_info)

# Access a single info
print(emp_info["Age"])

employee_id = [
                {"Name" : "Shivani" , "Age" : 19 , "ID" : 21},
                {"Name" : "Shubham" , "Age" : 20 , "ID" : 22},
                {"Name" : "Siddhi"  , "Age" : 20 , "ID" : 23},
                {"Name" : "Mitarth" , "Age" : 21 , "ID" : 24},
                {"Name" : "Raghav"  , "Age" : 20 , "ID" : 25},
]

for employee in employee_id:
    print(employee["Name"])
    print(employee["Age"])
    print(employee["ID"])

info = {"Name" : "Shivani" , "Standard" : 2 , "Age" : 19 , "ID" : 345}
print(info)
print(info["Name"])
print(info.get("Name"))

# They both are same but the difference is:

# print(info["Name1"])      # It throws an error
print(info.get("Name1"))  # give none as an output

# Access the multiple values

info = {"Name" : "Shivani" , "Standard" : 2 , "Age" : 19 , "ID" : 345}
print(info)
print(info.keys())  #access all the values of the dict
# 2 ways to access value 
#1)
print(info.values())

# 2)
for key in info.keys():
    print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")

info = {"Name" : "Shivani" , "Standard" : 2 , "Age" : 19 , "ID" : 345}
print(info.items())

for key , value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
