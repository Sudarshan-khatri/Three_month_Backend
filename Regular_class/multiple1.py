#class to define the my breakup story:
class my_story:
    def __init__(self,name,status,reason):
        self.name=name
        self.status=status
        self.reason=reason

    def my_intro(self):
        return f"My name is {self.name} .I am not in {self.status} due to another {self.reason}"
    

#class to define the  of her crush
class ex_story:
    def __init__(self,name,status,reason):
        self.name=name
        self.status=status
        self.reason=reason

    def ex_intro(self):
         return  f"My name is {self.name} .I am not in {self.status} due to another {self.reason}"
    

#class to define the ex
class my_ex(my_story,ex_story):
    def __init__(self, name, status, reason):
        super().__init__(name,status,reason)

    def ex(self):
        print(super().my_intro())
        print(super().ex_intro())



#creates an object for class my_ex:
name1=input("Enter the name:")
status1=input("Enter the status:")
reason1=input("Enter the reason:")

obj1=my_ex(name1,status1,reason1)
obj1.ex()