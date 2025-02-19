def factorial(number):
    if(number==0):
        return 1
    elif(number==1):
        return 1
    else:
        return number*factorial(number-1)

if __name__=="__main__":
    while True:
        num=int(input("Number to find factorial:"))
        fact=factorial(num)
        if(fact==1):
            print(f"Factorial:{fact}")
        else:
            print(f"Factorial:{fact}")