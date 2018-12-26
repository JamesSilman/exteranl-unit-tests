# import out unittest library 
import unittest
# import sys to allow us to append the system path
import sys 
# append the parent folder
sys.path.append('../') 
# import out class located in "src" and then in 
from src.sub_folder.test.my_class import MyClass 

class TestMyClass(unittest.TestCase):

	# perform any set up, i.e. create an instance of our example class
	@classmethod
	def setUpClass(self):
		print("Starting Unit Tests")
		global mc
		mc = MyClass()

	# perform any tear down
	@classmethod
	def tearDownClass(self):
		print("Finihsing Unit Tests")

	# test our example method
	def testExampleMethod(self):
		self.assertTrue(mc.exampleMethod(), msg=None)