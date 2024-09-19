import csv

# 영구 저장이 가능한 전화번호부 구현하기 * csv 파일로 영구저장
    # 조건1 : 등록시 이름과 전화번호를 입력받아 CSV 파일에 저장하기.
    # 조건2 : 목록시 모든 CSV 파일내 이름과 전화번호를 출력하기.

#[1] # 무한 루프 / 반복


phoneBooks = [ ] # 전화 번호 목록 리스트


while True :  # 들여쓰기 주의
    file = open('phoneBook.csv', 'r')  # 1. 파일 읽기 모드로 파일 객체 반환
    contents = csv.reader(file)  # 2. 파일 객체를 csv 객체로 읽어오기
    phoneBooks = list(contents) # 3. 읽어온 객체를 list타입으로 변환 # list() : list타입으로 변환해주는 함수
    file.close()
    # [2] 기능 입력받기
    ch = input('1.등록 2.목록보기 3.종료 : ')
    # [3] 입력 조건문
    if ch == '1' :
        print( '>>> 전화번호 등록 >>>' )
        # [4] 입력 받기
        name = str(input("등록할 이름을 입력해주세요 : "))
        number = str(input("등록할 전화번호를 입력해주세요 : "))
        phoneBooks.append( [ name , number ] ) # .append (새로운 요소) # 리스트내 요소 추가

    if ch == '2' :
        print( '>>> 전화번호 목록 >>>' )
        # 2차원 리스트 출력하기
        for row in phoneBooks : # 2차원 리스트 출력하기 # 2차원 리스트를 반복문 이용한 자료 반환하기
            print(row)

    if ch == '3':
        break # 가장 가까운 반복문을 종료한다, 탈출한다 # 즉 무한루프 종료
    ## ------- csv 파일 쓰기 --------- ##
    file = open('phoneBook.csv', 'w', newline="")  # 1. 파일쓰기 모드
    csvFile = csv.writer(file, delimiter=',')  # 2. csv 쓰기 파일 객체 호출
    # csvFile.writerow([name, number])  # 3. csv 내용 쓰기
    csvFile.writerows( phoneBooks ) # csv 내용쓰기
    file.close()  # 4. 파일객체 닫기