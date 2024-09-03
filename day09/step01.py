'''

    객체 지향 프로그래밍 언어
        - python , java 등등
    객체란?
        - Object( 물체 / 대상 )
        - 손님 (객)
        - 파이썬 내 생선된 물체/대상
        - 파이썬내 모든 타입들은 객체타입으로 만들어져 있다.
    주체란?
        - Subject(  )
        - 주인 (주)
    클래스란?
        - 객체를 만들기 위한 설계도/틀

'''

# [1] 클래스 만들기 # class 키워드 : 클래스를 정의하겠다는 뜻
# 클래스명 : 첫글자로 대문자로 하는 영대소문자
class Human :
    pass # pass 클래스 : 아무것도 수행하지 않는 문법 # 임시용


# [2] 객체 만들기
print( Human( ) ) # <__main__.Human object at 0x0000016BC3E4D6A0>
print( Human( ) ) # <__main__.Human object at 0x0000016BC3E4D6A0>

h1 = Human( )
h2 = Human( )
print( h1 )
print( h2 )


# [2] 클래스 만들기

class 붕어빵 :
    def __init__( self  , 내용물 ) :
        self.내용물  = 내용물

# [4] 붕어빵 객체 만들기

print( 붕어빵( '팥' ) )
print( 붕어빵( '슈크림' ) )
붕어빵1 = 붕어빵( ' 팥 ' )
붕어빵2 = 붕어빵( ' 슈크림 ')
print( 붕어빵1 )
print( 붕어빵2 )

#[5] 자동차 클래스 만들기
class Car :
    # 생성자
    def __init__( self , carNum ) :
        self.carNum = carNum
    # 함수
    def move( self ) :
        print( f'{self.carNum}가 이동한다')

#[6] 자동차 객체 생성
유재석차 = Car('1234') #1324 차량번호의 차 객체를 생성
강호동차 = Car('4567') #4567 차량번호의 차 객체를 생성
    # 두 객체는 같다고 할 수 있을까?

print( 유재석차 ) # <__main__.Car object at 0x0000023157DDE390>
print( 강호동차 ) # <__main__.Car object at 0x0000023157DDE3C0>

유재석차.move() # 유재석차(1234) 가 이동한다고 강호동차 까지 이동하지 않는다.

