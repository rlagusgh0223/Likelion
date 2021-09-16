#1
#시간 표현하는 방법
import datetime
d = datetime.datetime.now()
strTime1 = '%4d%02d%02d %02d%02d%02d'\
           %(d.year, d.month, d.day, d.hour, d.minute, d.second)
print(strTime1)     #20210916 090848
#\는 줄이 길때 엔터를 해도 다음줄도 같은줄이라는 내용이다
#한 줄인때에는 쓰면 안된다

time_now = d.strftime('%Y%m%d_%H%M%S')
print(time_now)     #20210916_090848

time_now = d.now()
print(time_now)     #2021-09-16 09:08:48.990523

time_now = d.today()
print(time_now)     #2021-09-16 09:08:48.997123


import time
time_now = time.strftime('%Y%m%d_%H%M%S',time.localtime())
print(time_now)     #20210916_090849
#time.localtime()은 현재지역의 시간을 출력하라는 의미이다
#strftime은 시간 출력 형식을 지정한다





#2
#GUI(그래픽 유저 인터페이스) Tkinter
#Tkinter : 파이썬 표준 라이브러리. GUI의 개념을 익히기에 적합
import tkinter as tk
root = tk.Tk()

lbl = tk.Label(root, text='EduCoding', underline=3)
lbl.pack()
#화면에 뜨는 문자는 EduCoing이고 3번재(0,1,2,3)에 밑줄이 있다

txt = tk.Entry(root)
txt.pack()
#타자 입력 부분

btn = tk.Button(root, text='OK', activebackground='red', width=5)
btn.pack()
#버튼은 OK라는 문자가 있는거 하나이며, 클릭시 빨간색으로 버튼이 변한다
#width를 바꾸면 버튼의 가로길이가 변한다

root.mainloop()



#GUI로 Hello World 출력하기
#Tkinter 라이브러리 임포트
import tkinter as tk

#Tk 객체 인스턴스 생성
root = tk.Tk()  #윈도우판 이름 root로 지정

#라벨 생성
label = tk.Label(root, text='Hello World')  #root라는 윈도우판에 Hello Wold라는 텍스트 넣은 객체를 만듬

#라벨 패치
label.pack()    #만들어진 객체를 윈도우에 배치

#root 표시
root.mainloop()



#버튼 만들기
#Tkinter 라이브러리 임포트
import tkinter as tk

#Tk 객체 인스턴스 생성
root = tk.Tk()

#버튼을 눌렀을 때 처리
def func():
    #메시지를 파이썬 셀에 출력
    print('Pushed')

#버튼 생성
button = tk.Button(root, text = 'Push!', command = func)
#commad에 의해 버튼 클릭시 자동으로 동작하는 함수 func
#func처럼 이벤트 발생에 따라 호출되는 함수를 콜백 함수라고 한다

#버튼 배치
button.pack()

#root 표시
root.mainloop()



#버튼 만들기2
import tkinter as tk
root = tk.Tk()

#버튼 눌렀을 때 처리
def func():
    #Label 표시 변경
    label.config(text = 'Pushed')
    #config는 옵션을 바꿔준다

#라벨 생성
label = tk.Label(root, text = 'Push Button')
label.pack()

#버튼 생성
button = tk.Button(root, text = 'Push!', command = func)
button.pack()

root.mainloop()



#Button 누를때마다 Label에 'apple','oragne'번갈아 표시하기
import tkinter as tk
root = tk.Tk()

bAct = False
def func():
    global bAct #global로 선언 안하면 수정할 수 없음
    if bAct:    #bAct가 True일때 동작(처음에는 False니까 동작 안함)
        label.config(text = 'apple')
        bAct = False
    else:       #bAct가 False일때 동작
        label.config(text = 'orange')
        bAct = True

label = tk.Label(root, text = 'apple')
label.pack()

button = tk.Button(root, text = 'Push!',command = func)
button.pack()

root.mainloop()



#버튼만들기 3
#버튼을 누른 다음에 마우스가 버튼을 벗어나면 라벨 돌아옴
import tkinter as tk
root = tk.Tk()
def func():
    label.config(text = 'Pushed')

#마우스 커서가 버튼을 벗어났을 때 처리
def func_event(ev):
    #라벨 표시 변경
    label.config(text = 'Push Button')
    
label = tk.Label(root, text = 'Push Button')
label.pack()
button = tk.Button(root, text = 'Push!', command = func)
button.pack()

#마우스 커서가 버튼을 벗어났을 때의 이벤트 추가
button.bind('<Leave>', func_event)
#bind : click이 아닌 이벤트때(클릭 이벤트는 command)
#<Leave> : 마우스 커서가 위젯 밖으로 벗어났을때

root.mainloop()



#초기에는 PushButton
#클릭하면 Pushed
#버튼 바깥으로 벗어나면 Leave
#버튼 안으로 들어오면 Enter
import tkinter as tk
root = tk.Tk()

def func():
    label.config(text = 'Pushed')
def func_leave(ev):
    label.config(text = 'Leave')
def func_enter(ev):
    label.config(text = 'Enter')

label = tk.Label(root, text = 'Push Button')
label.pack()
button = tk.Button(root, text = 'Push', command = func)
button.pack()

button.bind('<Leave>',func_leave)
button.bind('<Enter>',func_enter)

root.mainloop()



#Event Object
#버튼을 눌렀을 때 버튼의 어느 위치에 있는지 라벨에 표시
import tkinter as tk
root = tk.Tk()
def func():
    label.config(text = 'Pushed')

def func_event_click(ev):   #ev : 버튼 위치
    disp = str(ev.x) + '/' + str(ev.y)  #내가 버튼을 누른 위치 표시
    label.config(text = disp)

label = tk.Label(root, text = 'P B')
label.pack()
button = tk.Button(root, text = 'Push', command = func)
button.pack()

button.bind('<Button-1>',func_event_click)
#왼쪽 버튼이 눌렸을때

root.mainloop()



#라디오 버튼 만들기
import tkinter as tk
def Action1():
    lbl.config(text = 'Option 1')
def Action2():
    lbl.config(text = 'Option 2')

root = tk.Tk()

lbl = tk.Label(root, text = 'EduCoding', underline = 3)
lbl.pack()

rbvar = ''  #변수 Null로 생성
rb1 = tk.Radiobutton(root, text='Option 1', variable=rbvar, value='a', indicatoron=1, command=Action1)
#indicatoron이 1이면 여러개 중 하나 체크하는 원 모양으로 나온다
#rb1, rb2 둘다 1로 지정되면 체크하는 모양 나온다
rb1.pack()
rb2 = tk.Radiobutton(root, text='Option 2', variable=rbvar, value='b', indicatoron=1, command=Action2)
rb2.pack()

root.mainloop()









