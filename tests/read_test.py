import unittest
import sys
sys.path.append(".")
from src.read_data import ReadDataFrame

FILE_PATH = 'per_capita_income_data.csv'

class TestPoint(unittest.TestCase):

    def test_same(self):
        country_name = 'Poland'
        k = ReadDataFrame(country_name)
        self.assertEqual(k.iterate_on_rows(), '4578')


if __name__ == "__main__":
    unittest.main()
    
