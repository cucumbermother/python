'''
    예외 처리
        - 오류[ Error ] :
            - 시스템이 종료 되어야 할 수준의 상황과 같이 개발자가 수습할 수 없는 심각한 문제
            - 개발자가 미리 예측/방지 할 수 없다. 주로 하드웨어(메모리) 관련된 오류가 발생한다.

        - 예외[ Exception] :
            - 개발자가 구현한 로직에서 발생한 실수나 사용자의 영향에 의해 발생하는 문제
            - 오류와 달리 개발자가 미리 예측/방지 할 수 있기에 상황에 맞게 예외처리를 해야한다.
            - 개발자 예측 ---> 개발자 경험 풍부 ---> 개발자의 경험의 의존성이 크다.
            - 코드를 수정하는 직업이 아닌 예외가 발생했을때  흐름 제어 방식 , if와 비슷함
        - 목적 : 문제 또는 오류가 발생하면 프로그램은 자동으로 종료된다.
            즉] 예외가 발생 하더라도 프로그램은 24시간 종료되지 않고 서비스를 제공해야 한다. 안전한 프로그램 제공
        - 예외처리 문법
            try :
                예외가 발생 하거나 발생 할 것 같은 코드(예측)
            except :
                만약에 try 에서 예외가 발생 했을때 실행 되는 코드
'''

# [1] 고의적으로 예외 발생1 # 인덱스

array = [ 1 , 2 , 3 ]
# array[5] #IndexError: list index out of range # 중간에 프로그램 종료
try :
    array[ 5 ]
except :
    print('Index Error 예외 발생') # 프로그램 유지


# [2] 예외 발생 2 # ZeroDivisionError 클래스
# print( 3/0 ) # ZeroDivisionError: division by zero
try :
    print(3/0)
except ZeroDivisionError as e : # except 예외클래스명 as 변수명 : # 변수명에 예외 사유를 대입한다.
    print( e ) # division by zero


# [3] 예외 발생 3 #ValueError클래스
#int( ' a ' ) #ValueError: invalid literal for int() with base 10: ' a '

try:
    int('a')
except ValueError as e :
    print(e)
