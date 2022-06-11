import py35                     # py35.py 파일을 복사붙여넣기
import py35 as p                # py35.py 파일을 복사붙여넣기하고 p라는 키워드로 사용하기
from py35 import 이미지띄우기    # py35.py 파일 중 이미지띄우기 만 가져오기
import random                   # random.py 파일을 복사붙여넣기

# py35 안에 있는 이미지띄우기()
py35.이미지띄우기()
py35.이미지띄우기2("img2.jpg")
p.회색이미지("img3.jpg")
이미지띄우기()

# random.py 파일 안에 있는 randint 라는 함수를 사용
print(random.randint(1,11))