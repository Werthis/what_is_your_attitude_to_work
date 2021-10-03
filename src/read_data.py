from csv import reader
import numpy as np

FILE_PATH = 'per_capita_income_data.csv'

class ReadDataFrame():

    def __init__(self, country):
        self.country = country

        self.open_data_file()
        self.read_data_file()
        

    def open_data_file(self):
        self.data_file = open(FILE_PATH)
        return self.data_file

    def read_data_file(self):
        self.data_file_read = reader(self.data_file)
        return self.data_file_read

    def iterate_on_rows(self):
        for row in self.data_file_read:
            if self.country in row:
                print(row[2])
                return row[2]
            else:
                pass

            # print(row)
            for element in row:
                pass
                # print(element)

class StartProgram():

    def __init__(self):
        user_input = input('Write your country: ')

        program = ReadDataFrame(user_input)
        program.iterate_on_rows()


if __name__ == "__main__":
    start = StartProgram()