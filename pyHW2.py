# page 141 (1)
money = 10000
while True:
    print("현재 {}원이 있습니다.".format(money))
    use = int(input("사용할 금액 입력 >>> "))
    if use < 0:
        print("0 이하의 금액은 사용할 수 없습니다.")
        continue
    if use > money:
        print("{}원이 부족합니다.".format(use-money))
        continue
    money -= use
    if money == 0:
        print("현재 0원이 있습니다.")
        break
