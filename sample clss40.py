# Python3 program to
# demonstrate instantiating
# a class
class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
   # with self parameter
class GFG:
	def __init__(self, name, company):
		self.name = name
		self.company = company

	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" work in "+self.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()



# with another parameter

#class
class GFG:
	def __init__(somename, name, company):
		somename.name = name
		somename.company = company
# A sample method
	def say_hi(somename):
		print("Hello my name is " + somename.name +
			" and I working in "+somename.company+".")


obj = GFG("Renu", "Ring")
obj.say_hi()          #method through objects
