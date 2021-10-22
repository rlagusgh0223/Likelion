#예외 처리 사용하기
#예외(exception)란 코드를 실행하는 중에 발생한 에러를 뜻함
"""
def ten_div(x):
    try:    #실행할 코드
        return 10/x   #0을 넣으면 에러남
    except: #예외가 발생했을 때 처리하는 코드
        print("예외 발생")

print(ten_div(0))


#좀더 구체적
y = [10, 20, 30]

try:
    index, x = map(int, input("인덱스와 나눌 숫자를 입력 : ").split())
    print(y[index] / x)
except ZeroDivisionError:   #숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print("숫자를 0으로 나눌 수 없습니다.")
except IndexError:  #범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print("잘못된 인덱스입니다.")


#좀더 구체적
y = [10, 20, 30]

try:
    index, x = map(int, input("인덱스와 나눌 숫자를 입력 : ").split())
    print(y[index] / x)
except ZeroDivisionError as e:    #as 뒤에 변수를 지정하면 에러를 받아옴
    print("숫자를 0으로 나눌 수 없습니다.", e)    #e에 저장된 에러 메시지 출력
except IndexError as e:
    print("잘못된 인덱스입니다.", e)



#else와 finally 사용하기
try:
    x = int(input('나눌 숫자 : '))
    y = 10/x
except ZeroDivisionError:   #숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print("숫자를 0으로 나눌수 없습니다.")
else:
    print(y)



#finally는 except와 else를 생략할 수 있음
try:
    x = int(input("나눌 숫자 : "))
    y = 10 / x
except ZeroDivisionError:   #숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print("숫자를 0으로 나눌 수 없음")
else:       #try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:    #예외 발생 여부와 상관없이 항상 실행됨
    print("코드 실행 끝")



#예외 발생시키기
#raise 예외("에러메시지")
try:
    x = int(input("3의 배수 : "))
    if x % 3 != 0:                                  #x가 3의 배수가 아니면
        raise Exception("3의 배수가 아닙니다.")     #예외를 발생시킴
    print(x)
except Exception as e:          #예외가 발생했을 때 실행됨
    print("예외가 발생했습니다.",e)



#raise의 처리과정
#다음은 함수 안에서 raise를 사용하지만 함수 안에는 try except가 없는 상태임
def three_multiple():
    x = int(input("3의 배수 : "))
    if x % 3 != 0:  #x가 3의 배수가 아니면
        raise Exception("3의 배수가 아닙니다.") #예외를 발생시킴. try-except가 없으면 에러남
    print(x)     #현재 함수 안에는 except가 없으므로 예외를 상위 코드 블록으로 넘김

try:
    three_multiple()
except Exception as e:      #하위 코드 블록에서 예외가 발생해도 실행됨
    print("예외가 발생했습니다.", e)



#except 안에서 raise를 사용하면 현재 예외를 다시 발생시킴(re-raise)
def three_multiple():
    try:
        x = int(input("3의 배수 : "))
        if x % 3 != 0:  #x가 3의 배수가 아니면
            raise Exception("3의 배수가 아닙니다.") #예외를 발생시킴.
        print(x)     
    except Exception as e:  #함수 안에서 예외 처리
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise   #raise로 현재 다시 발생시켜서 상위 코드 블록으로 넘김

try:
    three_multiple()
except Exception as e:      #하위 코드 블록에서 예외가 발생해도 실행됨
    print("스크립트 파일에서 예외가 발생했습니다.", e)
"""


#예외 만들기(입력된 숫자가 3의 배수가 아닐 때 발생시킬 예외)
class NotThreeMultipleError(Exception): #Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다')

def three_multiple():
    try:
        x = int(input('3의 배수 입력 : '))
        if x % 3 != 0:  #x가 3의 배수가 아니면
            raise NotThreeMultipleError    #NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print("예외가 발생했습니다.", e)

three_multiple()
