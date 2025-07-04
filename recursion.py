# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)   #callinf the factorial fun under the factorial fun

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))    
print(factorial(4))    
print(factorial(5))    


# HOW IT WORKS :
# Ex:-factorial(5) ? n * factorial(n-1)
# 5 * factorial(4)             else condition
# 5 * 4 * factorial(3)         else condition
# 5 * 4 * 3 * factorial(2)     else condition
# 5 * 4 * 3 * 2 * factorial(1) else coondition
# 5 * 4 * 3 * 2 * 1            if condition


# Fibonacci sequance:  
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8 12 .........

def f(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(4))    
print(f(6))
print(f(8))
