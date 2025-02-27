"""This is the first project of three month backend class using the concept of basic python and 
oop in python .The project tittle is "Personal Library management system" .It has following functionlity
#Adding the Book
#Views the Books
# Search the Books
#Updates the Books
# Delete the books"""

from colorama import Fore
import book as bk



print(Fore.GREEN+"\n\n\t\twelcome personal library management system".upper())
print("\t\t1:Admin".upper())
print("\t\t2:student".upper()+Fore.RESET)
choice=int(input("User status:".upper()))
match choice:
    case 1:
        print("admin")
    case 2:
        print("student")
    

print("\n\n\n\n\n")

