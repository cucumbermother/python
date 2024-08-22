'''

함수
     - 함(집합/구역/상자), 수(숫자)
     - 상자 안에 들어있는 숫자 / 집합
     - 상자 안에 들어있는 코드들
     - 실행문을 기억함
     - 용어
        인자값 : 함수 안으로 들어가는 값 예) print(인자값)
        리턴값 : 함수가 종료되면서 돌려주는 반한값


'''



'''

입력함수 : input("프롬프트 문자")
연산자 : 
    1. 산술 연산자
    2. 비교 연산자
    3. and ,  or , not
    4. 복합대입연산자 : 좌항 = 우항 , (산술연산자)= 연산후에 대입

'''

x = 10
y = 3
z = 1


print( f' 산술연산자 : { x + y } , { x - y } , { x * y } , { x / y } , { x // y } , { x % y} , { x ** y } ')
print( f' 비교연산자 : { x > y } , { x < y} , { x >= y } , { x <= y } , { x == y } , { x != y }')
print( f' 논리연산자 : { x >= y and y <= z } , { x >= y or y <= z} , { not(x >= y) }')
x += 2
print( x ) # 12
x %= 7
print( x ) # 5 ( 나머지 )


# 1

won = int(input("금액을 입력해 주세요 : "))
sipman = won // 100000 # 갯수
man = (won - sipman * 100000 ) // 10000
chun = (won - (sipman * 100000 + man * 10000 ) )// 1000
back = (won - (sipman * 100000 + man * 10000 + chun * 1000)) // 100
sip = (won - (sipman * 100000 + man * 10000 + chun * 1000 + back * 100) ) // 10
print( f' 십만원권: {sipman}개 , 만원권 : {man}개 , 천원권 : {chun}개 , 백원 : {back}개 , 십원 : {sip}개 ')




#2

korean = int(input("국어점수를 입력해 주세요 : "))
eng = int(input("영어점수를 입력해 주세요 : "))
math = int(input("수학점수를 입력해 주세요 : "))

# [1] 평균 90 이상 국어 95 이상 '국어우수' 아니면 '장려'

test = "국어우수" if (korean + eng + math) / 3 >= 90 and korean >= 95 else "장려"

print(test)


