import sys
import os
import time
from threading import Thread
from io import StringIO

from PyQt5 import QtWidgets, QtCore, QtGui
import cv2

# os.environ['YOLO_VERBOSE'] = 'false'
from ultralytics import YOLO

class MWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.camBtn.clicked.connect(self.start_camera)
        self.stopBtn.clicked.connect(self.stop)
        self.videoBtn.clicked.connect(self.video)

        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)

        self.model = YOLO('yolov8n.pt')
        self.frameToAnalysis = []

        Thread(target= self.frameAnalysisThreadFunc, daemon= True).start()

    def log_message(self, message, level='INFO'):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'[{timestamp}] [{level}] {message}\n'
        self.text_log.append(log_entry)

    def initUI(self):
        self.resize(1200, 800)
        self.setWindowTitle('Main Window')
        self.statusBar().showMessage('Ready for action!')

        # Menu bar design
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False) # for macOS
        
        appMenu = menu_bar.addMenu("Application") 
        updateAction = appMenu.addAction('Check for Updates')
        preferenceMenu = appMenu.addMenu('Preferences')
        serviceMenu = appMenu.addMenu('Services')
        quitMenu = appMenu.addAction('Quit Application')

        settingsAction = appMenu.addAction('Settings')
        settingsAction.triggered.connect(self.showSettingsWindow)

        fileMenu = menu_bar.addMenu("File")
        open_file_action = fileMenu.addAction('Open...')
        open_folder_action = fileMenu.addAction('Open Folder')
        open_recent_menu = fileMenu.addMenu('Open Recent')
        save_action = fileMenu.addAction('Save')
        save_as_action = fileMenu.addAction('Save As...')

        editMenu = menu_bar.addMenu("Edit")
        undo_action = editMenu.addAction('Undo')
        redo_action = editMenu.addAction('Redo')
        cut_action = editMenu.addAction('Cut')
        copy_action = editMenu.addAction('Copy')
        paste_action = editMenu.addAction('Paste')

        helpMenu = menu_bar.addMenu("Help")
        help_action = helpMenu.addAction('Help')


        # central widget
        centralWidget = QtWidgets.QWidget(self) 
        self.setCentralWidget(centralWidget)

        mainLayout = QtWidgets.QVBoxLayout(centralWidget)

        # top layout
        topLayout = QtWidgets.QHBoxLayout()
        self.label_ori_video = QtWidgets.QLabel(self)
        self.label_treated = QtWidgets.QLabel(self)
        self.label_ori_video.setMinimumSize(520, 400)
        self.label_treated.setMinimumSize(520, 400)
        self.label_ori_video.setStyleSheet("border: 1px solid #D7E2F9;")
        self.label_treated.setStyleSheet("border: 1px solid #D7E2F9;")

        topLayout.addWidget(self.label_ori_video)
        topLayout.addWidget(self.label_treated)

        groupLayout = QtWidgets.QGroupBox(self)

        # bottom layout
        bottomLayout = QtWidgets.QHBoxLayout(groupLayout)
        self.text_log = QtWidgets.QTextBrowser()
        bottomLayout.addWidget(self.text_log)

        # button panel
        btnLayout = QtWidgets.QVBoxLayout()
        self.videoBtn = QtWidgets.QPushButton('📀Video')
        self.camBtn = QtWidgets.QPushButton('📷Camera')
        self.stopBtn = QtWidgets.QPushButton('🔴Stop')

        btnLayout.addWidget(self.videoBtn)
        btnLayout.addWidget(self.camBtn)
        btnLayout.addWidget(self.stopBtn)


        bottomLayout.addLayout(btnLayout)
        mainLayout.addLayout(topLayout)
        # mainLayout.addLayout(bottomLayout)
        mainLayout.addWidget(groupLayout)

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            exit()

        if self.timer_camera.isActive() == False:
            self.timer_camera.start(50)

    def video(self):
        video_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Video', './', 'Video Files(*.mp4 *.avi *.flv *.mkv *.MOV)')[0]
        if not video_path:
            return

        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            exit()

        if self.timer_camera.isActive() == False:
            self.timer_camera.start(50)

    def show_camera(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (520, 400))
        qImage = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888) 
        
        self.label_ori_video.setPixmap(QtGui.QPixmap.fromImage(qImage))

        if not self.frameToAnalysis:
            self.frameToAnalysis.append(frame)

    def frameAnalysisThreadFunc(self):
        while True:
            if not self.frameToAnalysis:
                time.sleep(0.1)
                continue

            frame = self.frameToAnalysis.pop(0)
            result = self.model(frame)[0]
            img = result.plot(line_width= 1)
            qImage_treated = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
            self.label_treated.setPixmap(QtGui.QPixmap.fromImage(qImage_treated))

            time.sleep(0.001)

    def stop(self):
        self.timer_camera.stop()
        self.cap.release()
        self.label_ori_video.clear()
        self.label_treated.clear()

    def showSettingsWindow(self):
        settings_window = QtWidgets.QDialog(self)
        settings_window.setWindowTitle('Settings')
        settings_window.setGeometry(300, 300, 300, 200)
        settings_window.exec_()
        settings_window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MWindow()
    main_win.show()
    sys.exit(app.exec_())