#1
#마우스 이벤트 제어
import numpy as np
import cv2

#콜백 함수 : event값에 따른 마우스 버튼 종류 구분
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")
        
image = np.full((200, 300), 255, np.uint8)    #영상 생성

title1, title2 = "Mouse Event1", "Mouse Event2"    #윈도우 이름
cv2.imshow(title1, image)    #영상보기
cv2.imshow(title2, image)

cv2.setMouseCallback("Mouse Event1", onMouse)    #마우스 콜백 함수
cv2.waitKey(0)    #키 이벤트 대기
cv2.destroyAllWindows()    #열린 모든 윈도우 제거



#2
#트랙바 이벤트 제어
import numpy as np
import cv2

def onChange(value):    #트랙바 콜백 함수
    global image    
    print('value 값 :', value)
    image = np.zeros((300, 500), np.uint8)    #영상 data 초기화
    image = image + value    #행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)
    
image = np.zeros((300, 500), np.uint8)    #영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)

#트랙바 콜백 함수 등록
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()



#3
#트랙바 이벤트 제어
import numpy as np
import cv2
def onChange(value):
    global image, title
    image = np.zeros((300, 500), np.uint8)    #영상 data 초기화
    image = image + value
    cv2.imshow(title, image)
    
def onMouse(event, x, y, flags, param):    #마우스 콜백 함수
    global image, bar_name
    if event == cv2.EVENT_RBUTTONDOWN:
        if image[0][0] < 246:
            image = image+10
        cv2.setTrackbarPos(bar_name, title, image[0][0])    #트랙바 위치 변경
        cv2.imshow(title, image)
        
    elif event == cv2.EVENT_LBUTTONDOWN:
        if image[0][0] >= 10:
            image = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])    #트랙바 위치 변경
        cv2.imshow(title, image)
            
image = np.zeros((300, 500), np.uint8)
title = 'Trackbar & Mouse Event'    #윈도우 이름
bar_name = 'Braightness'    #트랙바 이름
cv2.imshow(title, image)
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)    #트랙바 콜백 함수
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)    #키 입력 대기
cv2.destroyAllWindows()    #모든 윈도우 닫기



#4
#직선 및 사각형 그리기
import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)    #색상 선언(B, G, R)
image = np.zeros((400, 600, 3), np.uint8)    #3채널 컬러 영상 생성
image[:] = (255, 255, 255)    #컬러라는 의미

pt1, pt2 = (50, 50), (250, 150)    #좌표 선언 - 정수형 튜플
pt3, pt4 = (400, 150), (500, 50)    #녹색 대각선
roi = 50, 200, 200, 100

#직선 그리기
cv2.line(image, pt1, pt2, red)    #pt1 ~ pt2까지 red(파란테두리 사각형의 빨간 대각선)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)#계단 현상이 감소한 선#pt3 ~ pt4까지 green(두번째 대각선)

#사각형 그리기
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)    #4방향 연결선    #파란 테두리 사각형
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)    #빨간 테두리 사각형
cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED)    #내부 채움(녹색 사각형)

cv2.imshow('Line & Rectangle', image)    #윈도우에 영상 표시
cv2.waitKey(0)
cv2.destroyAllWindows()    #모든 열린 윈도우 닫기


#5
#글자 쓰기
import numpy as np
import cv2

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 200), (50, 260)    #문자열 위치 좌표

image = np.zeros((300, 500, 3), np.uint8) #3은 R,G,B의 컬러 이미지를 만든다는 소리
image.fill(255)

cv2.putText(image, "SIMPLEX", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, brown)
                                                    #폰트 종류, 두께, 색
cv2.putText(image, "DUPLEX", (50, 130), cv2.FONT_HERSHEY_DUPLEX, 3, olive)
cv2.putText(image, "TRIPLEX", pt1, cv2.FONT_HERSHEY_TRIPLEX, 2, violet)

fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC    #글자체 상수
cv2.putText(image, "ITALIC", pt2, fontFace, 4, violet)

cv2.imshow("Put Text", image)
cv2.waitKey(0)    #키 이벤트 대기
cv2.destroyAllWindows()



#6
#원 그리기
import numpy as np
import cv2

orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)
image = np.full((300, 500, 3), white, np.uint8)    #컬러 영상 생성 및 초기화

center = (image.shape[1]//2, image.shape[0]//2)    #영상의 중심 좌표
pt1, pt2 = (300, 50), (100, 220)
shade = (pt2[0] + 2, pt2[1] + 2)    #그림자 좌표(동일한 text를 약간 겹쳐 그림자 효과)
cv2.circle(image, center, 100, blue)    #원 그리기
cv2.circle(image, pt1, 50, orange, 2)
cv2.circle(image, pt2, 70, cyan, -1)    #원 내부 채움

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, 'center_blue', center, font, 1.0, blue)
cv2.putText(image, 'pt1_orange', pt1, font, 0.8, orange)
cv2.putText(image, 'pt2_cyan', shade, font, 1.2, black, 2)    #그림자 효과
cv2.putText(image, 'pt2_cyan', pt2, font, 1.2, cyan, 1)

title = 'Draw circles'
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#7
#타원 그리기
import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)    #색상 지정
image = np.full((300, 700, 3), white, np.uint8)

pt1, pt2 = (180, 150), (550, 150)    #타원 중심점
size = (120, 60)    #타원 크기 - 반지름 값임

cv2.circle(image, pt1, 1, 0, 2)    #타원의 중심정(2개의 픽셀 점) 표시
cv2.circle(image, pt2, 1, 0, 2)

cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1)    #타원 그리기
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 4)    #호 그리기
cv2.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

cv2.imshow("Draw Eclipse & Arc", image)
cv2.waitKey()
cv2.destroyAllWindows()
