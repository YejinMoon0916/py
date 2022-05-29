# page 86 5번
# input
kor= int(input("국어 점수를 입력하세요 >>> "))
eng= int(input("영어 점수를 입력하세요 >>> "))
math= int(input("수학 점수를 입력하세요 >>> "))

avg = (kor + eng + math) / 3

if avg >= 80:
    print("평균은 {}점이고, 결과는 합격입니다.".format(avg))
else:
    print("평균은 {}점이고, 결과는 불합격 입니다.".format(avg))