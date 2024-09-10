import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QGridLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')
        
        layout = QVBoxLayout()

        edit = QLineEdit()
        edit.setPlaceholderText('Enter')
        layout.addWidget(edit)

        grid = QGridLayout()

        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['1', '2', '3', '*', 'C'],
            3: ['0', '.', '=', '/', '=']
        }

        for line_number, line_data in data.items():
            for column_number, number in enumerate(line_data):
                button = QPushButton(number)
                grid.addWidget(button, line_number, column_number)
        
        layout.addLayout(grid)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    app.exec_()