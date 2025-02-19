class Animal:
    def sound(self):
        print("Animal speaks")

class dog(Animal):
    def bark(self):
        print("Bark")


obj1=dog()
obj1.bark()
obj1.sound()


#class shapes
class shapes:
    def __init__(self,no_sides):
        self.n=no_sides
        self.sides=[0 for i in range(no_sides)]
    
    def takesides(self):
        self.sides=[float(input("Enter side"+str(i+1)+":"))for i in range(self.n)]

    def disides(self):
        for i in range(self.n):
            print("sides",i+1,"is",self.sides[i])



class rec(shapes):
    def __init__(self):
        shapes.__init__(self,3)

    
    def findArea(self):
        print(self.sides)
        a=self.sides

        area=(a)*2
        print(f"The area fo the retangle:{area}")

    
# create an objects 
obj1=rec()
obj1.findArea()
obj1.takesides()
obj1.disides()