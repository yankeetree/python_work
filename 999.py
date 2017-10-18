import unittest
from salary_plus import Employee

class TestEmpoyee(unittest.TestCase):
	def setUp(self):
		
		self.employee1=Employee('yan','qiang')
		self.employee2=Employee('zhang','xiang',3000)

	def test_give_default_raise(self):
		
		self.assertEqual(str(self.employee1.give_raise()),'5000')

	def test_give_custom_raise(self):
		
		self.assertEqual(str(self.employee2.give_raise(3000)),'3000')

unittest.main()

