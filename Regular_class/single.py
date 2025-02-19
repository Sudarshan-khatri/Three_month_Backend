class my_info:
    def __init__(self,name,cast,age):
        self.name=name
        self.cast=cast
        self.age=age

    def s_info(self):
        print(f"My name is {self.name} {self.cast}.I am {self.age} years old")


#derived class named info display:
class display_my_info(my_info):
    def __init__(self, name, cast,age,status ):
        super().__init__(name,cast,age)
        self.status=status


    def display(self):
        super().s_info()
        print(f"I am {self.status}")


# create an object of class display_my_info
name=input("Enter the name:")
cast=input("Enter the cast:")
age=int(input("Enter the age:"))
stat=input("Enter the status:")
obj_1=display_my_info(name,cast,age,stat)
obj_1.display()
        