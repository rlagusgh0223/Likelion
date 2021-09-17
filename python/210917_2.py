#1
#클래스 사용하기
#클래스 : 객체를 표현하기 위한 문법
class Person:
    def __init__(self):     #클래스의 메소드 안에있는 이것은(__init__) 자동으로 실행된다
        self.hello = '안녕하세요. 저는 사람입니다.'

    def greeting(self):
        print(self.hello)   #클래스 안에 있는 함수가 __init__의 내용을 쓰기 위해서는 self.~를 쓴다
        #self : 그게 사용된 영역의 자기자신

james = Person()
james.greeting()    #안녕하세요. 저는 사람입니다.



#인스턴스를 만들 때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    #안녕하세요. 저는 마리아입니다

print("이름 :",maria.name)    #마리아
print("나이 :",maria.age)     #20
print("주소 :",maria.address) #서울시 서초구 반포



#Person클래스로 MAria, James라는 인스턴스 생성
#Maria, Jame 두 사람의 나이, 이름, 주소를 받아들여 객체에 저장하고 화면에 프린트
class Person:
    def __init__(self, age, name, address):
        self.age = age
        self.name = name
        self.address = address

name = input("이름은 무엇인가요? :")
age = input("나이는 무엇인가요? :")
address = input("주소는 무엇인가요? :")
Maria = Person(age, name, address)

name = input("이름은 무엇인가요? :")
age = input("나이는 무엇인가요? :")
address = input("주소는 무엇인가요? :")
James = Person(age, name, address)

print("첫번째 이름 :",Maria.name)
print("첫번째 나이 :",Maria.age)
print("첫번째 주소 :",Maria.address)

print("두번째 이름 :",James.name)
print("두번째 나이 :",James.age)
print("두번째 주소 :",James.address)



#비공개 속성 사용하기
#self.__속성 : 비공개 속성이라 클래스 바깥에서 접근 불가(__속성__는 비공개 아니다)
#클래스 내부적으로는 사용하지만 외부에서는 사용 못함
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet= wallet    #변수 앞에 __를 붙여서 비공개 속성으로 만듦
    def pay(self, amount):
        self.__wallet -= amount    #비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print("이제 {0}원 남았네요.".format(self.__wallet))

maria = Person("마리아", 20, '서울시 서초구 반포동', 10000)
#maria.__wallet -= 10000    #클래스 바깥에서 비공개 속성이 접근하면 에러가 발생
maria.pay(3000)



#연습문제
#게임 캐릭터 능력치(체력, 마나, AP)가 입력됨
#애니(Annie) 클래스를 작성하여 티버 스킬의 피해량이 출력되게
#피해량 : AP*0.65 + 400
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        self.ability_power = self.ability_power*0.65 + 400
        print("티버: 피해량",self.ability_power)

health, mana, ability_power = map(float, input().split())
x = Annie(health = health, mana=mana, ability_power=ability_power)
x.tibbers()



#연습문제
#class에 포함 내용
#1. Orange 상자 관리 Class 만들기
#2. 생성자(생성자 초기값 10개)
#3. Orange 추가 하는 멤버 함수
#4. Orange 제거 하는 멤버 함수
#5. Orange Box를 0으로 초기화하는 멤버 함수
#6. Ornage Box 내부의 Orange 수량을 확인하는 멤버 함수
#단, 수량을 관리하는 멤버 변수는 외부에서 접근 불가
#main 코드에 포함 내용
#1. 초기 Orange Box내의 Orange수량표시
#2. 입력 받은 수만큼 Orange 추가 -> Orange Box내의 Orange 수량 표시
#3. 입력 받은 수만큼 Orange 제거 -> Orange Box내의 Orange 수량 표시
class OrangeBox:
    def __init__(self):
        self.__count = 10       #초기값 주는데 쓰인 것 같다
    def __del__(self):      #소멸자
        print("Class 종료")
    def AddBox(self, add_count):
        self.__count += add_count
    def SubBox(self, sub_count):
        self.__count -= sub_count
    def DelBox(self):
        self.__count = 0
    def CountBox(self):
        return self.__count

MyOB = OrangeBox()
nData = int(input("추가 수량 : "))
MyOB.AddBox(nData)
print("현재 수량 %d"%MyOB.CountBox())

nData = int(input("제거 수량 : "))
MyOB.SubBox(nData)
print("현재 수량 %d"%MyOB.CountBox())

print("수량제거")
MyOB.DelBox()
print("현재 수량 %d"%MyOB.CountBox())

del MyOB    #여기에서는 이걸로 끝이니까 사실 소멸자 없어도 되지만
            #앞으로 프로그래밍할때에는 이런거 소멸 안해주면
            #한없이 메모리가 쌓이니까 없애주는게 좋다



#클래스 상속
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):  #Person의 자식클래스
    def __init__(self):
        print('Student __init__')
        #super()로 기반 클래스의 __init__ 메서드 호출
        super().__init__()  #super()는 부모 클래스를 의미한다.
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)





#GUI - 심화
#PyQt
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#QMainWindow는 PyQt의 main window class임. QMainWindow가 부모 class
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()      #부모 클래스의 생성자 이용
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
