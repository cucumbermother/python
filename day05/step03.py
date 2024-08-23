# 반복문 실습1 : 구구단 출력
# (1) 구구단 2단 출력
    # 반복문 없이 , 반복되는 코드 : print(f ' 2 * = { 2 * })
    # 반복 되지 않는 코드 : 1 ~ 9

# print(f'2 x 1 = { 2*1 }')
# print(f'2 x 2 = { 2*2 }')
# print(f'2 x 3 = { 2*3 }')
# print(f'2 x 4 = { 2*4 }')
# print(f'2 x 5 = { 2*5 }')
# print(f'2 x 6 = { 2*6 }')
# print(f'2 x 7 = { 2*7 }')
# print(f'2 x 8 = { 2*8 }')
# print(f'2 x 9 = { 2*9 }')
    # 반복문 변경

# 곱수는 1 부터 10미만
for 곱수 in range( 1 , 10 ) :
    print(f'2 x {곱수} = { 2 * 곱수 }')

# (2) 구구단 출력 , for중첩
# 2-1 단수 출력 , 2단 ~ 9단
# 단수는 2부터 10미만까지 1씩 증가하면서 단수 변수에 대입반복
for 단수 in range( 1 , 10 ) :
    print(단수)

# 2-2 곱 수 출력
# 곱수는 1부터 10 미만 1 씩 증가하면서 곱수 변수 대입 반복
for 곱수 in range (1 , 10 , 1) :
    print(곱수)

# 2-4 합치기, 단 마다 곱 계산 O , 곱 마다 단 계산 X
for 단수 in range ( 2 , 10 , 1 ) : # 2 ~ 9 : 총 8 회 반복
    for 곱수 in range(1 , 10, 1) : # 단 1회전 할때 곱 9회전
        # 총 9회 반복 중복 반복문 * 상위 반복횟수 => 총 72회 반복
        print(f'{ 단수 } x { 곱수 } = { 단수 * 곱수 }')



# 반복문 실습 2 : 키보드부터 끝값을 입력받아 1부터 끝값까지 누적합계를 구하시오


# 1부터 x까지의 누적합계
sum = 0
x = int(input('끝값을 입력해주세요 : '))
for var in range ( 1 , x+1, 1 ) :
    print(var) # 현재 반복문 변수의 무엇의 값이 들었는지 확인
    sum += var
print(sum)


# 조건 1. 값이 홀수일때만 누적합계
# continue 키워드 : 가장 가까운 반복문으로 이동하는 키워드 ( 증강식 )
# 조건 2. 1000 이상되면 누적합계를 계산을 종료한다.
# break 키워드 : 가장 가까운 반복문의 탈출/ (강제)종료

sum = 0
x = int(input('끝값을 입력해주세요 : '))
for var in range ( 1 , x+1  ) :
    #조건 1
    if var % 2 == 0 : # 만약에 현재 반복변수의 값을 나누기 2을때 나머지가 1이면 (짝슈)
        continue
        # continue: 반복문 안에서 사용되는 키워드 # 가장 가까운 반복문으로 이동 # continue 만나게 되면 아래코드는 실행되지 않음
    sum += var # 위에서 continue를 만나면 실행안됨! # continue 만나는 조건 : var % 2 == 1

    #조건 2
    if sum >= 1000 :
        break # 반복문 안에서 사용되는 키워드 (문법)
        # 가장 가까운 반복문을 탈출/강제종료 하는 코드 # break를 만나게 되면 아래 코드는 실행되지 않는다.
print(sum)


# 반복문 실습3 : 키보드로부터 입력을 무한루프(무한반복) 받아서 만약에 'x'이면 무한반복 하시오.
    # 무한루프의 주의할점 : 종료되는 조건을 판단 , break 키워드와 주로 사용된다.
while True : # while 반복문 # while 조건식 : # while True : 무한 루프
    print('무한반복')
    str = input('무한입력: ')
    if str == 'x' : # 만약에 입력받은 값이 x이면
        break