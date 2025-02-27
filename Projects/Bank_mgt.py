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
import json
import re


def validate_email(email):
    pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True
    return False
    

#class to create the accoun of individual customer:
class create_acc():
    def __init__(self,full_name,user_name,password,v_password,email_address,dob):
        self.full_name=full_name
        self.user_name=user_name
        self.password=password
        self.v_password=v_password
        self.email_address=email_address
        self.dob=dob
        #create a function to sign_up the account
    def signup_account(self):
            account_list=[1,2,3,4,5,6,7,8,9,0]
            digit=(random.sample(account_list,8))
            account_number = "".join(map(str, digit))
            print(account_number)
            try:
                data= {
                        "full_name":self.full_name,
                        "user_name":self.user_name,
                        "password":self.password,
                        "ver_pass":self.password,
                        "email_address":self.email_address,
                        "dob":self.dob,
                        "account_number":account_number
                    }
                with open("user_data.json","a") as file:
                        json.dump(data,file)
                        print("\n")
                        print("Data stored sucessfully")
            except:
                print("data not stored in file")


if __name__=="__main__":
    print("\t \n\n\t\t\t"+Fore.GREEN+"SUDARSHAN BANK OF ROYALAND"+Style.RESET_ALL)
    print("\n\n\t\t\t1:create account".upper())
    print("\t\t\t2:check balance".upper())
    print("\t\t\t3:Deposit balance".upper())
    print("\t\t\t5:withdraw balance".upper())
    choice=int(input("Choose the option:"))
    match choice:
        case 1:
            #instance of class create account
            f_name=input("Account_holder Full_name:")
            u_name=input("Account User_name:")
            pass_key=input("Account password:")
            v_pass=input("Verify_password:")
            Email_add=input("Email address:")
            if validate_email(Email):
                pass
            db=input("Date of birth:")
            user_account=create_acc(f_name,u_name,pass_key,v_pass,Email_add,db)
            user_account.signup_account()