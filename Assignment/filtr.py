ages=[2,5,8,18,23,67,89]

def my_ages(x):
    if x<18:
        return True
    else:
        return False
    

adults=filter(my_ages,ages)
for x in adults:
    print(x)