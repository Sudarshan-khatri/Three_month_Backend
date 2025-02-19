class parentdemo:
    def __init__(self,messg):
        self.messg=messg

    def message(self):
        print(self.messg)


class childemo(parentdemo):
    def __init__(self, messg,about):
        super().__init__(messg)
        self.about=about

    def childinfo(self):
        print(self.about)


obj1=childemo("sorry","sssss")
obj1.childinfo()