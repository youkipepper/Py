import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # container = QVBoxLayout()
        container = QHBoxLayout()

        hobby_box = QGroupBox('Hobby')
        v_layout = QVBoxLayout()
        btn1 = QRadioButton('Hobby 1')
        btn2 = QRadioButton('Hobby 2')
        btn3 = QRadioButton('Hobby 3')

        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)

        hobby_box.setLayout(v_layout)

        gender_box = QGroupBox('Gender')
        h_layout = QHBoxLayout()
        btn4 = QRadioButton('Male')
        btn5 = QRadioButton('Female')
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)

        gender_box.setLayout(h_layout)

        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        self.setLayout(container)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    app.exec_()