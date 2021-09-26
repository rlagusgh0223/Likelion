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



"""

            #==================
            #"서울":{"인천":32, "대전":162, "대구":289},
            #"인천":{"서울":32, "대전":174},
            #"대전":{"서울":162, "인천":174, "대구":153, "광주":169},
            #"대구":{"서울":289, "대전":153, "울산":108, "부산":109},
            #"광주":{"대전":169, "부산":262},
            #"울산":{"대구":108, "부산":51},
            #"부산":{"광주":262, "대구":109, "울산":51}
            #===================
            
        #visited = {"서울":1000,"인천":1000,"대전":1000,"대구":1000,"광주":1000,"울산":1000,"부산":1000}
        #visited = [1000]*7
            #        area = korea[now][0]    #딕셔너리 내에서 최단거리를 구하기 위한 변수. 초기값으로 딕셔너리의 첫번째값
              
#        for i in korea[now]:    #현재 검색하는 도시 인근의 거리 구하는 반복문
#            if visited[i[0]] > i[1]:    #최단거리를 구하기 위해 visited의 값과 현재값을 비교
#                visited[i[0]] = i[1]    #맨 처음에는 모든 visited의 값이 1000이므로 모든 도시의 거리가 입력됨
#            if area[1] > i[1]:  #visited와는 별도로 딕셔너리 내에서 최솟값을 구하기 위해 계산
                        #다음 반복문 도시를 정하기 위해 필요하다
#                area = i    #ex) 서울이 현재 반복문이 돌아가는 딕셔너리이면 area는 가장 거리가 짧은 인천이 된다
#            print(area)
#        now = area[0]    #now에 area를 넘겨줘서 다음 출발지를 바꿔준다
#        route = area[0]
#        length += area[1]
#        print(visited)
#2
#        while korea[now] != end:
#            for i in korea[now]:
#                if i == route:
#                    continue
#                if visited[i[0]] > i[1] + length:
#                    visited[i[0]] = i[1] + length
#                if area[1] > i[1]:
#                    area = i
#                print(area)
#            now = area[0]
#            route = area[0]
#            length += area[1]
#            print(visited)
"""
