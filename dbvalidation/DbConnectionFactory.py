from enum import Enum, auto
import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), './dbconnectionclasses')))
from MySqlConnection import MySqlConnection

class DbConnectionFactory(object):            
    class Dbs(Enum):
        MYSQL = auto()
    dbsmap = {
     Dbs.MYSQL: MySqlConnection
    }
    def getDbConnectionClass(self, db_application_name):
        db = self.dbsmap.get(db_application_name, "DB not supported")
        return db()