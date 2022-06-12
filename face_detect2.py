import cv2                              # pip install opencv-python
import mediapipe as mp                  # pip install mediapipe

# 이미지에서 얼굴 찾기
cap = cv2.VideoCapture("video.mp4")                             # cap = cv2.VideoCapture(0) : 웹캠 (안된다면 -1-2.. 해보기)

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.30)              # 30% 이상 얼굴로 인식될 경우

while True:
    success, img = cap.read()
    if success:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)
        if results.detections:                                  # 얼굴을 찾았으면
            for id, detection in enumerate(results.detections):
                mpDraw.draw_detection(img, detection)
        cv2.imshow("Video", img)                             # 얼굴 위치에 네모표시
        if cv2.waitKey(20) & 0xFF == 27:
            break