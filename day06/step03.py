memberList = [ '이강인' , '쏜흥민' , '김민재' ]

# [1] 리스트내 특정 요소의 값 수정

memberList[0] = '박지성' # 변수명[수정할 인덱스] = 새로운 값

print(memberList)

# [2] 리스트와 반복문 관계 # 인덱스란? 목록(리스트)에 저장된 요소들의 순서번호( 0 ~)

# (1) 리스트내 모든 요소들의 값 출력

print( memberList[0])
print( memberList[1])
print( memberList[2])

# 만약에 요소의 개수가 1000개이면 힘듦;


# (2) 반복코드 : print( memberList[ ]) , 변화코드(변수) : 0 , 1 ,2
# 0부터 2까지 1씩 증가 -> range( 0 , 3 )
for index in range( 0 , 3 ) : # 리스트의 개수를 모를때 # len()
    print(memberList[ index ])
for index in range( 0 , len( memberList )) : # 0부터 마지막 인덱스까지 반복
    print(memberList[ index ])
for value in memberList : # 리스트내 요소값 *하나씩* 반복변수(value)에 대입반복 # 마지막 인덱스까지
    print( value )

# (2)
marks = [ 90 , 25 , 67 , 40 , 80 ] # 리스트
for value in marks : # 리스트내 요소 하나씩 호출
    if value < 60 : #만약에 현재 반복중인 요소의 값이 60 미만 이면
        continue # 가까운 반복문으로 이동 # 아래 코드는 실행되지 않는다.
    print(f' {value} 는 60점 이상 이므로 합격 입니다. ')


# (3) 리스트 컴프리헨션 사용
    # 반복문 이용한 값을 리스트로 선언할때 주로 사용
    # [표현식 for 반복변수 in 반복가능 객체 ]
    # [표현식 fot 반복변수 in 반복가능객체 if 조건문 ]
a = [ py * 2 for py in range( 0 , 3 ) ]
print( a ) # [0, 2, 4]
b = [ 2*곱 for 곱 in range( 1 , 10 ) ]
print( b ) # 2단의 값들을 저장하는 리스트
c = [ 2*value for value in range ( 1 , 101 ) if value % 2 == 0 ]
print( c )

# (4) 2차원 리스트 : 리스트 타입에 리스트 타입을 저장하는 구조 # 행 , 열 ( 구구단 )
d = [ [1 , 2 , 3 , ["안녕","하이","유나"]] , [4 , 5 , 6] ]  # d 리스트에서는 요소 2개
# 2차원 리스트 인덱싱
    # 변수명[행 인덱스][열 인덱스]
print(d[0]) # 0번 인덱스의 요소 값 호출 : [1, 2, 3]
print(d[0][1]) # 인덱스 0번째 요소인 리스트중 1번째 요소호출 # 3
print(d[0][3][2])

#

아파트 = [
    [101 , 102 , 103] ,
    [201 , 202 , 202] ,
    [301 , 302 , 303] ] # 아파트 리스트 요소 3개 # 아파트의 요소들인 리스트요소들의 리스트의 요소는 각 3개씩있다.

print( 아파트[0][1] ) # 102 -> 첫번째 줄에 2번째 칸
print( 아파트[1][2] ) # 203 -> 두번째 줄에 3번째 칸
print( 아파트[2][0] ) # 301 -> 세번째 줄에 1번째 칸

# 2차원 리스트를 반복문과 사용 , for 문 중첩
for 행 in 아파트 :
    print( 행 )
    # 하나의 행(층)에 열 반복
    for 열 in 행 :
        print( 열 )
