import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
import mysql.connector
import TableColumnProperty

class MySqlConnection(object): 
    config = {
      'user': 'root',
      'password': 'BlueSkittles123',
      'host': '127.0.0.1',
      'database': 'vdb_290',
      'raise_on_warnings': True
    }

    def __init__(self):
        self.cursor = None
        self.cnx = None
        print('init mysql')

    def open_cursor(self):      
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        return self.cursor, self.cnx

    def get_table_description(self, table_name):
        self.open_cursor()
        column_properties = []
        query = "desc {}".format(table_name)
        self.cursor.execute(query)
        for (Field, Type, Null, Key, Default, Extra) in self.cursor:
            column_properties.append(TableColumnProperty.TableColumnProperty(Field, Type))
        self.close_cursor()
        return column_properties

    def close_cursor(self):
        self.cursor.close()
        self.cnx.close()