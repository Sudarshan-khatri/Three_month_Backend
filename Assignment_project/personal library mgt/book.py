#This program to use to enter the book list in file ,update the books and delete the book in the system.

import json
import datetime


class add_book:
    def __init__(self,title,author,year,version):
        self.title=title
        self.author=author
        self.year=year
        self.version=version

    def add_book_in_file(self):
        try:
            data={
                "title":self.title,
                "author":self.author,
                "year":self.year.strftime("%x"),
                "version":self.version
            }
            with open("book_data.json","a") as file1:
                json.dump(data,file1)
                file1.write("\n")
            print("data stored in json file")
            
        except FileNotFoundError:
            print("Data not stored in file")


class delete_book(add_book):
    pass

class update_book(delete_book):
    pass



if __name__=="__main__":
    Book_title=input("Enter the book_title:")
    Book_author=input("Enter the book author:")
    x=datetime.datetime.now()
    print(x.strftime("%x"))
    Book_version=input("Enter the book version:")
    obj1=add_book(Book_title,Book_author,x,Book_version)
    obj1.add_book_in_file()

