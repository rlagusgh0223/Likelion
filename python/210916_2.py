#1
import tkinter as tk
root = tk.Tk()
def func1():
    label.config(text = 'Button 1')
def func2():
    label.config(text = 'Button 2')

#라디오 버튼 값을 저장하는 정수형 Variable 객체 생성
sel = tk.IntVar()
#sel에 1 할당
sel.set(1)

label = tk.Label(root, text = 'Select Button')
label.pack()

#라디오 버튼 1 생성
rb1 = tk.Radiobutton(root, text = 'Button 1', variable = sel, value = 1, command = func1)
#라디오 버튼 1 배치
rb1.pack()
#라디오 버튼 2 생성
rb2 = tk.Radiobutton(root, text = 'Button 2', variable = sel, value = 2, command = func2)
#라디오 버튼 2 배치
rb2.pack()

root.mainloop()



#연습문제
#라벨 1개, 버튼 1개, 라디오버튼 3개
#버튼이 눌리면 선택된 라디오 버튼이 쉘에 print로 표시
#라디오 버튼이 선택되면 라벨에 선택 내용 표시
import tkinter as tk
root = tk.Tk()
def func1():
    label.config(text = 'Choice 1')
def func2():
    label.config(text = 'Choice 2')
def func3():
    label.config(text = 'Choice 3')
def func():
    #sel의 값(value)를 받아온다
    print('Choice',sel.get())
    #set.get()에서 () 안쓰면 value가 안나오고 문자열이 나온다

#위에선 따로 초기값을 줬지만(sel.set(1)) 여기서는 바로 줬다
#라디오 버튼의 정보를 가지고 있는 변수로 sel을 지정해줬다
#라디오 버튼은 처음 버튼을 1부터 시작한다
sel = tk.IntVar(root, 1)

label = tk.Label(root, text = 'EduCoding', underline = 3)
label.pack()

rb1 = tk.Radiobutton(root, text = 'Choice 1', variable = sel, value = 1, command = func1)
rb1.pack()
rb2 = tk.Radiobutton(root, text = 'Choice 2', variable = sel, value = 2, command = func2)
rb2.pack()
rb3 = tk.Radiobutton(root, text = 'Choice 3', variable = sel, value = 3, command = func3)
rb3.pack()

button = tk.Button(root, text = 'Print choice', command = func)
#아래처럼 코드를 짜면 함수 없이도 동일하게 동작된다
#button = tk.Button(root, text = 'Print choice', command = lambda:print('Choice',sel.get()))
button.pack()

root.mainloop()



#슬라이더
import tkinter as tk
root = tk.Tk()
#슬라이드 바의 값을 저장할 Variable 객체 생성(정수형)
val = tk.IntVar()
#0으로 설정(나중에 라디오버튼 값 바꿔줄때 쓸 수 있다)
val.set(0)

#손잡이를 움직였을때 처리
def func(scl):
    label.config(text = 'Value = %d' %int(scl))
    
#슬라이드 바의 값을 표시하는 라벨 생성
label = tk.Label(root, text = 'Value = %d' %val.get())
label.pack()

#슬라이브 바 생성
#Scale 라벨 표시. 수평으로 숫자 범위는 0에서 100까지
s = tk.Scale(root, label = 'Scale', orient = 'h', from_ = 0, to = 100,\
             showvalue = False, variable = val, command = func)
#orient = h:가로, v:세로로 바가 생김
#from_ : 슬라이드바 최솟값
#to : 슬라이드바 최댓값
#showvalue=True이면 바 위에 숫자가 보인다
#variable : 라디오버튼 묶음

s.pack()
root.mainloop()



#텍스트 박스 만들기
import tkinter as tk
root = tk.Tk()

#엔터 키(리턴 키) 눌럿을때 동작
def func(ev):
    #라벨 표시 변경
    label.config(text = e.get())

label = tk.Label(root, text = 'Input Text')
label.pack()

#텍스트 박스 생성
e= tk.Entry(root)
e.pack()

#리턴 키(엔터)를 눌렀을때의 이벤트 추가
e.bind('<Return>',func)

root.mainloop()



#연습문제
#라벨 1, 텍스트 박스1, 버튼 1
#버튼을 클릭하면 텍스트 박스의 입력 내용이 라벨에 표시
#라벨의 기본 문구는 'Input Text'
import tkinter as tk
root = tk.Tk()

