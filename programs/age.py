P=int(input("enter your age:"))
if(P>0 and P<12) :
    print("kid")
elif (P>=12 and P<19) :
    print("teenager")
elif(P>19 and P<30) :
    print("young") 
elif (P>30 and P<45) :
    print("mature")  
elif (P>45 and P<60) :
    print("experienced")
elif (P>60 and P<75) :
    print("old")
elif (P>75) :
    print("senior citizen")