#1
#간단한 OpenCV프로그래밍
import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8)
image.fill(200)     #혹은 image[:] = 200
#0을 넣으면 검정색이, 255를 넣으면 하얀색의 화면이 나온다
#256 이상의 값은 넣으면 안된다
#그런지만 결과는 255다음부터 계산이 된다 ex. 500 = 250이랑 같은 결과

cv2.imshow("Window title", image)
#키 입력 대기 시간으로 입력이 없으면 종료하는데, 0이면 무한대기
key = cv2.waitKey(0)
print('key : ', key)
cv2.destroyAllWindows()



#2
import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200    #회색 바탕

title1, title2 = 'Position1', 'Position2'    #윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)    #윈도우 이동
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)    #행렬 원소를 영상으로 표시
cv2.imshow(title2, image)
cv2.waitKey(0)    #키 이벤트 대기
cv2.destroyAllWindows()



#3
#WINDOW_AUTOSIZE vs. WINDOW_NORMAL
import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(255)    #모든 원소에 255(흰색) 지정

title1, title2 = 'AUTOSIZE', 'NORMAL'    #윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) #행렬 크기 변경 없이 윈도우 크기 변경(화면에 공백 있음)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) #표시되는 행력 크기변경되어 보여지며 윈도우 크기 변경
                                           #실제 행렬이 변경되는 것은 아님(화면에 공백 없음)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()    #열린 모든 윈도우 제거



#4
#반은 짙은회색, 반은 흰색으로 출력(WINDOW_AUTOSIZE와 WINDOW_NORMAL 차이 보기)
import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image[:100] = 100
image[100:] = 250

title1, title2 = 'AUTOSIZE', 'NORMAL'    #윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) #행렬 크기 변경 없이 윈도우 크기 변경(화면에 공백 있음)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) #표시되는 행력 크기변경되어 보여지며 윈도우 크기 변경
                                           #실제 행렬이 변경되는 것은 아님(화면에 공백 없음)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()    #열린 모든 윈도우 제거



#5
#키보드 이벤트 제어
import numpy as np
import cv2

#switch case문을 사전(dictionary)으로 구현
switch_case = {
    ord('a') : 'a키 입력',    #ord() 함수 - 문자를 아스키코드로 변환
    ord('b') : 'b키 입력',
    0x41 : 'A키 입력',
    int('0x42', 16) : 'B키 입력',    #16진수인 0x42를 10진수로 변환하면 66임
    2424832 : "왼쪽 화살표키 입력",    # 0x250000
    2490368 : "윗쪽 화살표키 입력",    # 0x260000
    2555904 : "오른쪽 화살표키 입력",    # 0x270000
    2621440 : "아래쪽 화살표키 입력"    # 0x280000
}

image = np.ones((200, 300), np.uint8)    #화소값이 1인 행렬 생성
cv2.namedWindow('Keyboard Event')    #윈도우 이름
cv2.imshow('Keyboard Event', image)
while True:    #무한 반복
    key = cv2.waitKeyEx(100)    #100ms 동안 키 이벤트 대기
    if key == 27:
        break    #ESC 키 누르면 종료
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1
cv2.destroyAllWindows()



