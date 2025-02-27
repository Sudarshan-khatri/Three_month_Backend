with open("example.txt","w") as file:
    content=file.write("hello I ma sudarshan khatri")



#example 1
class context_manager():
    def __init__(self):
        print("The 'init' is called ")

    def __enter__(self):
        print("The 'enter' method is called")
        return self
    def __exit__(self,exc_type,exc_value,exc_traceback):
        print("The 'exit' method is called")

with context_manager() as manager:
    print("The 'with' statement is block ")


#create a new file 
try:
    with open("D:\\Three_month_Django\\newfile.txt","w")as file1:
        content=file1.write("Helllo iam sudarshan khatri from kist college ,waiting for the excess of python class")

    with open("D:\\Three_month_Django\\newfile.txt","r") as file2:
        print(file2.read())
except FileNotFoundError:
    print("file not found")



# loop with file 
with open("newfile.txt","r") as file3:
    for x in file3:
        print(x)

with open("newfile.txt","r") as file4:
    print(file4.readline())
    file4.close()


#write the text inside the file:
with open("my_little.txt","a+")as file5:
    data=input("Your story:")
    file5.write(data)


with open("my_little.txt","r") as file6:
    print(file6.read())