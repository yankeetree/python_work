import unittest
from city_functions import city_country

class FullNameTestCase(unittest.TestCase):
	def test_city_country(self):
		full_name=city_country('santiago','chile',50000)
		self.assertEqual(full_name,'Santiago,Chile-Population=50000')

unittest.main()