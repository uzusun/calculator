# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox,QPlainTextEdit)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1= QPlainTextEdit()  # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)  # 텍스트 에디트 위젯을 읽기만 가능하도록 수정
        
        self.btn1=QPushButton('Message',self)
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭시 핸들러 함수 연결

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self):
        #QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText("Button clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())