# 1. 데이터들의 타입 확인 ,  type( 리터럴값 )

print(type(123))  # <class 'int'> 는 정수타입을 의미함
print(type("123")) # <class 'str'> 는 문자열타입을 의미함
print(type(3.14)) # <class 'float'> 는 실수타입을 의미함
print(type(True)) # <class 'bool'> 는 불리언타입을 의미함


# 2. 기본타입 종류와 데이터 형태


# 2-1 정수타입, 일반적인 정수의 데이터

print( 3 )
print( 123456 )
print( 3 + 3 ) # 3 + 3 의 결과 6이 정수이기 때문에 정수 리터럴

# 2-2 실수 타입, 일반적인 소수점 형식의 데이터

print( 3.14 )
print( 12.121212 )
print( 12.45 + 2.59 )

# 2-3 불리언타입 , 일반적인 참과 거짓 형식의 데이터, 주의할점 첫글자 대문자

print( True )
print( False )
print( 10 > 3 )


#2-4 문자열타입 , 일반적인 텍스트 형식의 데이터
#주의할점 정수, 실수, 불리언도 문자열로 감싸면 문자열이다.

print( "안녕" )
print( '안녕' )
print( """안녕""" )
print( '''안녕''' )
print( "True" )
print( "3.14" )


# 3. 타입을 변경 하는 방법
 # "123" (str문자열) --> 123(int정수)
 # int() : 문자열 타입을 정수 타입으로 변경 해서 반환/ 돌려주는 함수
 # float() : 문자열 타입을 실수 타입으로 변경해서 반환/ 돌려주는 함수
 # bool() : 문자열 타입을 불리언 타입으로 변경해서 반환/ 돌려주는 함수
 # 주의할점 : '('열고')' 닫기 개수를 맞추어 작성하기

print( type( int( "123" ) ) )  # <class 'int'>
print( type ( float( "3.14" ) ) ) # <class 'float'>
print( type ( bool( "True" ) ) ) # <class 'bool'>
print( type ( str ( 123 ) ) ) # <class 'str'>


