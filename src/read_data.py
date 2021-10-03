from csv import reader
import numpy as np

FILE_PATH = 'per_capita_income_data.csv'

class ReadDataFrame():

    def __init__(self, country):
        self.country = country

    def open_data_file(self):
        self.data_file = open(FILE_PATH)
        return self.data_file

    def read_data_file(self):
        self.data_file_read = reader(self.data_file)
        return self.data_file_read

    def iterate_on_rows(self):
        for row in self.data_file_read:
            if self.country in row:
                # print(row[2])
                return row[2]

    def close_files(self):
        self.data_file.close()

class StartProgram():

    def __init__(self):
        user_input = input('Write your country: ')

        program = ReadDataFrame(user_input)
        program.open_data_file()
        program.read_data_file()
        program.iterate_on_rows()

        program.close_files()


if __name__ == "__main__":
    start = StartProgram()