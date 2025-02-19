class bank:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
if __name__=="__main__":
    my_bank=bank(100)
    my_bank.deposit(50)
    print(my_bank.get_balance())
        