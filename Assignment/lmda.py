"""Lambda function:small anonymous function 
 syntax:
   lambda arguments:expression"""
# double=lambda x:x*2
# print(double(5))


# with function:
def get_sum():
    t_sum=lambda x,y:x+y
    return t_sum

if __name__=="main":
    num1=int(input("First number:"))
    num2=int(input("Second number:"))
    r_sum=get_sum(t_sum(num1,num2))
    print(f"Sum:{r_sum}")