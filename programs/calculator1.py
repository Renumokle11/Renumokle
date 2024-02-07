class Calculator:

    def addition(self,a,b):
        print("the addition of a and b is:")
        return(a + b)

    def subtraction(self,a,b):
        print("the subtraction of a and b is:")
        return(a - b)

    def multiplication(self,a,b):
        print("the multiplication of a and b is:")
        return(a * b)

    def division(self,a,b):
        print("the division of a and b is:")
        if b!=0:
            return a / b
        else:
            return ("can not divide by zero")
        
            
        
    def square(self):
        print("the square of a is:")
        return(a**2)
 

    def square_root(self,a):
        print("the square_root of a is:")
        if a >= 0:
            return a ** 0.5
        else:
             return "INVALID INPUT FOR SQUARE_ROOT "
        
         

cal = Calculator()

while True:
    print("CALCULATOR")
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    print("5. square")
    print("6. square_root")
    print("7.Exit")

    
    choice=input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    if choice in ('1','2','3','4'):
        a= int(input("Enter first number:"))
        b= int(input("Enter second number:"))

        if choice == '1':
            print(cal.addition(a,b))

        elif choice == '2':
            print(cal.subtraction(a,b))

        elif choice == '3':
            print(cal.multiplication(a,b))
    
        elif choice == '4':
            print(cal.division(a,b))

    elif choice == '5':
        a= int(input("Enter number:"))
        print(cal.square())  

    elif choice == '6':
        a= int(input("Enter number:"))
        print(cal.square_root(a))    
    else:
        print("Invalid choice")