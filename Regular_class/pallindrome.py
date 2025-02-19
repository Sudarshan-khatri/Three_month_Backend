def pallindrome(num):
    rev=0
    while num>0:
        dig=(num%10)
        rev=rev*10+dig
        num=num//10
    if(rev==num):
        return True
    else:
        return False



if __name__ == "__main__":
    num=int(input("Enter the number:"))
    check=pallindrome(num)
    if check==True:
        print(f"{num} is pallindrome")
    else:
        print(f"{num} is not pallindrome")