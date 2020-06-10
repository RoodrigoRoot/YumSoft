from logger import logger
from PyQt5.QtSql import QSqlQuery
import DB.constants as ct

class LoginMethods:

    @staticmethod
    def access_system(line_edit):
        """Method for access to system
        Only ask fot the password  """
        try:
            if ct.DB_CONNECTION.open():
                passwd = line_edit.text()
                sql = "SELECT * FROM usuarios WHERE strusuariopass = '{}' ".format(passwd)
                query = QSqlQuery()
                query.exec_(sql)
                if query.next():
                    return True
        except Exception as e:
            logger.warning("Loguin.utils.access_system", str(e))
        return False
        
            