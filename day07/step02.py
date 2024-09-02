    #   딕셔너리
    # - key 와 value 값 으로 하는 한쌍을 여러개 저장하는 자료구조
'''

리스트의 부족한 점 
    - 저장된 순서번호 (인덱스)와 요소(값) 저장되는 구조
    - 인덱스는 숫자로 구성된 순서번호 이므로 대량의 인덱스는 사람이 식별이 어렵다.
    - 


'''

# - 딕셔너리 형태
# { key : value , key : value , key : value }
# key 와 value를 :(콜론)으로 구분하여 한쌍을 이루는 여러 쌍들을 중괄호 감싼 형식
# list는 인덱스로 구분하고 딕셔너리는 key로 구분한다

# [1] 딕셔너리 선언
dic = { 'name' : 'youna' , 'phone' : '010-9944-6093' , 'birth' : '99.06.26' }
dic2 = { 1 : 'h1' } # key는 문자와 숫자 모드 가능
dic3 = { 'a' : { 'b' : 'h2' } } # 딕셔너리 안에 딕셔너리 중첩이 가능
dic4 = { 'a' : [ 1 , 2 , 3 ] } # 'a'라는 key에 리스트 자료가 1개(value) 존재한다

# [2] 딕셔너리의 한쌍 추가 , 삭제
# 변수명[ 'key' ] = 값 # 만약에 key가 존재하면 수정 , 존재하지 않으면 추가
    # 한쌍 추가
dic['addr'] = '인천시' # dic(딕셔너리) 에 'addr' 라는 key와 '인천시'value를 한쌍으로해서 딕셔너리 추가
print( dic )
    # value 수정 # 변수명['key'] = 새로운 값
dic[ 'name' ] = 'kim'
print(dic)
    # 한쌍 삭제 # del 변수명[ 삭제할 key ] # 지정한 key의 쌍을 제거한다
del dic[ 'addr' ]# del 키워드 [ 키워드란? 파이썬에서 미리 만들어진 기능이 당긴 단어들 ]
print(dic)

# [3] 딕셔너리 만들때 주의할 점
# a = { 1 : 'a' , 1 : 'b'} # 1. 중복된 key의 이름을 가질수 없다
    # 왜? key는 여러 쌍들중에서 value의 구별(식별) 용도로 사용하기 때문에

# a = { [ 1 , 2 ] : 'h1' } # 2. 리스트 타입으로는 key를 사용할 수 없다

# [4] 딕셔너리에서 key를 이용한 value 반환/추출 , # 변수명[ 'key' ]
print( dic[ 'name' ] ) #kim


# [5] 딕셔너리의 관련 함수들  # 함수란? 입력에 따른 기능처리후 결과 반환하는 구조
    # print( 'aa' ) # 'aa' 를 print함수에게 입력(인자값) 전달하여 console 출력 후 반환하는 구조

# 1. .keys() : 딕셔너리 내 모든 key들을 모아서 객체로 반환해주는 함수
print( dic.keys() ) # dict_keys(['name', 'phone', 'birth'])

# 2. list(자료) : 지정한 자료를 다양한 리스트 타입으로 반환 하는 함수
print( list( dic.keys() ) ) # ['name', 'phone', 'birth']

# 3. .values() : 딕셔너리 내 모든 value들을 모아서 객체로 반환해주는 함수
print( dic.values() ) # dict_values(['kim', '010-9944-6093', '99.06.26'])

# 4.
print( list(dic.values() ) ) # ['kim', '010-9944-6093', '99.06.26']

# 5. .items() : 딕셔너리 내 모든 쌍(key:value)을 튜플로 묶인 객체로 반환 해주는 함수
print( dic.items() ) # dict_items([('name', 'kim'), ('phone', '010-9944-6093'), ('birth', '99.06.26')])

# 6.
print( list( dic.items() ) ) # [('name', 'kim'), ('phone', '010-9944-6093'), ('birth', '99.06.26')

# 7. .get('key') : 딕셔너리 내 key에 해당하는 value 반환 함수
print( dic.get('name ') ) # == dic['name'] 동일한 방법

    # 차이점이 있다.
# print( dic['age'] ) # 딕셔너리 내 존재하지 않는 key를 호출하면 오류발셍
print( dic.get('age') ) # 딕셔너리 내 존재하지 않는 key를 호출하면 none을 반환

# 8. key in 딕셔너리 : 딕셔너리 내 key가 존재하면 True 존재하지 않으면 False

print( 'name' in dic ) # True # 딕셔너리내 'name'이라는 key가 존재, False가 반환됨
print( 'age' in dic ) # False # 딕셔너리내 'age'라는 key가 존재하지 않음으로 False가 반환됨

# 9. len( 딕셔너리 ): 딕셔너리 내 쌍 (key : value) 총 갯수
print( len(dic) ) #  3