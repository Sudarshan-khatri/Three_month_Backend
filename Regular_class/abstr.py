from abc import ABC, abstractmethod


class animal(ABC):
    @abstractmethod
    def make_sound(self):
        return "I am animal ,i make sound"

class dog(animal):
    def make_sound(self):
       return "Woof Woof"
    
class cat(animal):
    def make_sound(self):
        return "myau myau"
    

obj1=[cat(),dog()]
for obj in obj1:
    print(obj.make_sound())
