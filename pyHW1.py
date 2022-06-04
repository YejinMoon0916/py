# 기본 예제
# page 95
age = int(input("몇 살입니까? >>> "))

if age >= 20:
    print("성인")
else:
    print("미성년자")

# 기본 예제
# page 98
age = int(input("몇 살입니까? >>> "))

if age <= 7:
    print("미취학")
elif age <= 13:
    print("초등학생")
elif age <= 16:
    print("중학생")
elif age <= 19:
    print("고등학생")
else:
    print("성인")


# 응용 예제
# page 99 (1)
sNum = int(input("점수를 입력하세요 >>> "))

if sNum < 60:
    print("점수는 {}이고, 학점은 F학점입니다.".format(sNum))
elif sNum < 70:
    print("점수는 {}이고, 학점은 D학점입니다.".format(sNum))
elif sNum < 80:
    print("점수는 {}이고, 학점은 C학점입니다.".format(sNum))
elif sNum < 90:
    print("점수는 {}이고, 학점은 B학점입니다.".format(sNum))
elif sNum <= 100:
    print("점수는 {}이고, 학점은 A학점입니다.".format(sNum))
else:
    print("다시 입력해 주세요.")

# page 99 (2)
num = int(input("정수를 입력하세요 >>> "))
cal = num % 3

if cal == 0:
    print("{}는 3의 배수입니다.".format(num))
else:
    print("{}는 3의 배수가 아닙니다.".format(num))

# page 99 (3)
num1 = int(input("정수1 입력 >>> "))
num2 = int(input("정수2 입력 >>> "))
num3 = int(input("정수3 입력 >>> "))

if num1 >= num2 and num1 >= num3:
    print("가장 큰 수는 {}입니다.".format(num1))
elif num2 >= num1 and num2 >= num3:
    print("가장 큰 수는 {}입니다.".format(num2))
else:
    print("가장 큰 수는 {}입니다.".format(num3))

# page 99 (4)
carNum = input("차량번호를 입력하세요 >>> ")

carNumeven = int(carNum[7])

if carNumeven % 2 == 0:
    print("차량번호 {}는 오늘 운행 가능입니다.".format(carNum))
else:
    print("차량번호 {}는 오늘 운행불가능입니다.".format(carNum))




# page 99 (3)
while True:
    num1 = int(input("정수1 입력 >>> "))
    num2 = int(input("정수2 입력 >>> "))
    num3 = int(input("정수3 입력 >>> "))

    if num1 >= num2 and num1 >= num3:
        print("가장 큰 수는 {}입니다.".format(num1))
    elif num2 >= num1 and num2 >= num3:
        print("가장 큰 수는 {}입니다.".format(num2))
    else:
        print("가장 큰 수는 {}입니다.".format(num3))