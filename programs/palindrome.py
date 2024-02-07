n = int(input("enter the number :"))
x=n
r=0 
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
if x==r:
    print("the number is palindrome") 
else:
    print("the number is not palindrome") 
