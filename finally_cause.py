# finally code is always executes even if there is an error

try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation


    
try :
    l = [1 , 4 , 5 ,6]
    i = int(input("Enter the index : "))
    print(l[i])
except:
    print("Some Error occured")
finally:
    print("I am always executed")        

# doubt :- we can use only print("I am always executed") execpt finally what's the problem
# ans :- when we wrap up the code inside the function then it will give us a problem

def fun():
    try:
        l = [1 , 4 , 5 , 6]
        i = int(input("Enter the index : "))
        print(l[i])  
        return 1
    except:
        print("Some Error occured")
        return 0    
    # print("I am always executed") # it will not be executed
    finally:
        print("I am always executed")

x = fun()
print(x)
