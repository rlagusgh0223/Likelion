#리스트와 튜플 응용하기

#1
#리스트에 요소 하나 추가하기
a = [10,20,30]
a.append(500)
print(a)        #[10, 20, 30, 500]
print(len(a))   #4

a = []
for i in range(10):
    a.append(i)
print(a)          #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = []
for i in range(10):
    a.append((i+1)*10)
print(a)    #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#1부터 100까지의 짝수를 리스트에 넣기
a = []
for i in range(1,101):
    if i%2 == 0:
        a.append(i)
print(a)


#2
#리스트 안에 리스트 추가
a = [10, 20, 30]
a.append([500,600])
print(a)        #[10, 20, 30, [500, 600]]
print(len(a))   #4


#3
#리스트 확장하기
a = [10, 20, 30]
a.extend([500,600])
print(a)        #[10, 20, 30, 500, 600]
print(len(a))   #5



#4
#리스트의 특정 인덱스에 요소 추가하기
#insert(인덱스,요소) 리스트의 특정 인덱스의
#앞에 요소 하나 추가
a = [10, 20, 30]
a.insert(2,500)
print(a)        #[10, 20, 500, 30]
print(len(a))   #4

#append처럼 insert를 쓰려면
#a.insert(len(a),500)쓰면 된다
#len(리스트)는 마지막 인덱스보다 1이 더 크기 때문에
#리스트 끝에 값을 추가할때 자주 활용


#5
#리스트의 특정 인덱스에 요소 추가하기

#insert는 요소 하나를 추가하므로 insert에 리스트를
#넣으면 append처럼 리스트 안에 리스트가 들어감
a = [10,20,30]
a.insert(1, [500,600])
print(a)    #[10, [500, 600], 20, 30]

a = [10,20,30]
a[1:1] = [500,600]
print(a)    #[10, 500, 600, 20, 30]


#6
#pop()은 리스트의 마지막 요소를 삭제한 뒤
#삭제한 요소를 반환
a = [10, 20, 30]
print(a.pop())  #30
print(a)        #[10, 20]


#7
#리스트에서 특정 인덱스의 요소 삭제
#pop(인덱스)는 해당 인덱스의 요소를 삭제한 뒤 반환
a = [10,20,30]
print(a.pop(1)) #20
print(a)        #[10, 30]

a = [10,20,30]
del a[1]
print(a)        #[10, 30]


#8
#리스트에서 특정 값을 찾아서 삭제
#remove(값)은 리스트에서 특정 값을 찾아서 삭제
a = [10,20,30]
a.remove(20)
print(a)        #[10, 30]

#리스트에서 같은 값이 여러개 있으면 처음값 삭제
a = [10,20,30,20]
a.remove(20)
print(a)        #[10, 30, 20]


#9
#리스트로 스택 만들기
a = []
for i in range(1,5):
    a.append(i*10)
    print(a)
for i in range(4):
    print(a.pop())


#10
#리스트로 큐 만들기
#pop(0)을 쓰면 먼저 입력한걸 뺄 수 있다
a = []
for i in range(1,5):
    a.append(i*10)
    print(a)
for i in range(4):
    print(a.pop(0))
    #print(a)
