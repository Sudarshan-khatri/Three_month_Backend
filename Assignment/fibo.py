def fibonacci(number):
    if(number==0):
        return 0
    elif(number==1):
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

if __name__=="__main__":
    num=int(input("Number to find the fibonacci series:"))
    for i in range(num):
        fibo=fibonacci(i)
        if(fibo==0):
            print(fibo)
        elif(fibo==1):
            print(fibo)
        else:
            print(fibo)