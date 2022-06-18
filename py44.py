import csv                                              # import 파일 복봍
경로 = "C:\\Users\\Public\\Desktop\\내파일.csv"

# 함수 정의
def 엑셀쓰기(text):
    f = open(경로, "w", newline = "")
    내용 = csv.writer(f)
    내용.writerow(text)
    f.close()

def 엑셀추가쓰기(text):
    f = open(경로, "a", newline = "")
    내용 = csv.writer(f)
    내용.writerow(text)
    f.close()

def 엑셀읽기():
    f = open(경로, "r", newline = "")
    내용 = csv.reader(f)                                     # 엑셀 내용 전부 읽어옴

    for row in 내용:
        for col in row:
            print(col, end = " ")
        print()
    f.close

# 함수 사용
