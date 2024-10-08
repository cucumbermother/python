
# [7] 함수 안에서 선언된 변수의 사용범위 # 지역 변수
var1 = 1 # 함수 밖에서 선언된 변수 ( 전역 변수 )
def test1( var1 ) : # 함수 안에서 선언된 변수( 매개변수 , 지역 변수 )
    var1 = var1 + 1 # 함수 안에서 선언된 변수 ( 지역변수 )
test1( var1 )
print( var1 ) # 1

# 1. return 반환 # 전역변수와 지역변수가 이름이 동일하면 함수내에서는 지역변수가 우선이다.
# 지역변수를 사용하는 이유 == 함수를 사용하는 이유 : 함수는 정의하고 함수내 코드들은 실행시에만 메모리 할당/부여 , 종료되면 다 사라짐
# 메모리 (물리적인 저장장치) / 자원  = 자원을 아껴쓰자 -> 함수는 실행할때만 함수내 코드의 메모리 할당하고 함수를 종료하거나 안쓰면 메모리 할당 안함
# 즉 사용시에만 메모리(자원)를 사용하는 개념
def test2 ( var1 ) :
    var1 = var1 + 1 # var1 = 지역변수
    return var1 # 지역변수의 자료를 반환/리턴 # 함수 종료되면 함수내 메모리/변수/자료는 다 사라진다. # 필요한 자료는 복귀/반환
print( test2( var1 ) ) # 2

# 2. 전역변수를 함수 안으로 불러내기 , global 키워드
def test3() :
    global var1 # global 전역변수명 # 함수 밖에 있는 전역변수를 함수안으로 가져옴
    var1 = var1 + 2
test3()
print( var1 ) # 3


# [실습1] : 키보드로 부터 입력받은 2개의 정수를 인자값으로 전달하면 두 정수를 제곱계산하여 결과를 반환 하는 함수 만들기


a = int(input('정수를 입력해주세요 : '))
b = int(input('정수를 입력해주세요 : '))



def square ( x , y  ) : # 2개의 인자값을 받아 2개의 매개변수에 저장하는 함수 정의
    result = x ** y
    return result # 리턴을 안하면 함수내 모든 자료들이 사라진다 왜? 지역변수의 특징(지역에서 태어났으면 지역이 종료되면 사라짐)

print(square( a , b ))

# 또는

real_square = square( a , b )
print( real_square )

# [실습2] : [ 1 , 2 , 3 , 4 ] : 자료 4개를 가지는 리스트 자료 1개를 인자값으로 전달하여 매개변수의 총합계를 계산하여 반환하는 함수 만들기

list = [ 1 , 2 , 3 , 4 ]
sum = 0
def square (list) :
    for 합 in list :
        global sum
        sum += 합
    return sum

print(square(list))