from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QTextEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox
import sys
import psycopg2

def dialog():
    mbox = QMessageBox()
 
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

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
    w.resize(350,200) #Размеры w
    w.setWindowTitle('New window') #Заголовок w
    
    #Текстовое поле на виджете w
    label = QLabel() 
    label.setText("Main information") #Содержимое текстового поля
    label.setAlignment(QtCore.Qt.AlignCenter)
 
    #Кнопка на виджете w
    btn = QPushButton()
    btn.setText('Next') #Текст на кнопке
    btn.clicked.connect(dialog) 
    
    btn_se = QPushButton()
    btn_se.setText('Select all table') #Текст на кнопке
    btn_se.clicked.connect(select_all) 
 
    txt = QTextEdit()
    txt.setPlaceholderText("Enter some text here")

    hbox = QVBoxLayout(w)
 
    hbox.addWidget(label)
    hbox.addWidget(btn)
    hbox.addWidget(btn_se)
    hbox.addWidget(txt)

    w.show()
    sys.exit(app.exec_())