import unittest
import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../dbvalidation')))
import table_ddl_validation_service
import db_service
import HtmlTestRunner

REL_PATH = 'resources/testdata.csv'
HTML_REPORT_DIR = './html_report'

class TestTableDefinition(unittest.TestCase):
    def test_loading_of_csv_file(self):
        column_properties=table_ddl_validation_service.load_csv_data(build_file_path(REL_PATH))
        self.assertEqual(len(column_properties), 17)

    def test_describe_table(self):
        db_table_column_properties=db_service.get_table_description('appIdInfo_master')
        resource_file_column_properties=table_ddl_validation_service.load_csv_data(build_file_path(REL_PATH))
        for c in resource_file_column_properties:
            new_list = list(filter(lambda x: x.column_name==c.column_name, db_table_column_properties))
            self.assertTrue(len(new_list) == 1, 'Did not find {} in the resource file'.format(c.column_name))
            x = new_list[0]
            self.assertTrue(new_list[0] == c, 'For "{}" expected type to be "{}" but found "{}"'.format(c.column_name, c.column_type, x.column_type))
        self.assertTrue(set(db_table_column_properties) == set(resource_file_column_properties))

def build_file_path(relative_path):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, relative_path)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=HTML_REPORT_DIR))