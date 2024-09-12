# 문자열
# - 문자열은 리터럴 # 불변성(수정 불가능) 특징
# [1] 파이썬에서 문자열 표현하는 방법 : "" , '' , """ """ , ''' '''
from tkinter.font import names

# [2] 문자열 연산 # + 연결 , * 배수 , += 누적연결

a = 'python '
a += 'is fun'
print(a)

# [3] 문자열 인덱싱 # 문자열내 문자 위치를 인덱스(번호) 표현 #리스트/튜플
print( 'python'[0] ) # p[0] y[1] t[2] h[3] o[4] n[5]
print( 'python'[-1] ) # n
print( 'python'[-3] ) # p[-6] y[-5] t[-4] h[-3] o[-2] n[-1]


# [4] 문자열 슬라이싱 [ 시작번호 : 끝번호(미만) : 증강단위 ]
print( 'python' [ 0 : 2 ] ) # py
print( 'python' [  : 3 ] ) # pyh
print( 'python' [ 2 :  ] ) # thon
print( 'python' [  :  ] ) # python
print( 'python' [ 2 : -1 ] ) # tho
print( 'python' [ : : 2 ] ) # pto
print( 'python' [  : : -1 ] ) # nohtyp


# [5] 문자열 관련 함수/기능

a = '코딩도 헤매는 만큼 자기 땅이야'

# 1. .count ('찾을문자') # 문자열내 찾을 문자가 존재하면 개수 반환 함수
print( a.count("자") ) # 1 # 지정한 문자열내 '자' 인 문자가 1개 존재
print( a.count('가') ) # 0 # 지정한 문자열내 '가' 인 문자가 0개 존재

# 2. .fide('찾을문자') # 문자열내 찾을 문자가 존재하면 찾은 문자의 인덱스 반환 함수
print( a.find('자') ) # 11 # 문자열내 '자'인 문자의 인덱스 위치
print( a.find('가') ) # -1 # 문자열내 '가'인 문자의 인덱스가 없다는 뜻

# 3. .index('찾을문자') # 문자열내 찾을 문자가 존재하면 찾은문자의 인덱스를, 없으면 예외발생 하는 함수.
print( a.index('자') ) # 11
try:
    print( a.index('가')) # ValueError: substring not found
except ValueError as e :
    print(e)

# 4. '특정문자'.join("문자열" 또는 리스트) # 문자열내 또는 리스트 요소 사이의 특정문자를 삽입 해서 변환 함수.
print(','.join(a)) # 코딩도 헤매는 만큼 자기 땅이야. #코,딩,도, ,헤,매,는, ,만,큼, ,자,기, ,땅,이,야
b = ['python' , 'java' , 'c' , 'c++']
print( ' <=> '.join( b )) # python <=> java <=> c <=> c++

c = 'AbCsEf'

# 5.    .upper()    # 대문자로 치환해서 (새로운) 반환 함수
print( c.upper() ) # ABCSEF
print( c ) # c는 원본 그대로

#6.     .lower()    # 소문자로 치환해서 (새로운) 반환 함수
print( c.lower() ) # abcdef

a = c.lower() # 대입을 다시 해야 바뀜
print(a) # abcdef



d = '     pyt hon     '

#7.     .lstrip() # 문자열내 왼쪽 공백 제거 된 문자열 반환

print( d.lstrip() ) # pyt hon   ;

#8.     .rstrip() # 문자열 내 오른쪽 공백 제거 된 문자열 반환 함수

print( d.rstrip() ) #      pyt hon;

#9.     .strip() # 문자열내 양쪽 공백 제거 된 문자열 반환 함수

print( d.strip( ) ) # pyt hon
print( d ) #      pyt hon     ; 원본 그대로


a = '코딩도 헤매는 만큼 자기 땅이야'

# 10.   .replace( '기존문자' , '새로운문자' ) # 문자열내 기존문자가 존재하면 새로운 문자로 치환/변경해서 (새로운) 문자열 반환 함수
print( a.replace("코딩" , "파이썬") ) # 파이썬도 헤매는 만큼 자기 땅이야.

# 11.   .split( '구분자' ) # 구분자 기준으로 문자열을 분해해서 리스트 반환

print(a.split(" ")) # ['코딩도', '헤매는', '만큼', '자기', '땅이야']
d = '가:나:다:라'
print(d.split(":")) # : 콜론 기준으로 분해 # ['가', '나', '다', '라']



# 실습1 : dkfo csbdata를 아래 출력 조건과 같이 출력하시오.
csbdata = """유재석,39\n강호동,45\n신동엽,21"""

str1 = csbdata.split("\n")
print(str1) # ['유재석,39', '강호동,45', '신동엽,21']

for str2 in str1 : # 'str1'이라는 리스트를 반복문 사용하여 하나씩 반복하기
    # print( str2 )
    str3 = str2.split(",")
    print(f'{str3[0]} \t {str3[1]} \t')


# 실습2 : 여러명의 이름과 나이를 입력받아서 csv형식으로 파일에 저장
# csv란? 데이터(속성)를 ,(쉼표)로 구분하고 형을 \n(줄바꿈) 구분 하는 형식
    # 이름과 나이를 구분할떄는 ,(쉼표)
    # 사람과 사람을 구분할때는 \n(줄바꿈)

personlist = '' # 여러명의 사람들 정보를 가지는 문자열 (csv 형식)

while True :
    name = input('name : ')
    if name == 'x' :
        break
    age = input('age : ')
    # 문자열 연산
    person = name + ',' + age # 이름과 나이 사이에 ,(쉼표) 삽입해서 구분 가능
    # 사람과 사람 구분해서 사람명단에 저장
    personlist += person + '\n'


# 확인
print( personlist )


file = open('./text.txt' , 'w' )
file.write(personlist)
file.close()