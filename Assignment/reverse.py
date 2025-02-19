def reverse(number):
    rev=0
    while number>0:
        mod=number%10
        rev=rev*10+mod
        number=number//10
    return rev

if __name__=="__main__":
    num=int(input("Enter the number:"))
    is_reverse=reverse(num)
    print(f"Reverse {num} is {is_reverse}")