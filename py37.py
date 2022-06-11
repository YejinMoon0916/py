'''
# page 199 (1)
def vending_machine(money):
    juice = 0
    print("음료수 = {}개, 잔돈 = {}원".format(juice, money))
    while money > 700:
        juice += 1
        money -= 700
        print("음료수 = {}개, 잔돈 = {}원".format(juice, money))
    return money

order = int(input("얼마를 내시나요? >>> "))
vending_machine(order)
'''

'''
# page 199 (1)
def vending_machine(money):
    total = money // 700
    juice = 0
    for juice in range(total):
        print("음료수 = {}개, 잔돈 = {}원".format(juice, money))
        juice += 1
        money -= 700
    print("음료수 = {}개, 잔돈 = {}원".format(juice, money))

order = int(input("얼마를 내시나요? >>> "))

vending_machine(order)
'''

# 연습
def 절댓값더하기(숫자1, 숫자2):
    if 숫자1 < 0:
        숫자1 = 숫자1 * -1
        결과 = 숫자1 + 숫자2
    if 숫자2 < 0:
        숫자2 = 숫자2 * -1
        결과 = 숫자1 + 숫자2
    if 숫자1 > 0 and 숫자2 > 0:
        결과 = 숫자1 + 숫자2
    return 결과

print(절댓값더하기(3, -1))
print(절댓값더하기(5, 2))
print(절댓값더하기(-3, -2))

입력1 = int(input("숫자1를 입력하세요. >>> "))
입력2 = int(input("숫자2를 입력하세요. >>> "))
print(절댓값더하기(입력1, 입력2))

'''
def 절댓값더하기(숫자1, 숫자2):
    if 숫자1 < 0:
        숫자1 = 숫자1 * -1
    if 숫자2 < 0:
        숫자2 = 숫자2 * -1
    return 숫자1 + 숫자2

print(절댓값더하기(3, -1))
print(절댓값더하기(5, 2))
print(절댓값더하기(-3, -2))
'''