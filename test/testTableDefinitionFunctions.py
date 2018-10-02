import unittest
import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../dbvalidation')))
print(abspath(join(dirname(__file__), '../dbvalidation')))
import table_ddl_validation_service

class TestTableDefinition(unittest.TestCase):

    def test_loading_of_csv_file(self):
        script_dir = os.path.dirname(__file__)
        rel_path = 'resources/testdata.csv'
        column_properties=table_ddl_validation_service.load_csv_data(os.path.join(script_dir, rel_path))
        self.assertEqual(len(column_properties), 3)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()