import csv


# [2] 현재 python에 내장된 모듈 호출
# import 모듈명
# import csv # 현재파일에 csv 모듈 가져오기(호출)


# [1] 파일 열기 # 쓰기모드

file = open('test2.csv' , 'w' , newline="" )

# [2] csv 쓰기 객체 호출

csvFile = csv.writer( file , delimiter=',')

# [3] csv 파일에 내용 쓰기
csvFile.writerow( [ 'name' , 'phone number' ] )

csvFile.writerow( [ 'kimyouna' , '010-9944-6999' ] )

# [3] 파일 닫기
file.close()

# CSV 파일 읽기
# [5] 파일 열기 # 읽기모드 파일객체 반환
file = open('test2.csv' , 'r')

# [6] CSV 읽기 객체 호출 # .reader(파일객체)
content = csv.reader( file )
print(content)
print( list(content) ) # list() 리스트 타입으로 변환 함수