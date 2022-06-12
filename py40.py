# page 146 (파이썬 지원함수)
print(2**3)             # 제곱승
print(4**2)             # 제곱승

# 형변환 (자료형 바꾸기)
str(123)                # 정수 '123' -> 문자열 '123'
int('123')              # 문자열 '123' -> 정수 '123'
float('123.0')          # 문자열 '123.0' -> 실수 '123.0'

eval('100-50')          # 정수 50
# result = eval('100-50')
# print(result)

# page 149
# expr = input("계산식을 입력하세요 >>> ")
# result = eval(expr)
# print(expr + '=' + str(result))

# abs == 절대값 구하기
print(abs(-3))
print(abs(3))
# def 절대값구하기(num):                    # == abs
#     if num < 0:
#         num += -1
#         return num
#     return num

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(max(lst))
# print(min(lst))

# # divmod == %
# # pow == **

# # round : 반올림
# pi = 3.141592
# print(round(pi,2))

# # sum : 리스트 안에 있는 값을 전부 더하기해서 return
# print(sum(lst))

# # len : 리스트 항목의 갯수
# print(len(lst))

# lst 평균
def lstAvg():
    lstSum = sum(lst)
    avg = lstSum / len(lst)
    print(round(avg, 2))

lstAvg()

for i, j in enumerate(lst):
    print(i, ":", j)
# enumerate : 방번호와 값을 분리
 
# page 159
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(month):
    print("{}월 = {}일".format(month+1, day))

# page 160 (1)
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for rainbow, color in enumerate(rainbow):
    print("무지개의 {}번째 색은 {}입니다.".format(rainbow+1, color))

# page 160 (2)
exam = []
print("점수를 입력하세요. 더이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.")
while True:
    myScore = int(input("점수 입력 >>> "))
    if myScore < 0:
        break
    exam.append(myScore)

avg = sum(exam) / len(exam)
maxScore = max(exam)
minScore = min(exam)
print("평균 = {}, 최대 = {}, 최소 = {}".format(avg, maxScore, minScore))