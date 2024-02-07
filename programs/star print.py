num = int(input("enter the number row:"))
for i in range(0,num):
    for j in range (0,num-i):
        print("",end="")
    for k in range (0,i+1):
        print("*",end="")  
    print("")  