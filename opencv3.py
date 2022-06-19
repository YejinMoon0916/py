import cv2                                                                              # pip install opencv-python     # pip install python-opencv
from PIL import ImageFont, ImageDraw, Image                                             # pip install PIL
import numpy as np
                                                                                        # pip install pyinstaller # pyinstaller -w -F --icon="myico.ico" "opencv3.py"

def hangulText(image, text, pos, size, color):
    img_pil = Image.fromarray(image)                                                    # 이미지를 np리스트형태로 만든다
    img_draw = ImageDraw.Draw(img_pil)                                                  # 그림을 그릴 공간 지정
    font = ImageFont.truetype("HMKMAMI.TTF", size)                                      # 폰트와 사이즈 설정
    img_draw.text(pos, text, font=font, fill=color)                                     # 글자 그리기
    return np.array(img_pil)

width = 348
height = 348
origin_pos = np.array([[80,155],[282,155],[80,348],[282,348]], dtype = np.float32)      # 80 155px 왼쪽 위 # 282 155px 오른쪽 위 # 282 348px 오른쪽 아래 # 80 348px 왼쪽 아래
change_pos = np.array([[0,0],[width,0],[0,height],[width,height]], dtype = np.float32)
matrix = cv2.getPerspectiveTransform(origin_pos, change_pos)

img = cv2.imread("image10.jpg")                                                         # 이미지 읽기
img_change = cv2.warpPerspective(img,matrix, (width, height))

img_change = hangulText(img_change, "문예진", (10,10), 30, (255, 0, 255))

cv2.imshow("my title", img)                                                             # 원본 이미지 보여주기
cv2.imshow("change image", img_change)                                                  # 자른 이미지 보여주기
cv2.waitKey(0)                                                                          # 무한대기

