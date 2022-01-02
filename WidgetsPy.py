from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QInputDialog, QLineEdit, QTextEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox
import sys
import psycopg2


def insert_data():
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    
    id_p = QInputDialog.getInt(label= label_id)
    name_p = QInputDialog.getText(label= label_name)
    age_p = QInputDialog.getInt(label= label_age)

    cursor = connection.cursor()
    st = "insert into people (id, firstname, age) values ({id_p}, {name_p}, {age_p}) ".format()
    cursor.execute(st)                       
    
   
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
    txt.setPlainText(t)

if __name__ == "__main__":

    app = QApplication(sys.argv) #Создаем приложение интерфейса
    
    w = QWidget() #Создаем главный виджет
    w.resize(950,550) #Размеры w
    w.setWindowTitle('Table') #Заголовок w
    
    #Текстовое поле на виджете w
    label = QLabel() 
    label.setText('Table people') #Содержимое текстового поля
    label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
    
    label_id = QLabel()
    label_id.setText('Input id') #Содержимое текстового поля
    label_name = QLabel()
    label_name.setText('Input name') #Содержимое текстового поля
    label_age = QLabel()
    label_age.setText('Input age') #Содержимое текстового поля
    

    insert_id = QLineEdit()
    insert_name = QLineEdit()
    insert_age = QLineEdit()

    btn_ins = QPushButton()
    btn_ins.setText('insert information') #Текст на кнопке
    btn_ins.setFont(QtGui.QFont("Times", 10))
    btn_ins.clicked.connect(insert_data) 
    
    btn_se = QPushButton()
    btn_se.setText('Select all table') #Текст на кнопке
    btn_se.setFont(QtGui.QFont("Times", 10))
    btn_se.clicked.connect(select_all)
 
    txt = QTextEdit()
    txt.setPlaceholderText("Enter some text here")
    txt.setFont(QtGui.QFont("Times", 12))

    grid = QGridLayout(w) #Сетка для расположения объектов
    grid.setSpacing(10)
    grid.addWidget(label, 0, 1)
    
    grid.addWidget(label_id, 1, 0)
    grid.addWidget(label_name, 1, 1)
    grid.addWidget(label_age, 1, 2)
    
    grid.addWidget(insert_id, 2, 0)
    grid.addWidget(insert_name, 2, 1)
    grid.addWidget(insert_age, 2, 2)

    grid.addWidget(btn_ins, 4, 0, 1, 3)
    grid.addWidget(btn_se, 5, 0, 1, 3)
    
    grid.addWidget(txt, 6, 0, 1, 3)
    
    w.show()
    sys.exit(app.exec_())