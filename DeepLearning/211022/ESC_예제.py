import socket
from _thread import *
from pynput import keyboard
import time
import threading
import sys
bLoopEnd = False
start_time = 0
end_time = 0
calc_time = 0
nT_Count = 0
def MainLoop():
    print("program start")

def on_press(key):    #키보드 눌리는 event시 처리 : client 전송 data 입력도 표시 되므로 막아둠
    try:
        print("Alphanumeric key pressed : {0}".format(key.char))
    except AttributeError:
        print('special key pressed : {0}'.format(key))

def on_release(key):
    global bLoopEnd    #전역변수 bloopEnd 사용(종료 처리용)
    #print('Key released : {0}'.format(key)) #눌린 키 확인용 print 막아둠
    if key == keyboard.Key.esc:
        print("======================esc======================")
        bLoopEnd = True
        return False

def threaded():
    global start_time
    global end_time
    global calc_time
    global nT_Count

    start_time = time.time()
    while True:
        if bLoopEnd == True:
            print('Program close')
            sys.exit()
            break
        else:
            end_time = time.time()
            calc_time = end_time - start_time
            #print(calc_time)
            if calc_time > 1:
                start_time = time.time()
                nT_Count += 1
                print("thread count : ", nT_Count)

start_new_thread(threaded, ())
#keyboard Listner를 등록
#Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:#키가 눌리면 on_press, 떨어지면 on_release
    print("keyboard event 등록")
    listener.join()

MainLoop()
