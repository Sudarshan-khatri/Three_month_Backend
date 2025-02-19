"""polymorphism : many form """

class Duck:
    def sound(self):
        return "Quack quack!"
    
class AnotherBird:
    def sound(self):
        return "I am soilder"
    
def makesound(Duck):
    print(Duck.sound())


duck=Duck()
anotherbird=AnotherBird()
#calling methods
makesound(duck)
makesound(anotherbird)