def func():
    label.config(text = e.get())

label = tk.Label(root, text = 'Input Text')
label.pack()

e = tk.Entry(root)
e.pack()

button = tk.Button(root, text = 'Dislpay', command = func)
button.pack()

root.mainloop()



#부모 윈도우에서 자식 윈도우 생성하기
#자식 윈도우는 부모 윈도우에서 얼마든지 만들 수 있으며,
#자식 윈도우는 사라져도 부모 윈도우는 사라지지 않지만
#부모 윈도우가 사라지면 자식 윈도우도 같이 사라진다
import tkinter as tk

def create_window():
    def act_child():
        lbl_child.config(text='Child Action')

    window = tk.Toplevel(root)#root로부터 파생되는 또다른 윈도우를 만듬

    lbl_child = tk.Label(window, text='결과 표시창')
    lbl_child.pack()

    btn_child = tk.Button(window, text='New window Button', command=act_child)
    btn_child.pack()

root = tk.Tk()
btn_root = tk.Button(root, text = 'Create new window', command=create_window)
btn_root.pack()

root.mainloop()



#텍스트 계산기 만들기
#1. 입력을 받는 두개의 텍스트 박스
#2. 사칙연산은 라디오 버튼으로 선택
#3. 결과 버튼을 누르면 라벨에 결과가 표시
#4. 0으로 나누는 예외 상황 처리
#5. 표시는 소수점 2자리 까지 표기
import tkinter as tk
root = tk.Tk()

def func():
    if cal.get() == 1:
        result = float(n1.get()) + float(n2.get())
        label.config(text = '%.2f'%result)
    elif cal.get() == 2:
        result = float(n1.get()) - float(n2.get())
        label.config(text = '%.2f'%result)
    elif cal.get() == 3:
        result = float(n1.get()) * float(n2.get())
        label.config(text = '%.2f'%result)
    elif cal.get() == 4:
        if int(n2.get()) == 0:
            label.config(text = "0으로 나눌 수 없습니다")
        else:
            result = float(n1.get()) / float(n2.get())
            label.config(text = '%.2f'%result)

n1 = tk.Entry(root)
n2 = tk.Entry(root)
n1.pack()
n2.pack()

cal = tk.IntVar(root,1)
rb1 = tk.Radiobutton(root, text = 'Button +', variable = cal, value = 1)
rb1.pack()
rb2 = tk.Radiobutton(root, text = 'Button -', variable = cal, value = 2)
rb2.pack()
rb3 = tk.Radiobutton(root, text = 'Button *', variable = cal, value = 3)
rb3.pack()
rb4 = tk.Radiobutton(root, text = 'Button /', variable = cal, value = 4)
rb4.pack()

button = tk.Button(root, text = 'Result', command = func)
button.pack()

label = tk.Label(root, text = '결과 표시창', underline = 3)
label.pack()

root.mainloop()



#야구 타자 게임
import random
import tkinter as tk
root = tk.Tk()

mScore = 0
out = 0
ans = 0

def func():
    score = []
    global mScore
    global out
    global ans
    for i in range(10):
        score.append(random.randint(1,10))
    print(score)
    for i in range(10):
        if int(textbox.get()) == int(score[i]):
            if i == 0 or i == 1 or i == 2:
                mScore += 1
                label.config(text = '1루타')
                break
            elif i == 3 or i == 4:
                mScore += 2
                label.config(text = '2루타')
                break
            elif i == 5:
                mScore += 3
                label.config(text = '3루타')
                break
            elif i == 6:
                mScore += 4
                label.config(text = '홈런')
                break
            else:
                label.config(text = '아웃')
                out += 1
                break
    print("현재",mScore,"아웃:",out,"총점",ans)
    if mScore >= 4:
        mScore = 0
        ans += 1
    elif out >= 3:
        label.config(text='게임 종료 : 총점은 %d점입니다'%ans)
        out = 0
        ans = 0
        mScore = 0

head = tk.Label(root, text = '야구타자게임')
head.pack()

textbox = tk.Entry(width=30)
textbox.pack()

button = tk.Button(root, text='Button', command = func)
button.pack()

label = tk.Label(root, text = '결과 표시창')
label.pack()

root.mainloop()
