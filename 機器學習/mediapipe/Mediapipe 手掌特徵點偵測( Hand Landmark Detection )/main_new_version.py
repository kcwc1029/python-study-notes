import cv2 # 導入 OpenCV 函式庫用於影像處理
import numpy as np # 導入 NumPy 函式庫用於數值運算
import mediapipe as mp # 導入 MediaPipe 函式庫用於手掌偵測

from mediapipe import solutions # 導入 MediaPipe 解決方案模組
from mediapipe.framework.formats import landmark_pb2 # 導入 MediaPipe 地標資料格式

BaseOptions = mp.tasks.BaseOptions # 基本選項類別
HandLandmarker = mp.tasks.vision.HandLandmarker # 手掌地標檢測器類別
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions # 手掌地標檢測器選項類別
VisionRunningMode = mp.tasks.vision.RunningMode # 視覺運行模式類別

# 手掌偵測設定
options = HandLandmarkerOptions(
   num_hands=2, # 最多偵測兩隻手掌
   base_options=BaseOptions(model_asset_path='./hand_landmarker.task'), # 手掌偵測模型路徑
   running_mode=VisionRunningMode.IMAGE) # 以影像模式運行


# 標記文字
MARGIN = 10 # 像素邊距
FONT_SIZE = 1 # 字體大小
FONT_THICKNESS = 1 # 字體粗細
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # 手勢文字顏色 

# 繪製手掌骨架
def draw_landmarks_on_image(rgb_image, detection_result):
   hand_landmarks_list = detection_result.hand_landmarks # 手掌地標列表
   handedness_list = detection_result.handedness # 手勢列表
   annotated_image = np.copy(rgb_image) # 複製原始影像

   # 遍歷偵測到的手掌進行視覺化
   for idx in range(len(hand_landmarks_list)):
       hand_landmarks = hand_landmarks_list[idx] # 取得每隻手掌的地標
       handedness = handedness_list[idx] # 取得每隻手掌的手勢

       # 繪製手掌地標
       hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
       hand_landmarks_proto.landmark.extend([
           landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
       ])
       solutions.drawing_utils.draw_landmarks(
           annotated_image,
           hand_landmarks_proto,
           solutions.hands.HAND_CONNECTIONS, # 手掌骨架連接
           solutions.drawing_styles.get_default_hand_landmarks_style(), # 手掌地標樣式
           solutions.drawing_styles.get_default_hand_connections_style()) # 手掌骨架樣式

       # 取得偵測手掌邊界框的左上角座標
       height, width, _ = annotated_image.shape
       x_coordinates = [landmark.x for landmark in hand_landmarks] # x 座標
       y_coordinates = [landmark.y for landmark in hand_landmarks] # y 座標
       text_x = int(min(x_coordinates) * width) # 左上角 x 座標
       text_y = int(min(y_coordinates) * height) - MARGIN # 左上角 y 座標

       # 在影像上繪製手勢文字 (左手或右手)
       cv2.putText(annotated_image, f"{handedness[0].category_name}", # 文字內容
                   (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX, # 字體
                   FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA) # 字體大小、顏色、粗細

   return annotated_image

# 建立手掌地標檢測器
with HandLandmarker.create_from_options(options) as landmarker:
   cap = cv2.VideoCapture("./hand2.mp4") # 開啟攝影機
   if not cap.isOpened():
       print("無法開啟攝影機")
       exit()

   while True:
       ret, frame = cap.read() # 讀取影像框架
       w = frame.shape[1] # 畫面寬度
       h = frame.shape[0] # 畫面高度

       if not ret:
           print("無法接收影像框架")
           break

       mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame) # 建立 MediaPipe 影像
       hand_landmarker_result = landmarker.detect(mp_image) # 偵測手掌地標

       print(hand_landmarker_result.handedness) # 印出手勢 (左手或右手)

       annotated_image = draw_landmarks_on_image(frame, hand_landmarker_result) # 繪製手掌骨架與文字
       cv2.imshow('annotated_image', annotated_image) # 顯示處理後的影像

       if cv2.waitKey(5) == ord('q'):
           break # 按下 q 鍵停止

   cap.release() # 釋放攝影機
   cv2.destroyAllWindows() # 關閉所有視窗