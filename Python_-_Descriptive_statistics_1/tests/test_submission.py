# Here is where you will add the test cases used to validate the solution.
# The number and style of the test cases can significantly change how well you can evaluate your candidate's solution.
import unittest
from solution import row_count
# Note: the class must be called Test
class Test(unittest.TestCase):

    def test_row_count (self):
      self.assertEqual(row_count(),1460)        