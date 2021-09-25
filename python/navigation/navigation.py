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
            "서울":[["인천",32], ["대전",162], ["대구",289]],
            "인천":[["서울",32], ["대전",174]],
            "대전":[["서울",162], ["인천",174], ["대구",153], ["광주",169]],
            "대구":[["서울",289], ["대전",153], ["울산",108], ["부산",109]],
            "광주":[["대전",169], ["부산",262]],
            "울산":[["대구",108], ["부산",51]],
            "부산":[["광주",262], ["대구",109], ["울산",51]]
        }
        visited = {"서울":0,"인천":0,"대전":0,"대구":0,"광주":0,"울산":0,"부산":0}
        #visited = {"서울":1000,"인천":1000,"대전":1000,"대구":1000,"광주":1000,"울산":1000,"부산":1000}
        #visited = [1000]*7
        now = start
        route = start
        length = 0

        #인천-울산/부산은 한번 건너도 닿지 않으므로 추가로 계산
        if (start=='인천' and end=='부산') or (start=='인천' and end=='울산'):
            start = '서울'
            route = '인천-서울'
            length += 32
        elif (start=='부산' and end=='인천') or (start=='울산' and end=='인천'):
            end = '서울'
            rend = '인천'
            length += 32

        print(start,route,length)
        for i in korea[start]:    #현재 검색하는 도시 인근의 거리 구하는 반복문
            visited[i[0]] = i[1]
        print(visited)
        
        for i in range(len(korea[start])):    #인접한 도시는 두번 계산할 필요가 없다
            if end in korea[start][i][0]:   #도착지가 출발지의 딕셔너리 안에 있다면
                route = route + '-' + end    #바로 출력
                length += visited[end]
                return route, length
            
        for i in korea[end]:    #도착지에서도 출발지와 동일한 반복문 수행
            if visited[i[0]] != 0: #이때 visited의 값이 0이 아니라는 것은 출발지에서 들렀다는 뜻
                route = route + '-' + i[0] + '-' + end    #출발지와 중간 접견지, 도착지를 계산한다
                length += visited[i[0]] + i[1]
                if (start=='부산' and rend=='인천') or (start=='울산' and rend=='인천'):
                    route = route + '-인천'   #부산/울산 -> 인천일 경우 경로를 추가해준다
                return route, length    #여기서 리턴하지 않으면 광주-대구의 경우 겹치는 경로가 있어 이상한 경로가 나온다
            visited[i[0]] = i[1]
        print(visited)
     
    def search(self):
        Start = self.start.toPlainText()
        End = self.end.toPlainText()
        route, length = navi.street(Start, End)        
        self.label.setText(str(route))
        self.label_2.setText(str(length))   #라벨은 str만 받고 int는 받지 않는다

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = navi()
    demoWindow.show()
    app.exec_()
