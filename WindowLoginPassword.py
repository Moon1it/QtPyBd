import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QMessageBox, QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
import psycopg2
from WidgetsPy import select_all

class Second(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):

        self.lbl = QLabel('Вы вошли!\nЛогин и пароль верны!', self)
        self.lbl.setFont(QtGui.QFont('Arial', 25))
        self.lbl.move(40,50)
        #self.button.clicked.connect(self.ok)

        self.setWindowTitle('Главная')
        self.setGeometry(1000, 400, 520, 250)
        self.show()

    def ok(self):
        print('close clicked')
        self.close()

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.InitWindow()

    def InitWindow(self):

        self.lbl_login = QtWidgets.QLabel('Логин', self)
        self.lbl_login.move(132,30)

        self.lbl_password = QtWidgets.QLabel('Пароль', self)
        self.lbl_password.move(130,90)

        self.txt_login = QtWidgets.QTextEdit(self)
        self.txt_login.move(92,50)
        self.txt_login.resize(120,30)

        self.txt_password = QtWidgets.QTextEdit(self)
        self.txt_password.move(92,110)
        self.txt_password.resize(120,30)
        

        self.qbtn = QPushButton('Войти', self)
        self.qbtn.clicked.connect(self.Check_login_password)
        self.qbtn.resize(120,30)
        self.qbtn.move(92, 155)

        self.setGeometry(1000, 400, 300, 250)
        self.setWindowTitle('Войти')
        self.show()

    def ContinueSecond(self):
        self.close()
        self.next = Second()
        #next.__init__()
    
    def setText_login(self):
            text = self.txt_login.toPlainText()
            return text
        
    def setText_password(self):
        text = self.txt_password.toPlainText()
        return text
        
    def Check_login_password(self):
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
            if row[0] == self.setText_login() and row[1] == self.setText_password():        
                ck = 1
                self.ContinueSecond()
        if ck == 0:
            QMessageBox.critical(self, "Ошибка", "Неправильный логин или пароль!", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())