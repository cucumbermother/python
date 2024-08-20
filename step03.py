'''

1. 연산자
2. 연산자의 종류
    대입 연산자를 제외한 연산자 1개당 연산 결과의 자료값은 1개
    1. 산술 연산자 : + 더하기, - 빼기 , ** 제곱, / 나누기,  // 몫, % 나머지
    2. 연결연산자 : + 문자열연결, ,(쉼표) 문자열연결
    3. 비교연산지 : >초과, <미만, >=이상, <= 이하, == 같다 , != 같지않다
    4. 논리연산자 :
         and 이면서 이고 그리고,  모두 True 이면 결과도 True, 하나라도 False 이면 결과도 False
         or 이거나 거나 하나라도, 하나라도 True이면 결과도  True
        #not 부정 반대 , True -> False , False -> True
    5. 대입 연산자, 복합대입연산자
        1. = 오른쪽 값을 왼쪽에 대입
        2. +=. -=, **= , /= , //=, %=
            복합대입연산자

'''


# [1] 산술 연산자, 반환 리터럴: 정수,실수
print( 10 + 3 ) # 13
print( 10 - 3 ) # 7
print( 10 * 3 ) # 30
print( 10 ** 3 ) # 1000
print( 10 / 3 ) # 3.3333333
print( 10 // 3) # 3
print( 10 %  3 ) # 1

# [2] 연결연산자 반환 리터럴 : 문자열 자료 1개
print( "hello" + "python" )
print( "hello" , "python")
# print( "hello" + "python" + 3 ) 문자열 + 숫자 => 오류발생

# [3] 비교연산자, 반환 리터럴 : 불리언 자료 1개
print ( 10 > 3 ) # True
print ( 10 < 3 ) # False
print ( 10 >= 3 ) # True
print ( 10 == 3 ) # False
print (10 != 3 ) # True

# [4] 논리연산자
print( 10 > 3 and 20 > 15 ) # True
    # True and True  => True
print( 10 > 3 and 20 > 30 ) # False
    # True and False => False
print( 10 > 3 or 20 > 15 ) # True
    # True or True => True
print( 10 > 3 or 20 > 30 )
    # True or False => True
print( not ( 10 > 3 ) ) # True -> False


# [5] 대입연산자
var1 = 10 # 10 리터럴 값을 var1 변수에 대입.
#(1) var1 변수의 자료값에 10을 더해서 저장
var1 + 10  # var1 변수값 수정 X
var1 = var1 + 10  # print(var1) => 20
   # 1. var1 변수의 값호출, var1 = 10 + 10
   # 2. 연산, var1 = 20
   # 3. 대입, var1(20)
   # 짧게 작성하는 방법

var1 += 10
#좌항 += 우항 : 우항의 값을 좌항 값과 더한 후 좌항에 대입

print( var1 ) # 30

var1 -= 10
print(var1)  # 20
var1 *= 10
print(var1)  # 200
var1 **= 2
print(var1) # 40000
var1 /= 2
print(var1) # 20000.0
var1 //= 2
print(var1) # 10000.0
var1 %= 3
print(var1)  # 1.0


# [6] 삼항연산자 1. 조건항 2. 참 3. 거짓
    # [True 실행문] if [조건문] else [False 실행문]
        # 조건이 True 이면 [True 실행문] 실행
        # 만약에 조건이 False이면 [False 실행문] 실행\
    # 삼항 연산자 중첩
        # [True 실행문1] if [조건문1] else [True 실행문2] if [조건문 2] else [False 실핼문 ]

point = 85
# # 포인트가 90 이상이면 합격 아니면 불합격
print('합격' if point >= 90 else '불합격')
# 포인트가 90점 이상이면 '최우수' 80점 이상이면 '우수' 그 외 '장려' 출력
print('최우수'if point >=90 else '우수' if point >= 80 else '장려')


# 실습 1 : 기본급과 수당 금액을 각 정수로 입력 받아 실수령액 계싼
# 실수령액 기본급 + 수당 = 세금 (기본급10%)



pay = int(input('기본급 입력 : ' ))
plus_Pay = int(input('수당 입력 : ' ))
minus_pay = pay*0.1
real_pay = pay + plus_Pay - minus_pay
print(f"실수령액은 {real_pay} 입니다")
