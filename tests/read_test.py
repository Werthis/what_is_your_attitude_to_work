import unittest
import sys
sys.path.append(".")
from src.read_data import ReadDataFrame

FILE_PATH = 'per_capita_income_data.csv'

class TestPoint(unittest.TestCase):

    def test_per_capita_file(self):
        country_name = 'Poland'
        k = ReadDataFrame(country_name)
        k.open_data_file()
        k.read_data_file()
        self.assertEqual(k.iterate_on_rows(), '4578')
        k.close_files()

        country_name = 'Iran'
        k = ReadDataFrame(country_name)
        k.open_data_file()
        k.read_data_file()
        self.assertEqual(k.iterate_on_rows(), '3115')
        k.close_files()

if __name__ == "__main__":
    unittest.main()

