class cal():
    def addition( self,a, b):
       return a + b

    def subtract( self,a, b):
        return a - b
 
    def multiplication(self,a, b):
        return a * b

    def divide(self,a, b):
        if a!=0:
            return a / b
        else:
             return "can not divide by zero"
        
    def square(a):
        num = int(input("Enter a number: "))
        return num*num
 

    def square_root(a):
        num = int(input("Enter a number: "))
        return num**0.5
         
   
    
cal=cal()

result = cal.addition(3,5)
print("3+5=",result)
result = cal.divide(3,5)
print("3/5=",result)
result = cal.subtract(3,5)
print("3-5=",result)
result = cal.multiplication(3,5)
print("3*5=",result)
result = cal.square()
print(result)
result = cal.square_root()
print(result)
 
 