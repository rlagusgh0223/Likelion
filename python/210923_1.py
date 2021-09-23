
#1
#PyQt
#pip install pyside2를 먼저 cmd창에 입력한 다음
#pyside2-designer 검색창에 입력하면 들어가진다
#Qt Designer로 코딩
#DenoForm
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("DemoForm.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 PyQt데모")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()



#DemoForm2
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def FirstClick(self):
        self.label.setText("첫번째 버튼을 클릭")
    def SecondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def ThirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()



#DemoForm3
#PyQt5를 사용한 간단 계산기 만들기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("DemoForm3.ui")[0]

class DemoForm(QMainWindow, form_class):
    cal_type = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def plus(self):
        DemoForm.cal_type = '+' #여기에서 DemoForm은 클래스다
        print(DemoForm.cal_type)
    def minus(self):
        DemoForm.cal_type = '-'
    def mul(self):
        DemoForm.cal_type = '*'
    def div(self):
        DemoForm.cal_type = '/'
    def calc(self):
        print(DemoForm.cal_type)
        if DemoForm.cal_type == '+':
            result = int(self.text_In1.toPlainText()) + int(self.text_In2.toPlainText())
            self.label.setText(str(result))#text_In1에서 i가 소문자이면 돌아가지 않는다
        elif DemoForm.cal_type == '-':
            result = int(self.text_In1.toPlainText()) - int(self.text_In2.toPlainText())
            self.label.setText(str(result))
        elif DemoForm.cal_type == '*':
            result = int(self.text_In1.toPlainText()) * int(self.text_In2.toPlainText())
            self.label.setText(str(result))
        elif DemoForm.cal_type == '/':
            if int(self.text_In2.toPlainText()) != 0:
                result = int(self.text_In1.toPlainText()) / int(self.text_In2.toPlainText())
                self.label.setText(str(result))
            else:
                QMessageBox.about(self,'message','0 나누기 에러')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
