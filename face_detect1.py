import cv2                              # pip install opencv-python
import mediapipe as mp                  # pip install mediapipe

# 이미지에서 얼굴 찾기
cap = cv2.VideoCapture("img6.jpg")

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.25)              # 25% 이상 얼굴로 인식될 경우

success, img = cap.read()
if success:
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
    cv2.imshow("Image", img)                             # 얼굴 위치에 네모표시
    cv2.waitKey(0)