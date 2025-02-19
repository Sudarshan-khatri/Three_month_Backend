# Local variable 
def l_variable():
    x=20
    print(x)

l_variable()


#Global variable 
x=20
def g_variable():
    x=30
    print(x)

g_variable()



#mutable data types: data type that can be changed 
list=[1,2,3,4,5,'a','b']
list.append(8)
print(list)



#Arithmetic operator 

x=10
x+=5
print(x)

x=x**2
print(x)
x//=3
print(x)


# Logical operator 
has_password=True
has_visa=False

if has_password and has_visa:
    print("I am going to abroad")

elif has_password or has_visa:
    print("I love Nepal")
 
else:
    print("Not going to abroad not love nepal")


#Not :Reverse value
is_raining=True
if not is_raining:
    print("It's sunny")
else:
    print("Today rainning")


# Recursive function :function call by itself is called recursive function
def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*factorial(num-1)


num=int(input("Enter the number:"))
fact=factorial(num)
print(fact)



#pattern printing
"""
*
**
***
****
*****
"""

num=5
for i in range(1,num+1):
    for j in range(0,i):
        print("*",end='')
    print('')

"""
*****
****
***
**
*
"""
print("\n")
star=5
for i in range(1,star+1):
    for j in range(0,star+1-i):
        print("*",end='')
    print('')