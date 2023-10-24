from multiply import*
import unittest
class unittesting(unittest.TestCase):
    def test1(self):
        self.assertEqual(multiply(3,5),15)
    def test2(self):
        self.assertEqual('abc'.islower())
if __name__=="__main__":
    unittest.main()
