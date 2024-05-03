import cv2
import numpy as np

import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

# 設定方法
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


# 人臉偵測設定
options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='./face_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE)


# 執行人臉偵測
with FaceLandmarker.create_from_options(options) as landmarker:
    cap = cv2.VideoCapture("../MediaPipe偵測人臉/lady.mp4")               # 讀取攝影鏡頭
    while True:
        ret, frame = cap.read()             # 讀取影片的每一幀
        w = frame.shape[1]                  # 畫面寬度
        h = frame.shape[0]                  # 畫面高度
        img = cv2.resize(frame,(0,0), fx=1, fy=1)                 # 調整影像尺寸為 480x320
        output = np.zeros((h,w,3), dtype='uint8')     # 繪製 480x320 的黑色畫布
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)       # 轉換顏色




        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img2) # 換成 img2
        face_landmarker_result = landmarker.detect(mp_image)

        face_landmarks_list = face_landmarker_result.face_landmarks
        annotated_image = np.copy(output)

        # Loop through the detected faces to visualize.
        for idx in range(len(face_landmarks_list)):
            face_landmarks = face_landmarks_list[idx]

            """ 繪製人臉特徵點 """
            face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            face_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
            ])# 將人臉特徵點資料填入 NormalizedLandmarkList

            
            """ 使用 drawing_utils 模組繪製人臉特徵點 """
            solutions.drawing_utils.draw_landmarks(
                image=annotated_image, # 要標記的影像
                landmark_list=face_landmarks_proto, # 人臉特徵點清單
                connections=mp.solutions.face_mesh.FACEMESH_TESSELATION, # 繪製人臉網格
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style())
            
            """ 繪製人臉輪廓 """
            solutions.drawing_utils.draw_landmarks(
                image=annotated_image,
                landmark_list=face_landmarks_proto,
                connections=mp.solutions.face_mesh.FACEMESH_CONTOURS, # 繪製人臉輪廓
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())
            
            """ 繪製眼睛虹膜 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_IRISES, # 繪製眼睛虹膜
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_iris_connections_style())
            
            """ 繪製左眼 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_LEFT_EYE, # 左眼
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())
            
            """ 繪製右眼 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_RIGHT_EYE, # 右眼
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())
            
            """ 繪製左眉 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_LEFT_EYEBROW, # 左眉
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())
            
            """ 繪製右眉 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_RIGHT_EYEBROW, # 右眉
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())

            """ 繪製鼻子 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_CONTOURS, # 繪製鼻子
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())
            
            """ 繪製嘴唇 """
            # solutions.drawing_utils.draw_landmarks(
            #     image=annotated_image,
            #     landmark_list=face_landmarks_proto,
            #     connections=mp.solutions.face_mesh.FACEMESH_LIPS, # 繪製嘴唇
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())

            
            
            
            """ 針對某些點去畫圓 """
            for landmark_idx in [37, 0, 267, 269, 270, 409]:
                landmark = face_landmarks[landmark_idx]
                landmark_x = int(landmark.x * w)
                landmark_y = int(landmark.y * h)
                cv2.circle(annotated_image, (landmark_x, landmark_y), 5, (0, 255, 0), -1)  # Draw a green circle with radius 5



        #print(face_landmarker_result)
        if not ret:
            print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
            break
        cv2.imshow('img', img)     # 如果讀取成功，顯示該幀的畫面
        cv2.imshow('img2', img2)     # 如果讀取成功，顯示該幀的畫面
        cv2.imshow('annotated_image', annotated_image)     # 如果讀取成功，顯示該幀的畫面
        if cv2.waitKey(10) == ord('q'):     # 每一毫秒更新一次，直到按下 q 結束
            break
    cap.release()                           # 所有作業都完成後，釋放資源
    cv2.destroyAllWindows()                 # 結束所有視窗
