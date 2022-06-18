# # page 105 기본예제
# n = 10
# while n >= 1:
#     print(n)
#     n -= 1

# # page 107 기본예제
# my_list = []

# n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

# while n != 0:
#     my_list.append(n)
#     n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

# print(my_list)

# # page 110 기본예제
# dan = 2
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print('{}x{}={}'.format(dan, n, dan*n))
#         n += 1
#     dan += 1

# # page 111
# # 응용예제 1번
# n = int(input("정수를 입력하세요 >>> "))

# if n <= 0:
#     print("잘못된 입력입니다.")

# i = 0
# while i < n:
#     i += 1
#     print("{}번째 Hello".format(i))

# # 응용예제 2번
# i = 1

# while i < 100:
#     if i % 7 == 0:
#         print(i)
#     i += 1

# # 응용예제 3번
# money = int(input("자판기에 얼마를 넣을까요? >>> "))

# coffee = 0
# while money > 0:
#     if money > 300:
#         print("커피 {}잔, 잔돈 {}원".format(coffee + 1, money - 300))
#     coffee += 1
#     money -= 300

# 응용예제 4번
# number = set({})

# while True:
#     num = int(input("0 ~ 9 사이 정수를 입력하세요 >>> "))
#     number.add(num)
#     if len(number) == 5:
#         print("모두 입력되었습니다.")
#         print("입력된 값은 {}입니다.".format(number))
#         break

# # 응용예제 5번
# i = 1

# while i <= 100:
#     if i % 10 == 0:
#         print(i)
#     elif i < 10:
#         print(i, end = '     ')
#     else:
#         print(i, end = '    ')
#     i += 1

# # 응용예제 6번
# num = 2
# while num <= 9:
#     n = 1
#     while n <= 9:
#         print('{}x{}={}'.format(num, n, num*n))
#         n += 1
#     num += 1

# # page 120 기본예제
# pwd = input("비밀번호를 입력하세요 >>> ")

# ch_count = 0
# num_count = 0

# for ch in pwd:
#     if ch.isalpha():
#         ch_count += 1
#     elif ch.isnumeric():
#         num_count += 1
    
# if ch_count > 0 and num_count > 0:
#     print("가능한 비밀번호입니다.")
# else:
#     print("불가능한 비밀번호입니다.")

# # page 125 기본예제
# dan = int(input("출력할 구구단을 입력하세요 >>> "))
# for n in range(1,10):
#     print("{} x {} = {}".format(dan, n, dan*n))

# # page 128 기본예제
# eng_dict = {
#     'sun' : '태양',
#     'moon' : '달',
#     'star' : '별',
#     'space' : '우주'
#     }
# for word in eng_dict:
#     print("{}의 뜻: {}".format(word, eng_dict.get(word)))

# # page 129
# # 응용예제 1번
# for i in range(5, 0, -1):
#     print(i)

# # 응용예제 2번
# num = int(input("임의의 양수를 입력하세요 >>> "))

# sum= 0
# for i in range(1, num+1):
#     sum += i
# print("1부터 5사이 모든 정수의 합계는 {}입니다.".format(sum))

# # 응용예제 3번
# basket = []

# n = int(input("몇 개의 과일을 보관할까요? >>> "))

# for i in range(n):
#     fruit =  input("{}번째 과일을 입력하세요 >>> ".format(i+1))
#     basket.append(fruit)
# print("입력받은 과일들은 {}입니다.".format(basket))

# # 응용예제 4번
# exam = [99, 78, 100,91, 81, 85, 54, 100, 71, 50]
# score = []

# for i in exam:
#     if exam < 100:
#         exam += 5
#         score.append(exam)
#     else:
#         score.append(exam)
# print(score)

# # 응용예제 5번

# # page 136 기본예제
# while True:
#     city = input("대한민국의 수돈느 어디인가요? >>> ")
#     if city == '서울' or city == 'seoul' or city == 'SEOUL':
#         print('정답입니다.')
#         break
#     else:
#         print('오답입니다. 다시 시도하세요.')

# # page 137 기본예제
# hobbies = []
# while True:
#     hobby = input('취미를 입력하세요(종료는 그냥 엔터) >> ')
#     if hobby == '':
#         print("입력된 취미가 모두 저장되었습니다.")
#         break
#     else:
#         hobbies.append(hobby)
#     print(hobbies)

# # page 139 기본예제
# fruits = ['사과', '감귤']
# count = 3

# while count > 0:
#     fruit = input("어떤 과일을 저장할까요? >>> ")
#     if fruit in fruits:
#         print("동일한 과일이 있습니다")
#         continue
#     fruits.append(fruit)
#     count -= 1
#     print("입력이 {}번 남았습니다".format(count))

# print("5개 과일은 {}입니다.".format(fruits))

# # page 140 기본예제
# count = 0
# total = 0
# while count < 5:
#     n = int(input("{}번째 정수를 입력하세요 >>> ".format(count + 1)))
#     if n <= 0:
#         print("0 이하의 정수는 처리할 수 없습니다.")
#         continue
#     total += n
#     count += 1
# print("입력된 5개의 양수의 총 합은 {}입니다.".format(total))

# # page 141
# # 응용예제 1번
# money = 10000

# while money > 0:
#     print("현재 {}원이 있습니다.".format(money))
#     num = int(input("사용할 금액 입력 >>> "))
#     if num < 0:
#         print("0 이하의 금액은 사용할 수 없습니다.")
#         continue
#     if num > money:
#         print("{}이 부족합니다.".format(num - money))
#         continue
#     money -= num
#     if money == 0:
#         print("현재 0원이 있습니다.")
#         break

# # 응용예제 2번

# # 응용예제 3번

# # 응용예제 4번
