total = 0                           #총 금액 입력 변수
print("돈을 투입하세요")
#딕셔너리에 각 종목?과 금액을 넣으면 총 4개를 만들면 코드를 줄일 수 있을 것 같다
#리스트를 사용해도 그럴듯
while True:
    print("1:10,000원 / 2:5,000원 / 3:1,000원 / 4:500원 / 5:100원 / 0:입력완료")
    cnt = int(input("금액번호를 고르세요 : "))       #0이 입력될때까지 금액을 받는 변수
    if cnt == 0:
        break
    elif cnt == 1:
        total += 10000
        print("누적금액 :",total,"원")
    elif cnt == 2:
        total += 5000
        print("누적금액 :",total,"원")
    elif cnt == 3:
        total += 1000
        print("누적금액 :",total,"원")
    elif cnt == 4:
        total += 500
        print("누적금액 :",total,"원")
    elif cnt == 5:
        total += 100
        print("누적금액 :",total,"원")
    else:
        print("잘못된 입력")         #보기 이외의 값일 경우 재입력
    print()
print("총 투입 금액은",total,"원입니다")

drink = total                   #음료수 값을 뺀 잔액 변수(투입금과 잔액금을 출력해야 되므로)
while True:
    print("[자판기 판매 메뉴]")
    print("1.사이다 가격 : 1200원")
    print("2.콜라   가격 : 1100원")
    print("3.생수   가격 : 700원")
    print("4.주스   가격 : 1500원")
    print("5.커피   가격 : 1300원")
    print()
    cnt = int(input("메뉴번호를 선택하세요[선택완료:0] : "))       #보기 중 음료 입력
    if cnt == 0:
        break
    elif cnt == 1:
        if drink<1200:                  #해당 음료보다 잔액 부족할 경우 시스템 종료
            print("잔액이 부족합니다")
            continue                    #1200원은 안되지만, 더 저렴한 음료는 있으므로 continue
        drink -= 1200
        print("사이다 구입완료")
        print("잔액 :",drink)
    elif cnt == 2:
        if drink<1100:
            print("잔액이 부족합니다")
            continue
        drink -= 1100
        print("콜라 구입완료")
        print("잔액 :",drink)
    elif cnt == 3:
        if drink<700:
            print("잔액이 부족합니다")
            break                       #700원이 가장 적은값이므로 이것도 없으면 break
        drink -= 700
        print("생수 구입완료")
        print("잔액 :",drink)
    elif cnt == 4:
        if drink<1500:
            print("잔액이 부족합니다")
            continue
        drink -= 1500
        print("주스 구입완료")
        print("잔액 :",drink)
    elif cnt == 5:
        if drink<1300:
            print("잔액이 부족합니다")
            continue
        drink -= 1300
        print("커피 구입완료")
        print("잔액 :",drink)
    else:
        print("없는 음료입니다.")
    print()

print("투입 =",total,"잔액 =",drink)
print("거스름돈은 다음과 같습니다")

total = drink                          #최종적으로 얼마 반환했다고 나와야 되니까 total에 값을 넘기고 계산
print("잔액 :",total,"원")             #잔액 표시
Result = total//10000
print("만원 : ",Result,"장")           #total을 10000으로 나눈값의 몫 출력
total = total - Result*10000           #total에서 만원 단위의 값 제거
Result = total//5000
print("오천원 : ",Result,"장")
total = total - Result*5000
Result = total//1000
print("천원 : ",Result,"장")
total = total - Result*1000
Result = total//500
print("오백원 : ",Result,"개")
total = total - Result*500
Result = total//100
print("백원 : ",Result,"개")
print("자판기 종료, 잔액",drink,"반환")
"""
#잔액을 구하는 다른 방법
x = 잔액
Cost = [10000,5000,1000,300,100]
Count = [0,0,0,0,0]
for i in range(5):        #ex) 297000이면 10000으로 나누면
    Count[i] = x//Cost[i]     #몫이 2(나머지는 버리는 연산자 사용)를 Count에 넣음
    x -= Cost[i]*Count[i]    #x는 29700에서 20000원을 뺀 9700
#divmod(,):몫과 나머지로 나눈다
"""
