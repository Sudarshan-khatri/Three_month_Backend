from abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract method"
        return 
    
class circle(shape):
    def draw(self):
        super().draw()
        print("Draw the circle")
        return 
    
class rectangle(shape):
    def draw(self):
        super().draw()
        print("Draw a rectangle")
        return
    

shapes=[circle(),rectangle()]
for i in shapes:
    i.draw()


#method overriding

class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'vector (%d ,%d)'%(self.a,self.b)
    
    def  __add__(self,other):
        return vector(self.a+other.a,self.b+other.b)
    
v1=vector(2,10)
v2=vector(5,-2)
print(v1+v2)



#method overloading 
class sum:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def sum_2(self):
        sum1=self.a+self.b
        return sum1
    
    def sum_2(self):
        sum=self.a+self.b+self.c
        return sum
    

#create an object for class sum
sum_1=sum(1,2,3)
print(sum_1.sum_2())
print(sum_1.sum_2())


#method overriding
class parent:
    def mymethod(self):
        print("I am paremt")

class child(parent):
    def mymethod(self):
        print("calling child method")

#create an object of class child
obj1=child()
obj1.mymethod()



#class employeee problem
class Employee:
    def __init__(self,nm,sal):
        self.nm=nm
        self.sal=sal

    def getName(self):
        return self.nm
    def getSalary(self):
        return self.sal
    
class Salesofficer(Employee):
    def __init__(self, nm,sal,inc):f
        super().__init__(nm,sal)
        self.inc=inc

    def getSalary(self):
        return self.sal + self.inc
    
# create an objet 
e1=Employee("Rajesh",9000)
print("Total salary for {} is RS {}".format(e1.getName(),e1.getSalary()))
s1=Salesofficer("Kiran",10000,1000)
print("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))