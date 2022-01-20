import unittest
import calc 

class TestCalc(unittest.TestCase):

	def test_add(self):
		res= calc.add(10,5)
		self.assertEqual(res, 15)
		self.assertEqual(calc.add(-1,1),0)
		self.assertEqual(calc.add(-1,-1),-2)

	def test_subtract(self):
		res= calc.subtract(10,5)
		self.assertEqual(res, 5)
		self.assertEqual(calc.subtract(-1,1),-2)
		self.assertEqual(calc.subtract(-1,-1),0)

	def test_multiply(self):
		res= calc.multiply(10,5)
		self.assertEqual(res, 50)
		self.assertEqual(calc.multiply(-1,-1),1)
		self.assertEqual(calc.multiply(-1,1),-1)

	def test_divide(self):
		res= calc.divide(10,5)
		self.assertEqual(res, 2)
		self.assertEqual(calc.divide(-1,-1),1)
		self.assertEqual(calc.divide(-1,1),-1)
		self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ =='__main__':
	unittest.main()
