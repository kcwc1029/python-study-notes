# 單目標追蹤與多目標追蹤

這個存放庫包含兩個 Python 腳本,用於單目標和多目標追蹤。

![upgit_20240502_1714638804.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240502_1714638804.png)

## 使用到的技能

-   OpenCV 電腦視覺庫
-   物體追蹤算法 (KCF, CSRT)

## 用途

單目標追蹤 (single_object_tracking.py)
此腳本可讓你選取視頻/相機影像中的單一目標物體,並使用 KCF 追蹤器對其進行追蹤。（可以自行更換追蹤器）

多目標追蹤 (multi_object_tracking.py)
此腳本允許你選取視頻/相機影像中的多個目標物體,並使用 CSRT 追蹤器分別對它們進行追蹤。（可以自行更換追蹤器）

## 使用方法

1. 執行腳本
2. 按下 `a` 鍵進入選取模式
3. 使用滑鼠拖曳選取需要追蹤的目標
4. 腳本會自動初始化追蹤器並開始追蹤
5. 按下 `q` 鍵退出

-   預設會讀取 `running.mp4` 視頻,你可以修改成其他視頻或相機輸入
-   調整 `cv2.resize` 參數可以控制視窗大小,提高追蹤效率
-   你可以在 `CFG` 類中修改要追蹤目標的數量和對應顏色

## 不同種物件追蹤

-   BOOSTING 速度慢 精確度差 元老級追蹤器，速度較慢，並且不是很準確。追蹤器為`cv2.TrackerBoosting_create()`
-   MIL：速度慢 精確度差 比 BOOSTING 更精確，但仍然不是很準確。追蹤器為`cv2.TrackerMIL_create()`
-   GOTURN：速度中 精確度中 需要搭配深度運算模型才能運作的追蹤器。追蹤器為`cv2.TrackerGOTURN_create()`
-   TLD：速度中 精確度中 速度普通，精準度普通的追蹤器。追蹤器為`cv2.TrackerTLD_create()`
-   MEDIANFLOW：速度中 精確度中 對於會跳動或快速移動的物件，判斷不是很準確。追蹤器為`cv2.TrackerMedianFlow_create()`
-   KCF：速度快 精確度高 不錯的追蹤器，但在物件被遮蔽的狀態下不是很準確。追蹤器為`cv2.TrackerKCF_create()`
-   MOSSE：速度最快 精確度高 速度最快，但精準度比 KCF 和 CSRT 稍差。追蹤器為`cv2.TrackerMOSSE_create()`
-   CSRT：速度快 最高 精準度比 KCF 好，但速度比 KCF 慢。追蹤器為`cv2.TrackerCSRT_create()`
