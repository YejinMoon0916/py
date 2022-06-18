# # 클래스 정의(설계)
# class 자동차:
#     def __init__(self, 차주인, 차종):
#         self.name = 차주인
#         self.car = 차종

#     def 차정보(self):
#         print("{}차의 주인은 {}입니다.".format(self.car, self.name))
#     def 차변경(self, 차종):
#         self.car = 차종
#     def __del__(self):
#         print("{}차 안내 종료".format(self.name))

# # 클래스 사용
# # 객체화(클래스 사용을 위해 변수로 만들어 줌)
# 아빠차 = 자동차("아빠", "벤츠")                          # 클래스 사용1
# 엄마차 = 자동차("엄마", "아반떼")                        # 클래스 사용1
# 내차 = 자동차("나", "K5")                               # 클래스 사용1

# 아빠차.차정보()
# 엄마차.차정보()
# 내차.차정보()
# del 아빠차                                              # 아빠차 변수를 강제로 없앰
# 엄마차.차변경("제네시스")
# 엄마차.차정보()
# # 아빠차.차정보()                                        # 아빠차 변수가 이미 없어졌으므로 사용 불가

# page 287 (1)
population = 0
class Person:
    def __init__(self, person):
        global population
        population += 1
        self.person = person
        print("{} is born".format(self.person))
                                                                            # @staticmethod
    def get_population(self):                                               # def get_population(self):
        return population                                                         #print("전체 인구수: {}명".format(population))

    def __del__(self):
        global population
        population -= 1
        print("{} is dead".format(self.person))

man = Person("james")
woman = Person("emily")
print("전체 인구수: {}명".format(population))                                 # Person.get_population()
del man
print("전체 인구수: {}명".format(population))                                 # Person.get_population()
