import unittest
import unittest.mock as mock
from unittest.mock import patch
from load_db import DBLoader


class TestLoadDB(unittest.TestCase):
    def test_constructor_expected(self):
        # Function should only take a file path (string)
        # test expected functionality
        assert "abc" == DBLoader("abc").path_to_file

    def test_constructor_not_string(self):
       with self.assertRaises(TypeError):
           DBLoader(123)


    # #TODO: Finish this function
    # def test_load_the_database(self, mocker):
    #     mocker.patch('DBLoader.get_insert_statements()')
    #     assert()

    def test_get_insert_statements_correct(self):
        expected_list = ["INSERT INTO shows (band, date, venue)  VALUES ('The Strokes', '8/1/2019', 'Lollapalooza 2019 D1')"]
        with mock.patch('builtins.open', mock.mock_open(read_data= "a,b,c\nThe Strokes,8/1/2019,Lollapalooza 2019 D1")):
            assert expected_list == DBLoader("abc").get_insert_statements()

    def test_get_insert_statements_incorrect_not_enough_columns(self):
        with self.assertRaises(TypeError):
            with mock.patch('builtins.open',
                mock.mock_open(read_data="a,b\nThe Strokes,8/1/2019")):
                print(DBLoader("abc").get_insert_statements())