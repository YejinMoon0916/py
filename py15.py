'''
1. 연산자
덧셈 : A + B
뺄셈 : A - B
곱셈 : A * B
나눗셈 : A / B (A // B)
나머지값 : A % B
거듭제곱 : A ** B

대입 : A = B
같다 : A == B
다르다 : A != B
크다 : A > B
작다 : A < B
이상 : A >= B
이하 : A <= B

2. 누적 연산 (계산하고 자신한테 다시 저장)
덧셈 : A += B
뺄셈 : A -= B
곱셈 : A *= B   (A = A * B)
나눗셈 : A /= B (A = A / B)

3. 연산자(연산기호)의 우선순위
(1) 괄호 : A * (B + 2)
(2) 사칙연산 : *, /, +, -, %
(3) 비교 : A + B > C (덧셈 끝난 다음에 C와 비교)
(4) 왼쪽에 있는 거부터
'''
# page 78

a = 15

print("{} > 10 : {}".format(a, a>10)) 
print("{} < 10 : {}".format(a, a<10)) 
print("{} >= 10 : {}".format(a, a>=10)) 
print("{} <= 10 : {}".format(a, a<=10))
print("{} == 10 : {}".format(a, a==10))
print("{} != 10 : {}".format(a, a!=10))

# page 79
# 0 : False(거짓)
# 0을 제외한 모든 숫자 : True(참)

a = 10          # True (0을 제외한 모든 것은 True)
b = 0           # False

print("{} > 0 and {} > 0 : {}".format(a, b, a>0 and b>0))
print("{} > 0 or {} > 0 : {}".format(a, b, a>0 or b>0))
print("not {} : {}".format(a, not a))
print("not {} : {}".format(b, not b))
