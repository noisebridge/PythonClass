def func():
	return 'something'


class Integer(object):

	def __init__(self, value=None):
		self.value = value

	def add_value(self, value):
		self.value = value

	def convert_val_to_str(self):
		self.value = self.__str__()

	def con_val_to_str(self):
		self.value = str(self.value)

	def con_to_str(self):
		return str(self.value)







intgr = Integer(10)
