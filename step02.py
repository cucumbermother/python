# [1] 예외 다중 처리 # 다중 except #0개 또는 1개 실행

array = [1,2,3]
try :
    print(array[2])
    print(4/0)
    int('a')
except IndexError as e :
    print(e)
except ZeroDivisionError as e :
    print(e)
except ValueError as e :
    print(e)


# [2] 모든 예외 처리 하는 클래스 # 예외 상위 클래스 Exception 클래스
try:
    array[5]
    print( 4 / 0)
    int('a')
except Exception as e :
    print(e)
except ValueError as e: # 아무런 의미가 없는 예외 # 앞에서 모든 예외를 처리하기 때문에
    print(e)

# [3] finally 키워드 # 예외 발생 여부와 상관없이 무조건 실행되는 코드
try:
    array[2]
except IndexError as e:
    print(e)
finally:
    print('예외 여부와 상관없이 실행')

# [4] pass 키워드 # 예외회피 # 예외 발생시 그냥 통과 # 아무것도 하지 않을때 사용
try:
    print(4/0)
except :
    pass # 만약에 예외가 발생하면 pass

# [5] raise 키워드 # 예외 강제 발생 # 강제로 예외를 발생 시킬때 사용
try :
    raise ValueError # 강제로 예외 발생
except ValueError as e:
    print( e )

# 실습1 :
    # [1] 1. 이름(문자) 2.나이(정수)를 입력받는 하나의 (member)딕셔너리 저장
    # 나이를 입력받을때 1가지 이상의 예외 예측해서 예외처리 하기
    # [2] member 딕셔너리 내 'phone' key의 value를 호출하는데
    # 호출시 예외 발생 처리하기




try :
    # 1.
    name = str(input("이름을 입력해주세요 : "))
    age = int(input("나이를 입력하세요 : "))  # 나이 입력시 문자 입력하면 예외발생 : ValieEerror

    dic = { 'name' : name , 'age' : age }
    print( dic['phone']) #딕셔너리 내에서 존재하지 않는 key 사용했을때 예외 발생 : KeyError

except ValueError as e :
    print( '나이를 숫자형식으로 입력 해주세요.' )
except KeyError as e :
    print( '존재하지 않는 key 입니다.' )
except Exception as e :
    print('예외 발생 [관계자에게 문의] ')
finally :
    print( '프로그램이 안전하게 종료됩니다 ' )









