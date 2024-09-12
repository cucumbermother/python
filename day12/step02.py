# [1] csv 파일 읽어오기

file = open( '인천광역시 부평구_인구 현황_20240214 (1).csv' , 'r' )
    # csv 파일 경로 : 다운로드 받은 csv 파일명과 확장자를 넣는다.
    # 'r' 읽기모드
# print( file.read())

# [2] csv 파일내 모든 내용들을 가져온다.
contents = file.read()
# [3] 줄 단위로 구분해서 리스트에 반환한다.
contentsList = contents.split('\n')
# print( contentsList )
#[4] 반복문을 이용한 리스트내 요소들을 하나씩 호출해 보기
sum = 0
for row in contentsList[ 1 : -2] :
    # print(row) # 리스트내 요소 하나씩 출력
    cols = row.split(',') # 요소의 ,(쉼표) 기준으로 분해
    # [ 동별 , 인구수(계) , 인구수(남) , 인구수(여) , 세대수 , 데이터 기준일자 ]
    # [ 부평1동 , 35141 , 16835 , 18306 , 16861 , 2024-02-14] #,( 리스트내 요소 구분 )
    # print(cols)
    # print( cols[0] )  # 예시) 부평구의 모든 동명을 호출 하시오
    print( cols[1] ) # 숫자 처럼 보이지만 숫자형식의 문자열타입
    sum += int( cols[1])


print(f'부평구의 총 인구수 : { sum }')
