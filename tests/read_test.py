import unittest
import sys
sys.path.append(".")
from src.read_data import ReadPerCapitaFile, ReadCurrencyCode

PER_CAPITA_FILE_PATH = 'per_capita_income_data.csv'

class TestPoint(unittest.TestCase):

    def test_per_capita_file(self):
        country_name = 'Poland'
        k = ReadPerCapitaFile(country_name)
        k.open_per_capita_data_file()
        k.read_per_capita_data_file()
        self.assertEqual(k.iterate_on_rows(), '4578')
        k.close_files()

        country_name = 'Iran'
        k = ReadPerCapitaFile(country_name)
        k.open_per_capita_data_file()
        k.read_per_capita_data_file()
        self.assertEqual(k.iterate_on_rows(), '3115')
        k.close_files()

    def test_currency_file(self):
        country_name = 'Poland'
        k = ReadCurrencyCode(country_name)
        k.open_currency_data_file()
        k.read_currency_data_file()
        self.assertEqual(k.iterate_on_rows(), 'PLN')
        k.close_files()

        country_name = 'Australia'
        k = ReadCurrencyCode(country_name)
        k.open_currency_data_file()
        k.read_currency_data_file()
        self.assertEqual(k.iterate_on_rows(), 'AUD')
        k.close_files()

        country_name = 'Iran'
        k = ReadCurrencyCode(country_name)
        k.open_currency_data_file()
        k.read_currency_data_file()
        self.assertEqual(k.iterate_on_rows(), 'IRR')
        k.close_files()

if __name__ == "__main__":
    unittest.main()

