import csv
import dbconstants
from typing import List


class DBLoader:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def load_the_database(self):
        """
        This function will use a csv reader to load in csv data from a file in data/ and load the data
        into a database of my choosing. To start we're looking at postgres
        :param path_to_file: the fully qualified (or relative path) to the csv we're trying to read in
        :return: success or failure of the database being read in (true - success, false - failure
        """
        insert_statements: List[str] = self.get_insert_statements()
        for s in insert_statements:
            print(s)


    def get_insert_statements(self) -> List[str]:
        statements : list[str] = []
        with open(self.path_to_file) as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                statements.append("INSERT INTO " + dbconstants.TABLE_NAME + \
                    " (band, date, venue) " + \
                    " VALUES ('%s', '%s', '%s')" % (tuple(row[0:3])))
        return statements



if __name__ == '__main__':
    dbl = DBLoader("../data/shows_2.23.2020.csv")
    dbl.load_the_database()
