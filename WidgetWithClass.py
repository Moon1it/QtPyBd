from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QInputDialog, QLineEdit, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox
import sys
import psycopg2

  

def application():
#    frm.setStyleSheet('background: rgb(0,0,255);')

    def insert_data():
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        
        id_p = getText_id()
        name_p = getText_name()
        age_p = getText_age()

        cursor = connection.cursor()
        st = 'insert into people (id, firstname, age) values ('
        st += str(id_p) + "," + "'" + str(name_p)+ "'" + "," + str(age_p) + ")"
        print(st)
        cursor.execute(st) 
        
        connection.commit()

        cursor.close()
        connection.close()
    
    def getText_id():
        text = lbl1.toPlainText()
        return text

    def getText_name():
        text = lbl2.toPlainText()
        return text

    def getText_age():
        text = lbl3.toPlainText()
        return text

    app = QApplication(sys.argv)
    w = QMainWindow()
    w.setWindowTitle('New window')
    w.setWindowOpacity(30)
    #w.setStyleSheet('background: rgb(255,215,185);')
    w.setGeometry(1000, 300, 400, 250)

    lbl1 = QtWidgets.QTextEdit(w)
    lbl1.move(20,60)
    lbl1.resize(100,28)

    lbl2 = QtWidgets.QTextEdit(w)
    lbl2.move(150,60)
    lbl2.resize(100,28)

    lbl3 = QtWidgets.QTextEdit(w)
    lbl3.move(280,60)
    lbl3.resize(100,28)

    btn3 = QtWidgets.QPushButton(w)
    btn3.setText('Red')
    btn3.move(50,150)
    btn3.clicked[bool].connect(insert_data)   
    
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    application()