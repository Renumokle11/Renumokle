# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p1 = Person('renu')
p2= Person('priya')
p3= Person('rahul')
p1.say_hi()
p2.say_hi()
p3.say_hi()
