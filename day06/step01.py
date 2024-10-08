# 리스트 ( list ) / 목록
    # - 목록 : 어떤 물품의 이름을 일정한 순서로 적은 것
    # - 컴퓨터 : 어떤 자료의 값을 일정한 순서로 적은 것
    # - 리스트의 리터럴 : [ ] , 리스트 타입은 하나의 리터럴 타입이다.
    # - 용어 :
        # 1. 요소( element ) : 항목 ( 목록의 특정한 한개 / 자료 )
        # 2. 인덱스 : 리스트내 요소들이 저장된 순서번호 # 0번부터 시작 # 자료 검색 용도
from operator import index

# [1] 리스트 타입 형태 # 여러개의 자료들을 , ( 쉼표 ) 구분하고 [] 대괄호로 감싼 형식

# 변수명 = [ 요소1 , 요소2 , 요소3 , 요소4 ]
odd = [ 1 , 3 , 5 , 7 , 9 ] # 5개의 요소( 정수 )를 가지는 리스트 선언
# 요소 1 ( 인덱스 : 0 , 자료 : 1) , 요소 2 ( 인덱스 : 1 , 자료 : 3 ), 요소 3 ( 인덱스 : 2 , 자료 : 5 )
# 요소 4 ( 인덱스 : 3 , 자료 : 7 ) , 요소 5 ( 인덱스 : 4 , 자료 : 9 )

# [2] 리스트 호출
print( odd ) # 리스트 자료가 저장된 변수명 호출

a = [] # 요소가 없는 리스트 선언
print( a )

b = [ 'hello' , 'youna' , 'happy' , 'life' , 'LOL' ] # 요소가 5개인 리스트 선언
print( b )
c = [ 1 , 2 , True , 'life' , 'is' ] # 여러 가지 타입의 요소들 5개인 리스트 호출
print( c )
d = [ 1 , 2 , [ "life" , "is" ] ] # 여러 가지 타입의 요소들 3개인 리스트 선언 , 3번째 요소에는 2개의 요소가 들어있는 리스트 자료
print( d )

# 리스트의 인덱싱과 슬라이싱

studentlist = [ '김유나' , '김효주' , '장민환' , '이용호']
    # 인덱싱 : 인덱스를 이용한 요소 추출 # 변수명[ 인덱스번호 ]
print( studentlist [ 0 ] ) # 김유나 # 0번 인덱스의 요소자료 반환
print( studentlist [ 1 ] ) # 김효주 # 1번 인덱스의 요소자료 반환
print( studentlist [ 2 ] ) # 장민환 # 2번 인덱스의 요소자료 반환
print( studentlist [ 3 ] ) # 이용호 # 3번 인덱스의 요소자료 반환

print( studentlist [ -1 ] ) # 이용호 # 뒤에서부터 시작 # 마지막 인덱스
print( studentlist [ -2 ] ) # 장민환 # 뒤에서 두번째
print( studentlist [ -3 ] ) # 김효주 # 뒤에서 세번째
print( studentlist [ -4 ] ) # 김유나 # 뒤에서 네번째
# print( studentlist [ -5 ] ) # 뒤에서 다섯번째는 없음
    # 슬라이싱 : 인덱싱을 이용한 요소*들* (리스트) 부분 추출 # [ 시작인덱스(포함 O) : 끝인덱스(포함 x)]
print( studentlist [ 0 : 2 ] ) # ['김유나', '김효주'] # 0 부터 2미만 (1까지) , 0 ~ 1
print( studentlist [ 0 : 3 ] ) # 0 ~ 2 #['김유나', '김효주', '장민환']
print( studentlist [ : 4 ] ) # 생략시 0 # 0부터  4미만 (3까지)  , 0 ~ 3 # ['김유나', '김효주', '장민환', '이용호']
print( studentlist [ 2 : ] ) # 생략시 마지막 인덱스 # 2 ~ 3 # ['장민환', '이용호']
print( studentlist [ : ] ) # 전체 생략시 전체호출 # ['김유나', '김효주', '장민환', '이용호']
print( studentlist [ 0 : 4 : 1 ] ) # 0부터 3까지 1씩증감 # ['김유나', '김효주', '장민환', '이용호']
print( studentlist [ 0 : 4 : 2 ] ) # 0부터 3까지 2씩증가 # ['김유나', '장민환']
print( studentlist [ -1 : -5 : -1 ] ) # -1 부터 14까지 1씩 감소 # ['이용호', '장민환', '김효주', '김유나']
print( studentlist [ -1 : -5 : -2 ] ) # -1 부터 -4까지 2씩 감소 # ['이용호', '김효주']