from colorama import Fore


def my_name():
    row=6
    column=6
    for i in range(0,row):
        for j in range(0,column):
            #condition for "s"
            if(i==0 or i==3 or i==5) or (j==0 and i<3)or (j==5 and i>=3):
                print(Fore.RED+"*",end="")
            else:
                print(" ",end="")
        print("")

    #print the "U character in  star pattern":
    for i in range(0,row):
        for j in range(0,column):
            # condtion for "U" character
            if (j==0 and i<6) or (j==5 and i<6) or (i==5 and j<6):
                print(Fore.BLUE+"*",end="")
            else:
                print(" ",end="")
        print("")
    #print "D" character in star pattern
    for i in range(0,row):
        for j in range(0,column):
            # condtion for "D" character
            if (i==0 and j<6) or(j==0 and i<6) or(i==5 and j<6) or(j==5 and i<6):
                print(Fore.YELLOW+"*",end="")
            else:
                print(" ",end="")
        print("")
    
    #print "A" character in star pattern
    for i in range(0,row):
        for j in range(0,column):
            # condtion for "A" character
            if (i==3)or (j==0 and i>2) or(j==5 and i>2)or(i==1 and j==1)or(i==0 and j==2)or(i==1 and j==3)or(i==2 and j==4):
                print(Fore.GREEN+"*",end="")
            else:
                print(" ",end="")
        print("")

    
    #print "R" character in star pattern
    for i in range(0,row):
        for j in range(0,column):
            # condtion for "R" character
            if(j==0 and i<6)or (i==0 and j<4)or(j==3 and i<4)or(i==3 and j<4)or(i==4 and j==4)or(i==5 and j==5):
                print(Fore.MAGENTA+"*",end="")
            else:
                print(" ",end="")
        print("")

    #print "H" character in star pattern
    for i in range(0,row):
        for j in range(0,column):
            # condtion for "H" character
            if(j==0 and i<6)or (j==5 and i<6)or(i==3 and j<6):
                print(Fore.CYAN+"*",end="")
            else:
                print(" ",end="")
        print("")
    

    #print "N" character in star pattern
    for i in range(0,row):
        for j in range(0,column):
            # condtion for "N" character
            if(j==0 and i<6)or (j==5 and i<6)or(i==1 and j==1)or(i==2 and j==2)or(i==3 and j==3)or(i==4 and j==4):
                print(Fore.BLACK+"*",end="")
            else:
                print(" ",end="")
        print("")
    



if __name__=="__main__":
    my_name()
