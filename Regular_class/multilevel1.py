class sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum1(self):
        return self.a+self.b
    
class prod(sum):
    def __init__(self, a, b,c):
       super().__init__(a,b)
       self.c=c

    def prod_1(self):
       return (self.a*self.b*self.c)
    
class div(prod):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def div_1(self):
        return super().sum1() + super().prod_1()
        
    
#create an object
num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
num_3=int(input("Enter third number:"))
obj1=div(num_1,num_2,num_3)
print(obj1.div_1())