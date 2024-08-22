# 조건문 실습  1  :  하나의 점수를 입력 받아서
# 80점 이상 이면 ' 합격 ' 아니면 ' 불합격 ' 출력

# test = int(input( '점수를 입력해주세요 ' ))

# (1)

# if test >= 80 :
#     print( "합격" )
# else : print( "불합격" )


# (2)
# 90점 이상 A등급 80점 이상 B등급 70점 이상 C등급 그 외 재시험

# if test >= 90 :
#     print( "A등급" )
# elif test >= 80 :
#     print( "B등급" )
# elif test >= 70 :
#     print( "c등급" )
# else :
#     print( "재시험" )
#

# (3)
     # 세 정수를 입력 받아서 오름차순으로 출력하시오

num = int(input('첫번째 정수를 입력해 주세요 : '))
num2 = int(input('두번째 정수를 입력해 주세요 : '))
num3 = int(input('세번째 정수를 입력해 주세요 : '))


if num > num2 and num > num3 and num2 > num3 :
    print(f'{num},{num2},{num3}')
elif num2 > num and num2 > num3 and num > num3 :
    print(f'{num2},{num},{num3}')
elif num3 > num and num3 > num2 and num > num2 :
    print(f'{num3},{num},{num2}')
elif num > num2 and num > num3 and num3 > num2 :
    print(f'{num},{num3},{num2}')
elif num2 > num and num2 > num3 and num3 > num :
    print(f'{num2},{num3},{num}')
elif num3 > num and num3 > num2 and num2 > num :
    print(f'{num3},{num2},{num}')
else :
    print("각기 다른 숫자를 입력해주세요")


