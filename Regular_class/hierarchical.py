class manager:
    def __init__(self,name,status):
        self.name=name
        self.status=status

    def manager_info(self):
        return self.name,self.status
    

class employee(manager):
    def __init__(self, name, status,age):
        super().__init__(name, status)
        self.age=age

    def emp_info(self):
        print(f"Employee name:{self.name}")
        print(f"Employee status:{self.status}")
        print(f"Age of employee:{self.age}")

class customer(manager):
    def __init__(self,name,status,age):
        self.name=name
        self.status=status
        self.age=age

    def customer_info(self):
        print(f"Customer name:{self.name}")
        print(f"customer")

       
        