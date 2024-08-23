'''
제어문 : 특정 상황에 따라 코드 흐름을 제어
    - If (조건문)
    - For (반복문)


조건문 문법
    1. 조건식 : True or False, 비교연산 조건, 논리연산 조건, 변수 등등
    2. 들여쓰기 : 해당 조건이 충족했을때 실행되는 구역
    3. 실행문 : 조건이 True or False 일때 실행되는 코드

조건문 형태 종류
    1.
        if 조건식 :
            참1
    2.  if 조건식 :
            참
        else :
            거짓
    3.  if 조건식1 :
        elif 조건식2
            참1
        elif 조건식3
            참2
        else
            참3
[주의할점]
if 조건식1 :
    실행문 <---- 조건식1 실행문
    if 조건식2 :
        실행문2  <---- 조건식2 실행문
    실행문3 <---- 조건식1 실행문
'''


# 조건문 실습1 : 변수와 조건문의 활용
    # 3개의 정수를 입력받아 가장 큰수를 출력하시오

# (1)

a = int(input('정수를 입력해주세요 : '))
b = int(input('정수를 입력해주세요 : '))
c = int(input('정수를 입력해주세요 : '))

# (2) 가장 큰 수를 저장하는 변수를 임의로 생성
max = a # 첫번째 입력받은 값을 가장 큰 수로 대입,

# (3) 비교
if max < b : # 만약에 두번째 값이 max보다 크면
    max = b # max에 두번째 값을 대입
if max <  c : # 만약에 세번째 값이 max보다 크면
    max = c  # max에 세번째 값을 대입

print(f'max = { max }')
    # 다중 조건에 모슨 다중 검사 if~ if~ if~
    # 다중 조건에 특정 조건이 충족했을때 종료검사 if~ elif


# 조건문 실습2 : 변수와 조건문의 활용
    # 3개의 정수를 입력받아 내림차순으로 출력

if a < b : # 만약에 첫번째 값이 두번째 값보다 작으면
    a , b = b , a  # 두 변수 간의 값 교체 ( 스왑 )
if a < c :
    a , b = c , a
if b < c :
    b , c = c , b

print(f'{a},{b},{c}')



# 스왑 : 두 변수간의 값 바꾸기
    # 고려 : 변수는 하나의 값만 저장, 컴퓨터는 순차 처리한다. ( 주면서 받기x )
var1 = 3
var2 = 5
print(f'{ var1 } , { var2 }')
# var2 = var1 # var1의 값을 var2에 대입하면 var2에 있던 값이 사라짐.
# print(f'{ var1 } , { var2 }')

# ( 스왑방법1 ) 임시변수 temp : 두 변수간의 스왑할때 임시로 값 저장하고 있는 변수
temp = var1
var1 = var2
var2 = temp
print(f'{ var1 },{ var2 }') # 5 , 3

# ( 스왑방법2 ) # 파이썬만 가능
var1 , var2 = var2 , var1

print(f'{ var1 } , { var2 }') # 3 , 5