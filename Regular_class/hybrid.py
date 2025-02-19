#parent class
class CEO:
    def ceomethod(self):
        print("Iam the CEO")


class manager(CEO):
    def managermethod(self):
        print("Iam the manager")

class employee1(manager):
    def employee1method(self):
        print("Iam the first employee")

class employee2(manager,CEO):
    def employee1method(self):
        print("Iam the second employee")


emp=employee2()
emp.managermethod()
emp.ceomethod()
emp.ceomethod()