num = int(input("Enter a number: "))

factorial=1

if num < 1:
   print("Sorry, factorial does not exist ")     
elif num == 0:
   print("The factorial of")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)