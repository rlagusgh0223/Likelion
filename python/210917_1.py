#1
#텍스트 계산기 모범답안
import tkinter as tk
root = tk.Tk()
def func():
    nData1 = int(edit1.get())
    nData2 = int(edit2.get())
    nSel = sel.get()
    result = 0

#아래 부분 축소
#    if nSel == 1:
#        result = nData1 + nData2
#    elif nSel == 2:
#        result = nData1 - nData2
#    elif nSel == 3:
#        result = nData1 * nData2
#    elif nSel == 4:
#        if nData2 == 0:
#            lbl.config(text = '0으로 나눌 수 없습니다')
#            return
#        else:
#            result = nData1 / nData2
#    else:
#        lbl.config(text = '잘못된 연산자')
#        return
    if nSel == 4 and nData2 == 0:
            lbl.config(text = '0으로 나눌 수 없습니다')
            return
    else:
        result = eval(str(nData1) + but[nSel-1] + str(nData2))
        strResult = '%.2f'%result
        lbl.config(text = strResult)
        
        
        
    
    strResult = '%.2f'%result
    lbl.config(text = strResult)
nSel = 1

#텍스트 박스 생성 및 배치
edit1 = tk.Entry(root)
edit1.pack()
edit2 = tk.Entry(root)
edit2.pack()

#라디오 버튼 값을 저장하는 정수형 Variable 객체 생성
sel = tk.IntVar()
#sel에 1 할당
sel.set(1)

#라디오 버튼 1,2,3,4, 생성 및 배치
#rb1 = tk.Radiobutton(root, text = 'Button +', variable = sel, value = 1)
#rb1.pack()
#rb2 = tk.Radiobutton(root, text = 'Button -', variable = sel, value = 2)
#rb2.pack()
#rb3 = tk.Radiobutton(root, text = 'Button *', variable = sel, value = 3)
#rb3.pack()
#rb4 = tk.Radiobutton(root, text = 'Button /', variable = sel, value = 4)
#rb4.pack()

#위의 라디오 버튼 반복문으로 생성 및 배치
#4개일땐 별로 차이 안나지만 10개쯤 입력해야되면 확 줄어들것
rb = [0]*4
but = ['+', '-', '*', '/']
for i in range(4):
    rb[i] = tk.Radiobutton(root, text = 'Button'+but[i], variable = sel, value = i+1)
    rb[i].pack()

button = tk.Button(root, text = 'Result', command = func)
button.pack()

lbl = tk.Label(root, text = '결과 표시창')
lbl.pack()

root.mainloop()



#배치해보기 - place
import tkinter as tk
window = tk.Tk()
window.title('Educoding&IT')
window.geometry("320x400+100+100")#x대신 *나 대문자X를 쓰면 안된다
window.resizable(False, False)

b1 = tk.Button(window, text='(50, 50)')
b2 = tk.Button(window, text='(50, 100)')
b3 = tk.Button(window, text='(100, 150)')
b4 = tk.Button(window, text='(0, 200)')
b5 = tk.Button(window, text='(0, 300)')
b6 = tk.Button(window, text='(0, 300)')

b1.place(x=50, y=50)
b2.place(x=50, y=100, width=50, height=50)
b3.place(x=100, y=150, bordermode='inside')
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx=0.5)
b6.place(x=0, y=300, relx=0.5, anchor='s')

window.mainloop()



#계산기 만들어 보기
import tkinter as tk
window = tk.Tk()
window.title("계산기")
window.geometry("400x210") #창 크기
window.resizable(False,False) #창 고정

def monter(tm):
    global stri
    stri = stri+tm
    label.config(text = stri)
def zero():
    global stri
    stri = ''
    label.config(text = '0')
def calc():
    global stri
    result = eval(stri)
    label.config(text = result)

label = tk.Label(window, text='결과창')
label.pack()
stri=''

b1 = tk.Button(window, text='1', command = lambda:monter('1'))  #인자를 넘겨주기 위해 람다 사용
b2 = tk.Button(window, text='2', command = lambda:monter('2'))  #람다에서 함수를 사용하는 표현식 사용한것
b3 = tk.Button(window, text='3', command = lambda:monter('3'))
b4 = tk.Button(window, text='4', command = lambda:monter('4'))
b5 = tk.Button(window, text='5', command = lambda:monter('5'))
b6 = tk.Button(window, text='6', command = lambda:monter('6'))
b7 = tk.Button(window, text='7', command = lambda:monter('7'))
b8 = tk.Button(window, text='8', command = lambda:monter('8'))
b9 = tk.Button(window, text='9', command = lambda:monter('9'))
b0 = tk.Button(window, text='0', command = lambda:monter('0'))
p1 = tk.Button(window, text='+', command = lambda:monter('+'))
p2 = tk.Button(window, text='-', command = lambda:monter('-'))
p3 = tk.Button(window, text='*', command = lambda:monter('*'))
p4 = tk.Button(window, text='/', command = lambda:monter('/'))
bc = tk.Button(window, text='c', command = zero)
bm = tk.Button(window, text='=', command = calc)

