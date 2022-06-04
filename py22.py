# for 변수명 in range(10):

# while 
# import time

# 기준점 = 0
# while 기준점 < 10:
#     time.sleep(1)            # 1초동안 멈춤
#     print("10은 5보다 큽니다")
#     기준점 += 1
# print("프로그램 종료")

'''
while 조건:
    조건이 맞을 때 마다 실행 할 코드
'''

# num = 1

# while num < 11:
#     print(num, "번 했습니다.")
#     num += 1

# 105 page
# n = 10

# while n >= 1:
#     print(n)
#     n -= 1

# 110 page (2중 반복문)
dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print("{}x{}={}".format(dan, n, dan*n))
        n += 1
    dan += 1

# 111 page (1)
num = int(input("정수를 입력하세요 >>> "))

if num <= 0:
    print("잘못된 입력입니다.")

i = 0
while num > i:
     print("{}번째 Hello".format(i+1))
     i += 1


# 111 page (2)
i = 1

while i < 100:
    cal = i % 7
    if cal == 0:
        print(i)
    i += 1
