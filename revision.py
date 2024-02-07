'''x=5
y=10
r="renu"
print(x)
print(y)
print(r)          #variables '''

a=5
b= 10
if b > a:
    print ("b is greater than a")


elif a == b:
    print ("a and b are equal")


else:
    print("a is greater than b")    


people = 50
cars = 15
trucks = 20
if cars > people:
    print("We should take the cars.")

elif cars > people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people <trucks:
    print("Alright, let's just take the trucks.")
else:
   print("Fine, let's stay home then.")

  #loops

fruits = ['apples', 'oranges', 'pears', 'apricots']  
for fruit in fruits:
    print('welcome to fruit world')
    print(f"A fruit of type: {fruit}")
the_count = [1, 2, 3, 4, 5,6,7,8,9]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
 

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []


for i in range(0, 9):
    print(f"Adding {i} to the list.")

elements.append(i)


for i in elements:
    print(f"Element was: {i}")



#functions
def my_function(fname):
    print( fname +"welcome to python ")   #creating function


my_function("renu")                      #calling funcation
my_function("pooja")



def add(num1,num2):
    return num1+num2
print( 'the sum is',add (5,6))




def add_num(a,b):
    sum=a+b;
    return sum;
num1 =int(input("input the number one"))
num2= int(input("input the number two"))
print("the sum is",add_num(num1,num2))




#list

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])