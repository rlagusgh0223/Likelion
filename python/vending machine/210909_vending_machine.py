total = 0                           #총 금액 입력 변수
print("돈을 투입하세요")

nMoney = {1:10000, 2:5000, 3:1000, 4:500, 5:100}
nDrink = {1:1200, 2:1100, 3:700, 4:1500, 5:1300}
nName = {1:"사이다", 2:"콜라", 3:"생수", 4:"주스", 5:"커피"}
nGet = [0,3,3,3,3,3]

#========================금액 입력===========================
while True:
    print("1:10,000원 / 2:5,000원 / 3:1,000원 / 4:500원 / 5:100원 / 0:입력완료 / 99:재고관리")
    cnt = int(input("금액번호를 고르세요 : "))       #0이 입력될때까지 금액을 받는 변수
    if cnt == 0:
        break
    elif 1 <= cnt <= 5:                  #1~5를 입력하면 해당 금액 total에 추가
        total += nMoney[cnt]
        print("누적금액 :",total,"원")
    #===============재고관리===============
    elif cnt == 99:
        while True:
            print("1:추가 2:제거 3:현재수량 0:처음으로")
            n1 = int(input())
            if n1 == 1:
                n2 = int(input("제품을 선택하세요"))
                if 1<= n2 <= 5:
                    print(nName[n2],"는 재고가",nGet[n2],"개 있습니다. 몇개를 추가하나요")
                    nPlus = int(input())
                    nGet[n2] += nPlus
                    print(nName[n2],"는 재고가",nGet[n2],"개로 변경되었습니다.")
                else:
                    print("잘못된 입력")
                    
            elif n1 == 2:
                n2 = int(input("제품을 선택하세요"))
                if 1<= n2 <= 5:
                    print(nName[n2],"는 재고가",nGet[n2],"개 있습니다. 몇개를 제거하나요")
                    nPlus = int(input())
                    if nGet[n2] <0:
                        print("재고가 부족합니다")
                    else:
                        nGet[n2] -= nPlus
                        print(nName[n2],"는 재고가",nGet[n2],"개로 변경되었습니다.")
                else:
                    print("잘못된 입력")
                    
            elif n1 == 3:
                for n3 in range(1,6):
                    print("현재수량 :",nName[n3],"=",nGet[n3])
                    
            elif n1 == 0:
                break
            
            else:
                print("잘못된 입력")
    #======================================
    else:
        print("잘못된 입력")         #보기 이외의 값일 경우 재입력
    print()
print("총 투입 금액은",total,"원입니다")

#========================음료수 입력===========================
drink = total                   #음료수 값을 뺀 잔액 변수(투입금과 잔액금을 출력해야 되므로)
while True:
    print('''[자판기 판매 메뉴]
1.사이다 가격 : 1200원
2.콜라   가격 : 1100원
3.생수   가격 : 700원
4.주스   가격 : 1500원
5.커피   가격 : 1300원
''')
    cnt = int(input("메뉴번호를 선택하세요[선택완료:0] : "))       #보기 중 음료 입력
    if cnt == 0:
        break
    elif 1 <= cnt <= 5:
        if drink<nDrink[cnt]:
            print("잔액이 부족합니다")
            continue
        drink -= nDrink[cnt]
        print(nName[cnt],"구입완료")
        print("잔액 :",drink)
    else:
        print("없는 음료입니다.")
    print()

#=======================잔액 계산===========================
print("투입 =",total,"잔액 =",drink)
print("거스름돈은 다음과 같습니다")

won = [10000, 5000, 1000, 500, 100]
Result = [0,0,0,0,0]
total = drink                          #최종적으로 얼마 반환했다고 나와야 되니까 total에 값을 넘기고 계산

for i in range(5):
    Result[i] = total//won[i]
    total -= Result[i]*won[i]
    if i<3:
        print(won[i],"원 :",Result[i],"장")
    else:
        print(won[i],"원 :",Result[i],"개")
print("자판기 종료, 잔액",drink,"반환")
