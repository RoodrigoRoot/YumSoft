from logger import logger
from Loguin.login import Dialog
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Dialog()
    main.show()
    app.exec_()
