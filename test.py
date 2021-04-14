## Ex 5-1. QPushButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QLabel
from PyQt5.QtCore import Qt

import random

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&중앙 이동', self)
        btn1.setCheckable(True)

        btn2 = QPushButton(self)
        btn2.setText('난수 출력(5)')

        btn3 = QPushButton('UPDATE', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        textLabel = QLabel("Message: ", self)
        textLabel.move(0, 0)

        self.label = QLabel(" ",self)
        self.label.move(60, 0)
        self.label.resize(150, 30)

        btn1.move(20, 60)
        btn1.clicked.connect(self.moveSenter)


        btn2.move(140, 60)
        btn1.clicked.connect(self.moveSenter)
        btn2.clicked.connect(self.randomLabel)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 200, 300, 300)
        self.show()


    def moveSenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def randomLabel(self):
        n1 = str(random.randrange(1,6))
        n2 = str(random.randrange(1,6))
        n3 = str(random.randrange(1,6))
        n4 = str(random.randrange(1,6))
        n5 = str(random.randrange(1,6))
        a = n1 + ", " + n2 + ", " + n3 + ", " + n4 + ", " + n5
        self.label.setText(a)
        if n1 == n2 == n3 or n1 == n2 == n4 or n1 == n2 == n5 or n1 == n3 == n4 or n1 == n3 == n5 or n1 == n4 == n5 or n2 == n3 == n4 or n2 == n3 == n5 or n2 == n4 == n5 or n3 == n4 == n5:
            self.label.setText(a + ", Triple!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())