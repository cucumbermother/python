# type ( 자료 )
type(10.5) # 자료(리터럴), 정수 타입
# int( 문자열 ), float( 문자열), bool( 문자열 ) # 문자열 자료를 각 타입으로 반환 함수들
       # 정수타입 10 vs 문자열 타입 '10' 다르다

int( '10' )
# int( 'a' ) , 이러한 경우는 불가능
float( '10.4' )
bool( 'True' )



# 변수의 선언 하고 초기화 [처음에 값을 넣어주는 행위], 변수명 = 초기값
var = 10
# 변수의 자료/값 호출
var
# 변수의 자료/값 수정, 변수명 = 새로운값
var = 5

# 콘솔 창에 출력함수, print( 자료 또는 변수명 )
print( var )
print(f'var: { var }') # 문자열과 변수의 값을 같이 출력할수 있다. f포메팅
print(f'var: \t {var} \n ') # \n 줄바꿈 \t 들여쓰기, 이스케이프 문자


# 콘솔에서 입력받기, input()
     # 콘솔에서 입력후 엔터 기준으로 입력값을 반환하는 함수.
     # 콘솔창에 초록색 부분이 입력된 값, 검정색 부분이 출력된 값
input()
    # - 하나의 데이터를 입력받아서 출력하시오.
print( type(input()) )   #<class 'str'>
    # - 하나의 (2)정수 데이터를 (1)입력받아서 (3)출력하시오
print( int( input() ))
    # - 하나의 정수 데이터를 변수에 저장하고 해당 변수를 출력하시오.
# 1
input()
# 2
int( input() )
# 3
var = int( input() )
# 4
print(var)
