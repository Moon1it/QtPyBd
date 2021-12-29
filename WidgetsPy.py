from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
import sys

def dialog():
    mbox = QMessageBox()
 
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()
 
if __name__ == "__main__":

    app = QApplication(sys.argv) #Создаем приложение интерфейса
    
    w = QWidget() #Создаем главный виджет
    w.resize(300,300) #Размеры w
    w.setWindowTitle('New window') #Заголовок w
    
    #Текстовое поле на виджете w
    label = QLabel(w) 
    label.setText("Main information") #Содержимое текстового поля
    label.move(50,70) #Расположение текстового поля на виджете
    label.show() #Вывод поля на экран
 
    #Кнопка на виджете w
    btn = QPushButton(w)
    btn.setText('Beheld') #Текст на кнопке
    btn.move(110,150) #Расположение кнопки
    btn.show() #Вывод кнопки на экран
    btn.clicked.connect(dialog) 
 
    w.show()
    sys.exit(app.exec_())