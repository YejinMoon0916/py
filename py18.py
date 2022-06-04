나이 = 20

'''
if 나이 >= 20:
    print("성인")
if 나이 < 20:
    print("미성년자")
'''
'''
if 나이 >= 20:
    print("성인")
else:
    print("미성년자")
'''

# page 95
# 나이에 따라서 프로그램의 동작을 다르게 if ~ elif ~ else
age = int(input("몇 살 입니까? >>> "))

if age >= 20:
    print("성인")
elif age >= 0:
    print("미성년자")
else:   
    print("?")

# page 86 5번
# input
kor = int(input("국어 점수를 입력하세요 >>> "))
eng = int(input("영어 점수를 입력하세요 >>> "))
math = int(input("수학 점수를 입력하세요 >>> "))

avg = (kor + eng + math) / 3

if avg >= 80:
    print("평균은 {}점이고, 결과는 합격입니다.".format(avg))
else:
    print("평균은 {}점이고, 결과는 불합격 입니다.".format(avg))

# 숙제 90 ~ 99