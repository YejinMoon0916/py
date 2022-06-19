import pandas as pd
from openpyxl.workbook import Workbook                                                                  # xlsx
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def 표만들기():
    번호 = [1,2,3]
    data = {
        '이름':['홍길동', '아무개', '김철수'],
        '키':[175.5, 166.3, 180.0],
        '몸무게':[66.8, 50.7, 80.8]
    }

    df = pd.DataFrame(data, index=번호)
    print(df)

    # 쓰기
    df.to_csv('myTable.txt', sep='\t')                                                                  # 메모장
    df.to_excel('myTable.xlsx', index=False)                                                            # 엑셀

    # 읽기
    df2 = pd.read_excel('myTable.xlsx')
    print(df2)

# page 340
def 꺽은선형그래프():
    font_name = font_manager.FontProperties(fname="HMKMAMI.TTF").get_name()
    plt.rc("font", family=font_name)

    figure = plt.figure()
    axes = figure.add_subplot(111)                                                                      # 한개의 화면에 하나의 표 만들기
    x = ['1월','2월','3월','4월','5월','6월']                                                            # 가로축
    y = [1200,800,500,400,700,800]                                                                      # 세로축
    axes.plot(x,y,linestyle='--', marker = '^')
    
    plt.title('상반기 실적')
    plt.show()

'''
def 원형그래프():
    figure = plt.figure()
    axes = figure.add_subplot(111)
    data = [1,2,3]                                                                                      # 리스트 값
    label = ['Good','Bad','Normal']
    axes.pie(data, labels=label, autopct='%d%%')                                                        # pie 데이터 넘김

    plt.axis('equal')
    plt.legend(label, loc='center left')
    plt.show()
'''

'''
# page 348 (1)
def 원형그래프1():
    font_name = font_manager.FontProperties(fname="HMKMAMI.TTF").get_name()
    plt.rc("font", family=font_name)

    figure = plt.figure()
    axes = figure.add_subplot(111)
    data = [0.18,0.3,3.33,3.75,0.38,25,0.25,2.75,0.1]                                                   # 리스트 값
    label = ['비타민A','비타민B1','비타민B2','나이아신','비타민B6','비타민C','비타민D','비타민E','엽산']                         
    axes.pie(data, labels=label, autopct='%d%%')                                                        # pie 데이터 넘김

    plt.axis('equal')
    plt.legend(label, loc='center left')
    plt.show()

원형그래프1()
'''

def 원형그래프(data, y):
    font_name = font_manager.FontProperties(fname="HMKMAMI.TTF").get_name()
    plt.rc("font", family=font_name)

    plt.pie(data, autopct='%d%%')
    plt.legend(y, loc="center left")
    plt.title("비타민 함량")
    plt.show()

data = [0.18,0.3,3.33,3.75,0.38,25,0.25,2.75,0.1]
label = ['비타민A','비타민B1','비타민B2','나이아신','비타민B6','비타민C','비타민D','비타민E','엽산'] 
원형그래프(data, label)
