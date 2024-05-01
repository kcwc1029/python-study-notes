import cv2
""" 可以調整參數"""
cap = cv2.VideoCapture("./car.mp4")
car = cv2.CascadeClassifier("./models/cars.xml")    # 讀取汽車模型


""" main """
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    # img = cv2.resize(frame,(540,320))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # 轉換成黑白影像
    gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊
    cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)       # 偵測汽車
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 繪製外框


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break     # 按下 q 鍵停止

cap.release()
cv2.destroyAllWindows()