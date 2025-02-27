myList=[1,3,4,56,"banana",'mango',"schedule"]
myit=iter(myList)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#iterable for string 
my_string="banab globala"
myb=iter(my_string)

print(next(myb))
print(next(myb))
print(next(myb))
print(next(myb))
print(next(myb))
print(next(myb))



#using loop 
myList1=[1,3,4,56,"banana",'mango',"schedule"]
for item in myList1:
    print(item)


#using class 
class myNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
    
myclass=myNumber()
myiter=iter(myclass)

for x in myiter:
    print(x)


#global keyword:

x=300
def myfunc():
    global x
    x=200
myfunc()
print(x)

#use nonlocal
def myfunc1():
    x="jone"
    def myfunc2():
        nonlocal x
        x="hello"
    myfunc2()
    return x
print(myfunc1())


