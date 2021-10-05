from csv import reader
import numpy as np
from forex_python.converter import CurrencyRates



PER_CAPITA_FILE_PATH = 'per_capita_income_data.csv'
CURRENCY_CODES_FILE_PATH = 'currency_codes.csv'

class ReadPerCapitaFile():

    def __init__(self, country):
        self.country = country
        self.title_country = self.country.title()

    def open_per_capita_data_file(self):
        self.per_capita_data_file = open(PER_CAPITA_FILE_PATH)
        return self.per_capita_data_file

    def read_per_capita_data_file(self):
        self.per_capita_data_file_read = reader(self.per_capita_data_file)
        return self.per_capita_data_file_read

    def iterate_on_rows(self):
        for row in self.per_capita_data_file_read:
            if self.title_country in row:
                # print(row[2])
                return row[2]
            for i in row:
                if self.title_country in i:
                    # print(row[2])
                    return row[2]
    def close_files(self):
        self.per_capita_data_file.close()


class ReadCurrencyCode():

    def __init__(self, country):
        self.country = country
        self.upper_country = self.country.upper()

    def open_currency_data_file(self):
        self.currency_data_file = open(CURRENCY_CODES_FILE_PATH)
        return self.currency_data_file

    def read_currency_data_file(self):
        self.currency_data_file_read = reader(self.currency_data_file)
        return self.currency_data_file_read

    def iterate_on_rows(self):
        for row in self.currency_data_file_read:
            if self.upper_country in row:
                # print(row[2])
                return row[2]
            for i in row:
                if self.upper_country in i:
                    # print(row[2])
                    return row[2]

    def close_files(self):
        self.currency_data_file.close()



c = CurrencyRates()

# print(c.get_rate('USD', 'GBP'))

class StartProgram():

    def __init__(self):
        user_input = input('Write your country: ')

        get_per_capita_value = ReadPerCapitaFile(user_input)
        get_per_capita_value.open_per_capita_data_file()
        get_per_capita_value.read_per_capita_data_file()
        per_capita = get_per_capita_value.iterate_on_rows()
        get_per_capita_value.close_files()

        get_currency_code = ReadCurrencyCode(user_input)
        get_currency_code.open_currency_data_file()
        get_currency_code.read_currency_data_file()
        currency = get_currency_code.iterate_on_rows()
        get_currency_code.close_files()

        c = CurrencyRates()
         
        rate = c.get_rate('USD', currency)
        final = rate * float(per_capita)
        print(f'Your country per capita is {per_capita} USD and the currency is {currency}, so the per capita in your currency is: {final}.')




if __name__ == "__main__":
    start = StartProgram()