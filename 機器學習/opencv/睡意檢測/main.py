import cv2 as cv
import mediapipe as mp
import numpy as np
from playsound import playsound
# =============================================================================
# 眼睛閉眼：參照“眼睛纵横比”（EAR）
# 可以參考 https://developer.aliyun.com/article/336184
# =============================================================================

def EAR(landmarks):
    # 计算眼睛的水平距离
    horizontal_dist1 = np.linalg.norm(landmarks[1] - landmarks[5])
    horizontal_dist2 = np.linalg.norm(landmarks[2] - landmarks[4])
    # 计算眼睛的垂直距离
    vertical_dist = np.linalg.norm(landmarks[0] - landmarks[3])
    # 计算EAR
    ear = (horizontal_dist1 + horizontal_dist2) / (2.0 * vertical_dist)
    return ear


"""比較重要的眼睛的點"""
class CFG:
    sleep_count = 0  # 記錄閉眼次數的變數,初始值為 0
    sleep_deadline = 10  # 閉眼次數的閾值,當超過此值時會觸發提醒
    right_eye_landmark_id = [362, 385, 387, 263, 373, 380]  # 右眼特徵點的索引
    left_eye_landmark_id = [33, 160, 158, 133, 153, 144]  # 左眼特徵點的索引



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



def f2(left_eye_landmark, right_eye_landmark):
    """根據眼睛的縱橫比檢測閉眼狀態,如果閉眼次數超過閾值就播放音效提醒"""
    left_EAR = EAR(left_eye_landmark)
    right_EAR = EAR(right_eye_landmark)
    # 如果平均縱橫比小於 0.8,視為閉眼
    if (left_EAR+right_EAR)/2<0.80:
        CFG.sleep_count+=1
        # print(CFG.sleep_count)
        if CFG.sleep_count > CFG.sleep_deadline:
            playsound("./睡你媽起來嗨.mp3")
    else:
        # print(CFG.sleep_count)
        CFG.sleep_count = 0




# 初始化人臉網格模型
face_mesh = mp.solutions.face_mesh.FaceMesh()
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        # 將影像從 BGR 轉換為 RGB (MediaPipe需要RGB格式)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        # 進行人臉網格偵測
        result = face_mesh.process(frame)
        # 檢查是否偵測到人臉
        if result.multi_face_landmarks:
            # 遍歷每一個偵測到的人臉
            for i in result.multi_face_landmarks:

                # TEST: 抓特定一點出來
                # x_pos, y_pos = f1(frame, i.landmark[362])
                # cv.circle(frame, (x_pos, y_pos), 4, (0, 255, 0), thickness=cv.FILLED, lineType=cv.LINE_AA)

                left_eye_landmark = []
                right_eye_landmark = []
                # 遍歷該人臉的每個地標點
                for index,landmark in enumerate(i.landmark):
                    # 如果是右眼特徵點
                    if index in CFG.right_eye_landmark_id:
                        # print(landmark.x, landmark.y)
                        x_pos, y_pos = f1(frame, landmark) # 處理每個點輸出值的格式
                        cv.circle(frame, (x_pos, y_pos), 3, (0, 255, 0), thickness=cv.FILLED, lineType=cv.LINE_AA)
                        right_eye_landmark.append(np.array([x_pos, y_pos])) 
                    # 如果是左眼特徵點
                    if index in CFG.left_eye_landmark_id:
                        x_pos, y_pos = f1(frame, landmark) # 處理每個點輸出值的格式
                        cv.circle(frame, (x_pos, y_pos), 3, (0, 255, 0), thickness=cv.FILLED, lineType=cv.LINE_AA)
                        left_eye_landmark.append(np.array([x_pos, y_pos])) 

                # 檢測閉眼狀態
                f2(left_eye_landmark, right_eye_landmark)

        cv.imshow("frame", frame)
        # 按下任意鍵退出
        if cv.waitKey(1) != -1:
            break
