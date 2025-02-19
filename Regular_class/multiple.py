class add:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def two_sum(self):
        self.c=self.num1+self.num2
        return self.c

class sub:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num1=num2
    
    def two_sub(self):
        self.e=self.num1-self.num2 
        return self.e
    
class prod(add,sub):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def two_prod(self):
        self.product=self.num1*self.num2
        return self.product
    


#create an object for class prod
if __name__=="__main__":
    nm1=int(input("Enter first number:"))
    nm2=int(input("Enter second number"))
    product_obj=prod(nm1,nm2)
    print(f"sum of two number:{product_obj.two_sum()}")
    print(f"SUbtraction of two number:{product_obj.two_sub()}")
    print(f"product of two numebr:{product_obj.two_prod()}")


print(type(1))
print(type([]))
print(type(()))
print(type({}))
    