리스트 = ['h', 'e', 'l', 'l', 'o']
문자열 = 'hello'

# 잘라내기
print(리스트[1:4])          # ['e', 'l', 'l']
print(문자열[1:4])          # ell
print(리스트[-1])           # o
print(문자열[-1])           # o

글자 = "3학년 5반 10번"
print(글자[7:10])
print(글자[7:])

# page 99 (4)
carNum = input("차량번호를 입력하세요 >>> ")

carNumeven = int(carNum[6:])     # carNum[-1]

if carNumeven % 2 == 0:
    print("차량번호 {}는 오늘 운행 가능입니다.".format(carNum))
else:
    print("차량번호 {}는 오늘 운행불가능입니다.".format(carNum))
