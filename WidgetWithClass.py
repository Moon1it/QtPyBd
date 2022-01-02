from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QInputDialog, QLineEdit, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox
import sys
from PyQt5.sip import delete
import psycopg2

def application():
#    frm.setStyleSheet('background: rgb(0,0,255);')

    def select_all():
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        
        cursor = connection.cursor()
        cursor.execute("SELECT * from people")                          
        rows = cursor.fetchall()
        t = ''
        for row in rows:
            t += str(row) + '\n'  
        txt1.setPlainText(t)

        cursor.close()
        connection.close()
    
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
        cursor.execute(st) 
        connection.commit()
        cursor.close()
        connection.close()
        select_all()
    
    def delete_data():
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        
        d = getText_del()
        
        cursor = connection.cursor()
        st = 'Delete from people where id='
        st += str(d) + ";"
        cursor.execute(st)

        connection.commit()
        cursor.close()
        connection.close()
        select_all()

    def getText_id():
        text = lbl1.toPlainText()
        return text

    def getText_name():
        text = lbl2.toPlainText()
        return text

    def getText_age():
        text = lbl3.toPlainText()
        return text

    def getText_del():
        text = delete.toPlainText()
        return text

    app = QApplication(sys.argv)
    w = QMainWindow()
    w.setWindowTitle('New window')
    w.setWindowOpacity(30)
    #w.setStyleSheet('background: rgb(255,215,185);')
    w.setGeometry(1000, 300, 404, 420)

    l1 = QtWidgets.QLabel(w)
    l1.setText('ID')
    l1.move(63,30)

    l2 = QtWidgets.QLabel(w)
    l2.setText('Name')
    l2.move(183,30)
    
    l3 = QtWidgets.QLabel(w)
    l3.setText('Age')
    l3.move(320,30)

    lbl1 = QtWidgets.QTextEdit(w)
    lbl1.move(20,60)
    lbl1.resize(100,30)

    lbl2 = QtWidgets.QTextEdit(w)
    lbl2.move(150,60)
    lbl2.resize(100,30)

    lbl3 = QtWidgets.QTextEdit(w)
    lbl3.move(280,60)
    lbl3.resize(100,30)

    btn1 = QtWidgets.QPushButton(w)
    btn1.setText('Загрузить данные')
    btn1.move(135,120)
    btn1.resize(130,30)
    btn1.clicked[bool].connect(insert_data)

    txt1 = QtWidgets.QPlainTextEdit(w)
    txt1.move(20,180)
    txt1.resize(365,160)

    d_t = QtWidgets.QLabel(w)
    d_t.setText('delete line')
    d_t.move(75,342)
    
    delete = QtWidgets.QTextEdit(w)
    delete.move(40,370)
    delete.resize(130,30)

    btn3 = QtWidgets.QPushButton(w)
    btn3.setText('Удалить')
    btn3.move(230,370)
    btn3.resize(130,30)
    btn3.clicked[bool].connect(delete_data)
    
    select_all()
    
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    application()