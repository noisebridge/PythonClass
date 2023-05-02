import random

class Cat(object):

	#import random
	enemies = 5

	def __init__(self, name=None, top_speed=9223372036854775808L, cat=None, hunger=None, food=None):

		self.name = name
		self.top_speed = top_speed
		self.hunger = random.randint(1,10)
		self.food = []
		self.at_vet = False

	#if self.hunger >= 10:
	#	return "cat at vet: {}".format(self.at_vet=True)


	def change_name(self, name):
		self.name = name 

	def __str__(self):
		return "this is a cat named {0} and has attributes {1}" \
				.format(self.name, self.__dict__)

	def chase_bird(self):
		self.hunger += 1
		if self.hunger >= 10:
			self.at_vet=True
			return "cat at vet: {}".format(self.at_vet)


	def catch_bird(self):
		if random.randint(1,2) == 1:
			self.food.append(2)
		else:
			print("the bird flew away")

	def eat(self):
		self.hunger -= self.food.pop()



cat = Cat()