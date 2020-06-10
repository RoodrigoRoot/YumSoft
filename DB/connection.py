##########################################################################
#   This file contains the data and connection to DB                     # 
#   I use multiple constants to assign value from a file                 #
#   Date: Jun 9 2020                                                     #
##########################################################################


from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import json
from logger import logger
import DB.constants as ct

def get_parameters_db():
    """This Method is for set value the constants from a file config"""
    file = "Yum.config.json"
    with open(file, "r") as f:
        text = json.loads(f.read())
    ct.DB_DATABASE = text["db"]
    ct.DB_PASSWORD = text["password"]
    ct.DB_USER = text["user"]
    ct.DB_HOST = text["server"]
    ct.DB_TYPE_DB = text["type_db"]


def connection_DB():
    try:
        """Set connection db to DB_CONNECTION and return connection"""
        get_parameters_db()      
        ct.DB_CONNECTION = QSqlDatabase.addDatabase("QPSQL")
        ct.DB_CONNECTION.setHostName("localhost")
        ct.DB_CONNECTION.setUserName("rod")
        ct.DB_CONNECTION.setPassword("forever11")
        ct.DB_CONNECTION.setDatabaseName("dbpos")
        if ct.DB_CONNECTION.open():
            return ct.DB_CONNECTION
        return False
    except Exception as e:
        logger.debug(e)

if __name__ == "__main__":
    connection_DB()