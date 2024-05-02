import cv2
# =============================================================================
# area = cv2.selectROI('視窗名稱', frame, showCrosshair=False, fromCenter=False)
# area：(x, y, width, height)
# frame：要選取的影像
# showCrosshair：選取框中間是否要有十字線，預設 True
# fromCenter：True 中心點選取，False 右上角選取
# =============================================================================

tracker = cv2.TrackerKCF_create()  # 創建追蹤器（直接查看readme）
tracking = False                    # 設定 False 表示尚未開始追蹤

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("./running.mp4")  
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(540,300))  # 縮小尺寸，加快速度
    keyName = cv2.waitKey(1)

    if keyName == ord('q'): # q 關閉程式
        break
    if keyName == ord('a'): # 暫停，進入擷取模式
        tracking = False
        area = cv2.selectROI('frame', frame, showCrosshair=True, fromCenter=False)
        tracker.init(frame, area)    # 初始化追蹤器
        tracking = True              # 設定可以開始追蹤
    if tracking:
        success, point = tracker.update(frame)   # 追蹤成功後，不斷回傳左上和右下的座標
        if success:
            p1 = [int(point[0]), int(point[1])]
            p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
            cv2.rectangle(frame, p1, p2, (0,0,255), 2)   # 根據座標，繪製四邊形，框住要追蹤的物件

    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()