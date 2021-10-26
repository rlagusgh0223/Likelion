#1
#영상 파일 읽기
import cv2
def print_matInfo(name, image):
    if image.dtype == 'uint8': mat_type = 'CV_8U'
    elif image.dtype == 'int8': mat_type = 'CV_8S'
    elif image.dtype == 'uint16': mat_type = 'CV_16U'
    elif image.dtype == 'int16': mat_type = 'CV_16S'
    elif image.dtype == 'float32': mat_type = 'CV_32F'
    elif image.dtype == 'float64': mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1
    ## depth, channel 출력
    print("%12s : depth(%s), channels(%s) -> mat_type(%sC%d)"
          %(name, image.dtype, nchannel, mat_type, nchannel))
    
title1, title2 = 'gray2gray', 'gray2color'    #윈도우 이름
#주피터일 경우 파일이 저장되는 공간에 images 파일을 만들고 거기에 사진을 저장하면 image/read_gray.jpg만 써도 된다
gray2gray = cv2.imread('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/read_gray.jpg', cv2.IMREAD_GRAYSCALE)    #영상 파일 적재
gray2color = cv2.imread('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/read_gray.jpg', cv2.IMREAD_COLOR)
if (gray2gray is None or gray2color is None):    #예외처리 - 영상 파일 읽기 여부 조사
    raise Exception("영상파일 읽기 에러")
#행렬 내 한 화소 값 표시
print("행렬 좌표 (100, 100) 화소값")
print("%s %s" %(title1, gray2gray[100,100]))
print("%s %s\n" % (title2, gray2color[100,100]))
print_matInfo(title1, gray2gray)
print_matInfo(title2, gray2color)
cv2.imshow(title1, gray2gray)
cv2.imshow(title2, gray2color)
cv2.waitKey(0)
cv2.destroyAllWindows()



#2
#행렬을 영상파일로 저장
import cv2

