import cv2 as cv
import mediapipe as mp
import time

# 初始化攝影機
# cap = cv.VideoCapture(0)
cap = cv.VideoCapture("./hand.mp4")

# 初始化手部檢測模組
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 初始化繪製工具
mp_draw = mp.solutions.drawing_utils
point_style = mp_draw.DrawingSpec(color=(81, 236, 255), thickness=7) # 設定點的樣式
line_style = mp_draw.DrawingSpec(color=(229, 199, 205), thickness= 5) # 設定線的樣式



def f1(img, landmark):
    """處理每個點輸出值的格式：
    在 Mediapipe 中，landmark 的值是归一化的图像坐标，而不是像素坐标。这意味着它们的值位于 [0, 1] 的范围内，
    表示它们相对于图像宽度和高度的比例位置。
    """
    img_height = img.shape[0]
    img_width = img.shape[1]
    x_pos = int(landmark.x * img_width)
    y_pos = int(landmark.y * img_height)
    return x_pos, y_pos

# 在循环开始之前获取开始时间戳
start_time = time.time()

# DOC: 計算幀率
def f2(img):
    global start_time
    end_time = time.time() # 在循环的每次迭代结束时获取结束时间戳
    elapsed_time = end_time - start_time # 计算每次循环的持续时间
    fps = 1 / elapsed_time # 计算帧率（FPS）
    cv.putText(img, f"FPS: {int(fps)}", (30, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    start_time = time.time() # 更新开始时间戳，以便下一次循环
    


while True:
    # 從攝影機讀取影像
    ret, img = cap.read()

    if ret:
        # img = cv.resize(img, (500, 300))  # 調整影像大小
        img = cv.resize(img, (0, 0), fx=0.3, fy=0.3)  # 調整影像大小
        # 將影像從 BGR 轉換為 RGB (MediaPipe需要RGB格式)
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # 進行手部檢測
        results = hands.process(imgRGB)
        # 如果檢測到手
        if results.multi_hand_landmarks:
            # 遍歷每一隻檢測到的手
            for i in results.multi_hand_landmarks:
                # 在影像上繪製手部關鍵點(img, 參數、連接手、點的樣式、線的樣式)
                mp_draw.draw_landmarks(img, i, mp_hands.HAND_CONNECTIONS, point_style, line_style) 
                # 印出單隻手上的21個點
                for index, landmark in enumerate(i.landmark):
                    x_pos, y_pos = f1(img, landmark) # 處理每個點輸出值的格式
                    # print(index, x_pos, y_pos)

                    # DOC: 將手指標示索引
                    # cv.putText(img, str(index), (x_pos-25, y_pos+5), cv.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 2)

                    # DOC: 針對某個手指點放大(設定第四個參數)
                    # if index == 4:
                    #     cv.circle(img, (x_pos, y_pos), 20, (0, 0, 255), cv.FILLED)

        # DOC: 計算幀率
        f2(img) 

        # 顯示處理後的影像
        cv.imshow("img", img)

        # 按下任意鍵退出
        if cv.waitKey(1) != -1:
            break

# 釋放資源
cap.release()
cv.destroyAllWindows()
