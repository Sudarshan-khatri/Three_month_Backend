#class to define the my breakup story:
class my_story:
    def __init__(self,name,status,reason):
        self.name=name
        self.status=status
        self.reason=reason

    def my_intro(self):
        return "My name is "+{self.name} +".I am not in" +{self.status} +"due to another" + {self.reason}
    

#class to define the 