b1.place(x=50, y=50,width=50, height=25)
b2.place(x=130, y=50, width=50, height=25)
b3.place(x=210, y=50, width=50, height=25)
b4.place(x=50, y=90, width=50, height=25)
b5.place(x=130, y=90, width=50, height=25)
b6.place(x=210, y=90, width=50, height=25)
b7.place(x=50, y=130, width=50, height=25)
b8.place(x=130, y=130, width=50, height=25)
b9.place(x=210, y=130, width=50, height=25)
bc.place(x=50, y=170, width=50, height=25)
b0.place(x=130, y=170, width=50, height=25)
bm.place(x=210, y=170, width=50, height=25)
p1.place(x=290, y=50, width=50, height=25)
p2.place(x=290, y=90, width=50, height=25)
p3.place(x=290, y=130, width=50, height=25)
p4.place(x=290, y=170, width=50, height=25)

window.mainloop()



#배치해보기 - grid 사용
#grid : 표 형태로 표현되는 프로그램
import tkinter as tk

root = tk.Tk()
root.title('레이아웃 테스트')

frame = tk.Frame(root)
frame.pack()

button0_0 = tk.Button(frame, text = '버튼0-0', width=20, bg='#00ffff')
button0_0.grid(row = 0, column = 0)

button0_1 = tk.Button(frame, text = '버튼0-1', width=20, bg='#ffc000')
button0_1.grid(row = 0, column = 1)

button1_0 = tk.Button(frame, text = '버튼1-0', width=20, bg='#ff9999')
button1_0.grid(row = 1, column = 0)

#button1_1 = tk.Button(frame, text = '버튼1-1', width=20, bg='#99ff99')
#button1_1.grid(row = 1, column = 1)

button2_0 = tk.Button(frame, text = '버튼2-0', width=20, bg='#99ff99')
button2_0.grid(row = 2, column = 0)

root.mainloop()


#grid에서 버튼 위치 행렬에 맞추지 않고 출력
import tkinter as tk

root = tk.Tk()
root.title('레이아웃 테스트')

frame = tk.Frame(root)
frame.pack()

button0_0 = tk.Button(frame, text = '버튼0-0', width=20, bg='#00ffff')
button0_0.grid(row = 0, column = 0)

button0_1 = tk.Button(frame, text = '버튼0-1', width=20, bg='#ffc000')
button0_1.grid(row = 0, column = 1, rowspan = 2)    #rowspan=2 : 위, 아래 두칸 차지

button1_0 = tk.Button(frame, text = '버튼1-0', width=20, bg='#ff9999')
button1_0.grid(row = 1, column = 0)

button2_0 = tk.Button(frame, text = '버튼2-0', width=20, bg='#99ff99')
button2_0.grid(row = 2, column = 0, columnspan = 2)     #columnspan=2 : 좌, 우 두칸 차지

root.mainloop()


#위에거에서 공간 꽉 채우기
import tkinter as tk

root = tk.Tk()
root.title('레이아웃 테스트')

frame = tk.Frame(root)
frame.pack()

button0_0 = tk.Button(frame, text = '버튼0-0', width=20, bg='#00ffff')
button0_0.grid(row = 0, column = 0)

button0_1 = tk.Button(frame, text = '버튼0-1', width=20, bg='#ffc000')
button0_1.grid(row = 0, column = 1, rowspan = 2, sticky = tk.W+tk.E+tk.N+tk.S)
# sticky = tk.W+tk.E+tk.N+tk.S : 내가 있는 공간 꽉 채우겠다

button1_0 = tk.Button(frame, text = '버튼1-0', width=20, bg='#ff9999')
button1_0.grid(row = 1, column = 0)

button2_0 = tk.Button(frame, text = '버튼2-0', width=20, bg='#99ff99')
button2_0.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W+tk.E+tk.N+tk.S)

root.mainloop()
