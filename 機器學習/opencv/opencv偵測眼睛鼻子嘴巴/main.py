import cv2

""" 可以調整參數"""
img = cv2.imread('./woman.jpg')
eye_cascade = cv2.CascadeClassifier("./models/haarcascade_eye.xml")  # 使用眼睛模型
mouth_cascade = cv2.CascadeClassifier("./models/haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
nose_cascade = cv2.CascadeClassifier("./models/haarcascade_mcs_nose.xml")    # 使用鼻子模型



# =============================================================================
# 做偵測照片之用途
# =============================================================================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
# gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)      # 標記綠色方框


mouths = mouth_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框


noses = nose_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              # 標記藍色方框

cv2.imshow('img', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()



# =============================================================================
# 做偵測影片之用途
# =============================================================================
# import cv2
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Cannot receive frame")
#         break
#     img = cv2.resize(frame,(540,320))
#     gray = cv2.medianBlur(img, 1)
#     gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
#     gray = cv2.medianBlur(gray, 5)

#     eyes = eye_cascade.detectMultiScale(gray)      # 偵測眼睛
#     for (x, y, w, h) in eyes:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     mouths = mouth_cascade.detectMultiScale(gray)  # 偵測嘴巴
#     for (x, y, w, h) in mouths:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

#     noses = nose_cascade.detectMultiScale(gray)    # 偵測鼻子
#     for (x, y, w, h) in noses:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     cv2.imshow('img', img)
#     if cv2.waitKey(1) == ord('q'):
#         break     # 按下 q 鍵停止

# cap.release()
# cv2.destroyAllWindows()