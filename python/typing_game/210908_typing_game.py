import time
#경과시간 = end - start
import random
print('타자게임 준비되면 Enter')
input()                                 #엔터 누른 후 게임이 시작되게 하기 위해(엔터가 아니어도 가능) 
Start = time.time()                     #시작시간 입력
eng = ['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf','python','k-digital']

for cnt in range(1,6):                  #5회 반복을 위한 반복문
    print('*문제',cnt)
    num = random.randint(0,len(eng)-1)  #임의의 수 랜덤하게 생성(0 ~ 리스트수-1만큼)
    strShow = eng[num]                  #랜덤한 수에 해당하는 리스트의 값 변수에 입력
    print(strShow)
    strInput = input()                  #사용자의 타자 입력
    while strInput != strShow:          #사용자의 입력값과 영어단어 불일치시 맞을때까지 무한반복
        print("다시 입력하시오")
        print(strShow)
        strInput = input()
    del eng[num]                        #사용한 단어 삭제(중복 방지)
End = time.time()                       #끝 시간 입력
nTime = End - Start                     #사용시간 계산
print(round(nTime,2),"초")              #사용시간 출력(소수점 둘째자리까지)



#============================모범답안================================
import random
import time
w = ['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf','python','k-digital']

n=1
print('타자게임 준비되면 Enter')
input()
start = time.time()
q = random.choice(w)
while n<=5:
    print('*문제',n)
    print(q)
    x = input()
    if q==x:
        print('통과!')
        n = n+1
        q = random.choice(w)
    else:
        print('오타! 다시 도전!')
end = time.time()
et = end - start
print('타자 시간 : ',round(et,2),"초")
#====================================================================
