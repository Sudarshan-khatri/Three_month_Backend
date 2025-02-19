"""Bank Management system: """
"""1: First task to create account
    2:Login system
    3:check balance 
    4:Deposit balance
    5:withdraw balance
    6:
    """



import random
from  colorama  import Fore,Style

# simple user interface for bank management system 
print("\t \n\n\t\t\t"+Fore.GREEN+"SUDARSHAN BANK OF ROYALAND"+Style.RESET_ALL)
name=input("Enter the name:")
print("\t \n\t\t\t"+Fore.CYAN+f"WELCOME {name.upper()}!!!"+Style.RESET_ALL)

def create_account():
    account_list=[1,2,3,4,5,6,7,8,9,0]
    digit=(random.sample(account_list,8))
    account_number = "".join(map(str, digit))
    print(account_number)

# class to create new account in the bank
class signup_account:
    def __init__(self,user_name,password,rematch_password):
        self.user_name=user_name
        self.password=password

if __name__=="__main__":
    create_account()