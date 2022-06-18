import py43
import py44
# page 238 1번
nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바','미국', '워싱턴']
idx = 0
py43.메모장쓰기('')
# txt
for i in nation:
    if idx % 2 == 0:
        py43.메모장추가쓰기(i)                  # 나라
    else:
        py43.메모장추가쓰기(' - '+ i +'\n')     # 수도
    idx += 1

# # cvs
# py44.엑셀쓰기('')
# for i in nation:
#     if idx % 2 == 0:
#         py44.엑셀추가쓰기(i)                    # 나라
#     else:
#         py44.엑셀추가쓰기('-'+ i)                    # 수도
#     idx += 1