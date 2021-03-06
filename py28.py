'''
# 1. 리스트 (== 문자열)
lst = []                    # 리스트 변수 선언

# 추가하기
lst.append(3)
lst.append(3.14)
lst.append('안녕하세요')

# 삽입하기(중간에 추가)
lst.insert(1, '1번에 추가')

# 수정하기
lst[1] = "1번방 수정"

# 제거하기
lst.pop(-1)                 # -값은 뒤에서부터 계산, (앞에서부턴 0 부터, 뒤에서부턴 -1부터)

# 잘라내기
print(lst[0:2])             # 0 ~ 1까지 잘라냄

for i in lst:
    print(i, end=", ")
'''

# page 129 (3)
basket = []
num = 0

count = int(input("몇 개의 과일을 보관할까요? >>> "))
while count > num:
    fruit = input("{}번째 과일을 입력하세요 >>> ".format(num+1))
    basket.append(fruit)
    num += 1
print("입력받은 과일은 {}입니다.".format(basket))

'''
basket = []

count = int(input("몇 개의 과일을 보관할까요? >>> "))
for i in range(count):
    fruit = input("{}번째 과일을 입력하세요 >>> ".format(i+1))
    basket.append(fruit)
print("입력받은 과일은 {}입니다.".format(basket))
'''