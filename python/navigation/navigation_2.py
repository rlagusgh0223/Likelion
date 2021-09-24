import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_navi = uic.loadUiType("navigation.ui")[0]

class navi(QMainWindow, form_navi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def street(start,end):
        korea = {
            "서울":{"인천":32, "대전":162, "대구":289, "광주":331, "울산":397, "부산":398},
            "인천":{"서울":32, "대전":174, "대구":327, "광주":343, "울산":435, "부산":436},
            "대전":{"서울":162, "인천":174, "대구":153, "광주":169, "울산":161, "부산":162},
            "대구":{"서울":289, "인천":327, "대전":153, "광주":322, "울산":108, "부산":109},
            "광주":{"서울":331, "인천":343, "대전":169, "대구": 322, "울산":311, "부산":262},
            "울산":{"서울":397, "인천":435, "대전":161, "대구":108, "광주":311, "부산":51},
            "부산":{"서울":398, "인천":436, "대전":162, "대구":109, "광주":262, "울산":51}
        }
        route = start + '-' + end
        length = korea[start][end]
        return route, length
   
    def search(self):
        Start = self.start.toPlainText()
        End = self.end.toPlainText()
        route, length = navi.street(Start, End)        
        self.label.setText(str(route))
        self.label_2.setText(str(length))#라벨은 str만 받고 int는 받지 않는다

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = navi()
    demoWindow.show()
    app.exec_()
