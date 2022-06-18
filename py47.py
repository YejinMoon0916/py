# 두 수의 합
import service_identity


a = 3
b = 2
result = a + b
print(result)
a = 3
b = 2
result = a + b
print(result)
# 코드가 길어지면 지저분!!

# 그렇다면 함수를 이용하자
def Sum():
    result = a + b
    print(result)
def Sub():
    result = a - b
    print(result)
def Mul():
    result = a * b
    print(result)
def Div():
    result = a / b
    print(result)

# 함수 사용
# a, b = 3, 4
# Sum(a,b)
# Sum(3,6)
# 함수의 이름과 사용법을 알고 있어야함
# 초보자가 사용하기에는 어려움
# Sub(5,"6")      # 오류!!
# Div(7,2)        # 0 안됨!!

# 초보자가 사용하기 편하게 변수와 함수를 뭉쳐놓고 쉽게 제공하자
class 사칙연산:
    a, b = 0, 0             # self
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Sum(self):
        result = a + b
        print(result)
    def Sub(self):
        result = a - b
        print(result)
    def Mul(self):
        result = a * b
        print(result)
    def Div(self):
        result = a / b
        print(result)

객체1 = 사칙연산(3,5)               # class를 담는 것을 객체
객체1.Div()

class 더하기:
    # 두개더하기
    def 두개더하기(self, a, b):
        result = a + b
        print(result)
    # 세개더하기
    def 세개더하기(self, a, b, c):
        result = a + b + c
        print(result)
    # 네개더하기
    def 네개더하기(self, a, b, c, d):
        result = a + b + c + d
        print(result)
    def __init__(self):                 # 생성자
        print("처음에 무조건 사용됨")
    def __del__(self):                  # 파괴자
        print("끝날때 무조건 사용됨")

객체2 = 더하기()
객체2.두개더하기(1,2)
객체2.세개더하기(1,2,3)
객체2.네개더하기(1,2,3,4)

# page 277
class Service:
    def __init__(self, service):
        self.service = service
        print("{} Service가 시작되었습니다.".format(self.service))
    
    def __del__(self):
        print("{} Service가 종료되었습니다.".format(self.service))
    
s = Service('길 안내')
del s