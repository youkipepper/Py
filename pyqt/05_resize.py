import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    
    w.setWindowTitle('QLineEdit')
    
    label = QLabel('Hello', w)
    label.setGeometry(20, 20, 30, 30)

    edit = QLineEdit(w)
    edit.setPlaceholderText('Enter your account')
    edit .setGeometry(20, 50, 200, 30)

    btn = QPushButton('Sign Up', w)
    btn.setGeometry(20, 100, 200, 30)

    w.resize(300, 200)
    w.show()
    app.exec_()