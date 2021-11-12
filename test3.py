from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap,QColor

import sys
from chellam import Chellam
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chellam anna ")
        self.setGeometry(200, 200, 400, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        label = QLabel(self)
        pixmap = QPixmap('Chellam sir.jpg')
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 400, 400)
        label.setStyleSheet("color: white")

        label1 = QtWidgets.QLabel('white',label)
        label1.setText("Voice Based Personal Assistant Chellam:")
        label1.setGeometry(80, 50, 300, 50)

        button = QtWidgets.QPushButton('white',label)
        button.setText("press to Start listening")
        button.clicked.connect(Chellam)
        button.setGeometry(100, 100, 200, 50)
        button.setStyleSheet("background-color: black")

        label2 = QtWidgets.QLabel('white',label)
        label2.setText("Say \"Activate\" to activate chellam and \n \"Deactivate\" to stop listening commands")
        label2.setGeometry(80, 200, 300, 80)


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())