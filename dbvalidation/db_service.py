import mysql.connector
import TableColumnProperty

config = {
  'user': 'root',
  'password': 'BlueSkittles123',
  'host': '127.0.0.1',
  'database': 'vdb_290',
  'raise_on_warnings': True
}

def open_cursor():      
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    return cursor, cnx

def get_table_description(table_name):
    column_properties = []
    cursor, cnx = open_cursor()
    query = "desc {}".format(table_name)
    cursor.execute(query)
    for (Field, Type, Null, Key, Default, Extra) in cursor:
        column_properties.append(TableColumnProperty.TableColumnProperty(Field, Type))
    close_cursor(cursor, cnx)
    return column_properties
    
def close_cursor(cursor, cnx):
    cursor.close()
    cnx.close()