import cv2
import mediapipe as mp                  # pip install mediapipe

mpDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpDetection.FaceDetection()

img = cv2.imread("img6.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceDetection.process(imgRGB)

# mpDraw.draw_detection(img, results.detections.location_data)
print(results)
cv2.imshow("my title", img)
cv2.waitKey(0)