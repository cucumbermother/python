# [1] 파일쓰기(생성)

open('test1.txt' , 'w') #
open( '../test2.txt' , 'w')


# [2] 파일의 내용 쓰기
file4 = open( './test4.txt' , 'w' ) # 쓰기모드 파일 생성하고 파일객체 반환받아서 변수에 저장
file4.write("dhsdhsa")
file4.close()

file5 = open('./test5.txt' , 'w' , encoding='utf-8')
for value in range( 1 , 11 ) :
    # range(시작값 , 끝값): 시작값 부터 끝값 전까지 1씩 증가하는 리스트 반환
    data = f'{value} 번째 줄입니다. \n'
    file5.write(data)

file5.close()

# [3] 키보드로부터 입력받은 값을 파일(file6)에 저장

input1= str(input("입력 ㄱㄱ : "))
file6 = open('./test6.txt' , 'w' , encoding='utf-8')
file6.write(input1)
file6.close()


# [4] 파일을 읽는 여러가지 방법

file = open('./test5.txt' , 'r' , encoding='utf-8')
#1. readline() # 파일을 한줄을 읽음
line = file.readline()
print(line)
while True :
    line = file.readline()
    if not line : # 만약에 읽어온 문자가 '공백'이면
        break # 가장 가까운 반복문을 종료
    print( line )
file.close() # 파일닫기

#2. .readlines() # 파일내 한줄씩 요소로 해서 여러줄을 리스트로 반환

file = open('./test5.txt' , 'r' , encoding='utf-8')
lines = file.readlines()
print( lines )

for line in lines :
    print( line )
file.close() # 파일 작업이 끝나면 파일닫기

# 3.read # 파일내 모든 내용을 문자열로 읽어오는 함수
file = open( './test5.txt' , 'r' , encoding='utf-8' )
content = file.read()
print(content)
file5.close()

# [5] 키보드로부터 입력받은 값이 저징된(file6.txt) 파일의 값을 읽어오기

uzer1 = input('입력 : ')
file = open('./test6.txt' , 'w' , encoding='utf-8')
file.write(uzer1)
file = open('./test6.txt' , 'r' , encoding='utf-8')
read = file.read()
print(read)

# 파일처리와 예외처리 같이 작성 하기
    # 1. 파일명의 오타가 있거나 존재하지 않는 파일은 예외 발생 # FileNotFoundError

try :
    file = open('./test7.txt', 'r', encoding='utf-8')
except FileNotFoundError as e : # 2. 예외 발생시 안내문구
    print("존재하지 않는 파일 이거나 경로의 문제가 있습니다")
