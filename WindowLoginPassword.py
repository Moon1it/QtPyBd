import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
import psycopg2
from WidgetsPy import select_all


class window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        def setText_login():
            text = txt_login.toPlainText()
            return text
        
        def setText_password():
            text = txt_password.toPlainText()
            return text
        
        def Check_login_password():
            connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        
            cursor = connection.cursor()
            cursor.execute("SELECT * from login")                          
            rows = cursor.fetchall()
            
            cursor.close()
            connection.close()
            ck = 0
            for row in rows:
                if row[0] == setText_login() and row[1] == setText_password():
                    print('Yes')
                    ck = 1
            if ck == 0:
                QMessageBox.critical(self, "Ошибка", "Неправильный логин или пароль!", QMessageBox.Ok)
                        
        lbl_login = QtWidgets.QLabel(self)
        lbl_login.setText('Логин')
        lbl_login.move(132,30)

        lbl_password = QtWidgets.QLabel(self)
        lbl_password.setText('Пароль')
        lbl_password.move(130,90)

        txt_login = QtWidgets.QTextEdit(self)
        txt_login.move(92,50)
        txt_login.resize(120,30)

        txt_password = QtWidgets.QTextEdit(self)
        txt_password.move(92,110)
        txt_password.resize(120,30)

        qbtn = QPushButton('Войти', self)
        qbtn.clicked.connect(Check_login_password)
        qbtn.resize(120,30)
        qbtn.move(92, 155)

        self.setGeometry(1000, 400, 300, 250)
        self.setWindowTitle('Войти')
        self.show()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = window()
    sys.exit(app.exec_())