## KCF 演算法

![upgit_20240514_1715623605.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240514_1715623605.png)

-   相關文獻：https://arxiv.org/abs/1801.06729
-   在快速影片中表現不佳，會有丟失物品之困境

## CSRT 演算法

![upgit_20240514_1715624043.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240514_1715624043.png)

-   相關文獻：https://ar5iv.labs.arxiv.org/html/1611.08461

-   從左到右：使用 Sklearn 對包含物體邊界框的訓練補丁（training patch）進行訓練。
-   使用 HOG 提取圖像的有用信息
-   應用 Random Markov Test 生成概率，這可能是指將隨機馬爾可夫測試應用於生成概率。（隨機馬爾可夫測試（Random Markov Test）可能用於生成與 HOG 演算法相關的概率信息，幫助更好地理解數據或模型的行為）。
-   訓練補丁，使用信心圖（confidence map）進行遮罩，可能有助於提高模型的準確性或穩定性。
