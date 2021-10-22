import socket
from _thread import *
from pynput import keyboard
import time
import threading
import sys

#bLoopEnd = False
bClientWaitEnd = False
bServerLoopEnd = False

def MainLoop():
    #if bLoopEnd == False:   #키보드 이벤트인 on_release에서 ESC가 눌리면 bLoopEnd 상태 변화
        #threading.Timer(0.1, MainLoop).start()
    if bServerLoopEnd == False:
        threading.Timer(0.1, MainLoop).start()
        
    else:   #ESC키가 눌려서 종료되면 server를 닫아줌
        print('Server close')
        server_socket.close()
        sys.exit()

def on_press(key):    #키보드 눌리는 event시 처리 : client 전송 data 입력도 표시 되므로 막아둠
    """
    try:
        print("Alphanumeric key pressed : {0}".format(key.char))
    except AttributeError:
        print('special key pressed : {0}'.format(key))
"""
def on_release(key):
    #global bLoopEnd    #전역변수 bloopEnd 사용(종료 처리용)
    global bClientWaitEnd
    
    #print('Key released : {0}'.format(key)) #눌린 키 확인용 print 막아둠
    if key == keyboard.Key.esc:
        print("======================esc======================")
        bClientWaitEnd = True
        #bLoopEnd = True
        return False

#스레드에서 실행되는 코드
"""
def ClientChkThreaded(i):
    while True:
        print("ClientChkThreaded wait!!!")
        client_socket, addr = server_socket.accept()    #새로운 client thread 접속할때까지 대기
        #print(type(client_socket))
        #print(type(addr))
        print("client_socket connected!!", addr)
        threaded(client_socket, addr)   #계속 loop를 돌면서 새로운 client thread 생성
"""
def ClientChkThreaded(i):
    global bClientWaitEnd
    global bServerLoopEnd
    while True:
        print("ClientChkThreaded wait!!!")

        server_socket.settimeout(1)
        if bClientWaitEnd == False:
            try:
                client_socket, addr = server_socket.accept()
            except socket.timeout:
                continue
            server_socket.settimeout(None)
            print("client_socket connected!!", addr)
            threaded(client_socket, addr)

        else:
            print("KeyboardInterrupt")
            bServerLoopEnd = True
            break

#접속한 클라이언트마다 새로운 스레드가 생성되어 통신을 하게됨
def threaded(client_socket, addr):
    print("Connected by :", addr[0], ":", addr[1])

    #클라이언트가 접속을 끊을 때 까지 반복
    while True:
        try:
            #데이터가 수신되면 클라이언트에 다시 전송(에코)
            data = client_socket.recv(1024)
            if not data:
                print("Disconnected by " + addr[0], ':', addr[1])
                break
            
            print('Received from ' + addr[0], ':', addr[1], data.decode())
            
            client_socket.send(data)
            
        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
    print("end")
    client_socket.close()

HOST = '127.0.0.1'
PORT = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')

i = 0
start_new_thread(ClientChkThreaded, (i,))
MainLoop()

#keyborad Listner를 등록
#Collect events until released
#키가 눌리면 on_press, 떨어지면 on_release
#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
