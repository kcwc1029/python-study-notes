import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

# 启用姿势检测
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(520,300))
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img2)


        # 检查是否检测到左手
        if results.pose_landmarks and results.pose_landmarks.landmark:
            left_hand_landmarks = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            nose_landmarks = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
            print("左手位置：", left_hand_landmarks)
            print("鼻子位置：", nose_landmarks)
            if left_hand_landmarks.y < nose_landmarks.y: print("你舉手")
            else: print("你沒舉手")

        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        cv2.imshow('img', img)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
