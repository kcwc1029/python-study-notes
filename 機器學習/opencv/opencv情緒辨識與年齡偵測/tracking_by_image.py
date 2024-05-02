import cv2
from deepface import DeepFace
import numpy as np

img = cv2.imread('./lady.jpg')     # 讀取圖片
try:
    analyze = DeepFace.analyze(img)  # 辨識圖片人臉資訊
    print(analyze)

    emotion = DeepFace.analyze(img, actions=['emotion'])  # 情緒
    age = DeepFace.analyze(img, actions=['age'])          # 年齡
    race = DeepFace.analyze(img, actions=['race'])        # 人種
    gender = DeepFace.analyze(img, actions=['gender'])    # 性別

    # print(emotion[0]['dominant_emotion']) # emotion
    # print(age[0]['age']) # age
    # print(race[0]['dominant_race']) # race
    # print(gender[0]['gender'])
    # print(gender[0]['dominant_gender']) # gender
    

    text1 = f"emotion: {emotion[0]['dominant_emotion']} age: {age[0]['age']} "
    text2 = f"race: {race[0]['dominant_race']} gender: {gender[0]['dominant_gender']}"
    # 獲取圖像的尺寸
    height, width, _ = img.shape

    # 計算文字區域的尺寸
    (text_width, text_height), _ = cv2.getTextSize(text1, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

    # 計算文字需要放置的起始位置座標
    x = (width - text_width) // 2
    y = (height + text_height) // 2

    # 在圖像中央繪製文字
    cv2.putText(img, text1, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.putText(img, text2, (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # cv2.putText(img, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), thickness=1, lineType=cv2.LINE_AA, bottomLeftOrigin=False)
except:
    pass

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

