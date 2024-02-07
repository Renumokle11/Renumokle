class Calculator:
    def __init__(self):
        pass

    def add(self,numbers):
        return sum(numbers)
        

    def sub(self,numbers):
        return numbers[0]-sum(numbers[1:])
       

    def mul(self,numbers):
        result =1
        for num in numbers:
            result *= num
        return result

    def div(self,numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num !=0:
                result /= num
            else:    
                return "can not divide by zero" 
    
        return result  
     

cal=Calculator ()
operation = input("enter operation (1.add,2.sub,3.mul,4.div):").lower() 




if operation not in ["1.add","2.sub","3.mul","4.div"]:
    print('invalid operation ') 
else:
    numbers=[int(x) for x in input("enter numbres separated by spaces:").split()]


    if operation == "add":
        result= cal.add(numbers)
    elif operation == "sub":
        result= cal.sub(numbers)  
    elif operation == "mul":
        result= cal.mul(numbers) 
    elif  operation =="div":  
        result= cal.div(numbers)

print("Result:",result)
