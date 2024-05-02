import cv2
from deepface import DeepFace
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 定義該情緒的中文字
text_obj={
    'angry': '生氣',
    'disgust': '噁心',
    'fear': '害怕',
    'happy': '開心',
    'sad': '難過',
    'surprise': '驚訝',
    'neutral': '正常'
}

# 定義加入文字函式
def putText(x,y,text,size=40,color=(0,0,255)):
    global img
    fontpath = '../NotoSerifTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text_obj[text], fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array

cap = cv2.VideoCapture("./臉部偵測.mp4")

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
    # img = cv2.resize(frame,(384,240))

    try:
         
        emotion = DeepFace.analyze(img, actions=['emotion'])  # 情緒
        age = DeepFace.analyze(img, actions=['age'])          # 年齡
        race = DeepFace.analyze(img, actions=['race'])        # 人種
        gender = DeepFace.analyze(img, actions=['gender'])    # 性別
        text1 = f"emotion: {emotion[0]['dominant_emotion']} age: {age[0]['age']} "
        text2 = f"race: {race[0]['dominant_race']} gender: {gender[0]['dominant_gender']}"
        # 獲取圖像的尺寸
        height, width, _ = img.shape

        # 計算文字區域的尺寸
        (text_width, text_height), _ = cv2.getTextSize(text1, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

        # 計算文字需要放置的起始位置座標
        x = (width - text_width) // 2
        y = (height + text_height) // 2 + 50

        # 在圖像中央繪製文字
        cv2.putText(img, text1, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.putText(img, text2, (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)


    except:
        pass
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()