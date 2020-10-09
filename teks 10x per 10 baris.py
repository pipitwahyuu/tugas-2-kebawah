from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    
    a = 1
    while a<=10:
        labelku = QLabel(window)
        labelku.setText('Halo My name is Pipit Wahyuningsih')
        labelku.setFont(QFont('Arial',12))
        labelku.move(100, a*20)
        a+=1

    window.setGeometry(400,100,700,500)
    window.setWindowTitle('Belajar PyQt5')
    window.setStyleSheet("background-color : black; color: white")
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    window()