image = cv2.imread('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/read_color.jpg', cv2.IMREAD_COLOR)    #컬러로 읽기
if image is None: raise Exception("영상 파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)    #JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]    #PNG 압축 레벨 설정

#행렬을 영상 파일로 저장

cv2.imwrite('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/write_test1.jpg', image)    #디폴트는 95
cv2.imwrite('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/write_test2.jpg', image, params_jpg)    #지정 화질로 저장
cv2.imwrite('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/write_test3.png', image, params_jpg)
cv2.imwrite('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/write_test4.bmp', image)    #BMP 파일로 저장
print("저장 완료")



#3
#기본 배열(Array) 처리 함수
import cv2

image = cv2.imread('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/flip_test.jpg', cv2.IMREAD_COLOR)    #컬러로 읽기
if image is None: raise Exception("영상 파일 읽기 에러")
    
x_axis = cv2.flip(image, 0)    #x축 기준 상하 뒤집기
y_axis = cv2.flip(image, 1)    #y축 기준 좌우 뒤집기
xy_axis = cv2.flip(image, -1)
rep_image = cv2.repeat(image, 1, 2)    #반복 복사
#전치 행렬은 행과 열을 교환하여 얻는 행렬
#즉, 주대각선을 축으로 하는 반사 대칭을 가하여 얻는 행렬
trans_image = cv2.transpose(image)   #행렬 전치
#각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis', ' xy_axis', 'rep_image', 'trans_image']
for title in titles:
    cv2.imshow(title, eval(title))    #eval : 문자열을 명령어로 만듦 - 행렬 변수로 적용
cv2. waitKey(0)
cv2.destroyAllWindows()




#4
#채널 처리 함수
import numpy as np
import cv2

#numpy array 이용해 단일 채널 3개 생성
ch0 = np.zeros((2, 4), np.uint8) + 10    #0원소 행렬 선언 후 10 더하기
ch1 = np.ones((2, 4), np.uint8) * 20    #1원소 행렬 선언 후 20 곱하기
ch2 = np.zeros((2, 4), np.uint8); ch2[:] = 30    #0원소 행렬 선언 후 행렬원소값 30 지정

list_bgr = [ch0, ch1, ch2]    #단일 채널들을 모아 리스트 구성
merge_bgr = cv2.merge(list_bgr)    #채널 합성
split_bgr = cv2.split(merge_bgr)    #채널 분리 : 컬러영상 -> 3채널 분리

print('split_bgr 행렬 형태', np.array(split_bgr).shape)
print('merge_bgr 행렬 형태', merge_bgr.shape)

print("[ch0] = \n%s" %ch0)    #단일 채널 원소 출력
print("[ch1] = \n%s" %ch1)
print("[ch2] = \n%s" %ch2)
print("[merge_bgr] = \n%s\n" %merge_bgr)    #다중 채널 원소 출력

print("[split_bgr[0]] = \n%s" %split_bgr[0])
print("[split_bgr[1]] = \n%s" %split_bgr[1])
print("[split_bgr[2]] = \n%s" %split_bgr[2])



#5
#영상 채널 분리
import cv2

image = cv2.imread('C:/Users/Owner/Desktop/khh/git/Likelion/DeepLearning/211026/color.jpg', cv2.IMREAD_COLOR)    #영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")    #예외 처리
if image.ndim != 3: raise Exception("컬러 영상 아님")
    
bgr = cv2.split(image)    #채널 분리 : 컬러영상 -> 3채널 분리
#blut, green, red = cv2.split(image)
print("bgr 자료형 :", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소 개수 :", len(bgr))

#각 채널을 윈도우에 띄우기
cv2.imshow("image", image)
cv2.imshow("Blue channel", bgr[0])    #blue 채널
cv2.imshow("Green channel", bgr[1])    #bgreen 채널
cv2.imshow("Red channel", bgr[2])    #red 채널
#cv2.imshow("Blue channel", image[:,:,0])    #넘파이 객체 인덱싱
#cv2.imshow("Green channel", image[:,:,0])
#cv2.imshow("Red channel", image[:,:,0])
cv2.waitKey()
cv2.destroyAllWindows()


#6
#사칙 연산
import numpy as np, cv2

m1 = np.full((3, 6), 10, np.uint8)    #단일 채널 생성 및 초기화
m2 = np.full((3, 6), 50, np.uint8)
m_mask = np.zeros(m1.shape, np.uint8)     #마스크 생성
m_mask[ :, 3:] = 1    #관심 영역을 지정한 후, 1을 할당

m_add1 = cv2.add(m1, m2)    #행렬 덧셈
m_add2 = cv2.add(m1, m2, mask=m_mask)   #관심 영역만 덧셈 수행

#행렬 나눗셈 수행
m_div1 = cv2.divide(m1, m2)
m1 = m1.astype(np.float32)    #형변환 - 소수 부분 보존
m2 = np.float32(m2)
m_div2 = cv2.divide(m1, m2)

titles = ['m1', 'm2', 'm_mask', 'm_add1', 'm_add2', 'm_div1', 'm_div2']
for title in titles:
    print("[%s] = \n%s\n" % (title, eval(title)))



#7
#논리(비트) 연산 함수
import numpy as np, cv2

image1 = np.zeros((300, 300), np.uint8)    #300행, 300열 검은색 영상 생성
image2 = image1.copy()

h, w = image1.shape[:2]
cx, cy = w//2, h//2
cv2.circle(image1, (cx,cy), 100, 255, -1)    #중심에 원 그리기, 끝에 -1은 내부 채움
cv2.rectangle(image2, (0,0,cx,h), 255, -1)

image3 = cv2.bitwise_or(image1, image2)    #원소 간 논리합
image4 = cv2.bitwise_and(image1, image2)    #원소 간 논리곱
image5 = cv2.bitwise_xor(image1, image2)    #원소 간 배타적 논리합
image6 = cv2.bitwise_not(image1)    #행렬 반전

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("bitwise_or", image3)
cv2.imshow("bitwise_and", image4)
cv2.imshow("bitwise_xor", image5)
cv2.imshow("bitwise_not", image6)
cv2.waitKey(0)
cv2.destroyAllWindows()
