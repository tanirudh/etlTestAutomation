import unittest
import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../dbvalidation')))
import table_ddl_validation_service
from DbConnectionFactory import DbConnectionFactory
import HtmlTestRunner

REL_PATH = 'resources/testdata.csv'
HTML_REPORT_DIR = abspath(join(dirname(__file__), './html_report'))

class TestTableDefinition(unittest.TestCase):
    def test_loading_of_csv_file(self):
        column_properties=table_ddl_validation_service.load_csv_data(build_file_path(REL_PATH))
        self.assertEqual(len(column_properties), 17)

    def test_describe_table(self):
        error_messages = []
        dbfactory = DbConnectionFactory()
        dbConnection = dbfactory.getDbConnectionClass(DbConnectionFactory.Dbs.MYSQL)
        db_table_column_properties = dbConnection.get_table_description('appIdInfo_master')
        resource_file_column_properties=table_ddl_validation_service.load_csv_data(build_file_path(REL_PATH))
        for c in resource_file_column_properties:
            new_list = list(filter(lambda x: x.column_name==c.column_name, db_table_column_properties))
            if(len(new_list) != 1):
               error_messages.append('Did not find {} in the resource file'.format(c.column_name))
            else:
                x = new_list[0]
                if (new_list[0] != c):
                    error_messages.append('For "{}" expected type to be "{}" but found "{}"'.format(c.column_name, c.column_type, x.column_type))
        self.assertTrue(len(error_messages) == 0, error_messages)

def build_file_path(relative_path):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, relative_path)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=HTML_REPORT_DIR))