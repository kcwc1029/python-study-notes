

# 個人理財網頁應用程式

這是一個使用 Flask 框架開發的個人理財網頁應用程式。其主要功能包括記錄現金和股票資產,並提供相關統計資訊,方便使用者管理個人財務狀況。

![upgit_20240502_1714588588.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240502_1714588588.png)
## 功能

-   現金資產管理
    -   記錄新台幣和美金現金餘額
    -   顯示總現金資產
    -   列出現金紀錄,可刪除特定紀錄
-   股票資產管理
    -   新增股票交易紀錄 (股票代號、股數、單價、手續費、交易稅等)
    -   顯示持有股票資產及其統計數據 (市值、資產佔比、購買總成本、平均成本、報酬率)
    -   提供股票資產佔比圖表視覺化

## 使用技術

-   Flask - Python 網頁框架
-   SQLite - 關聯式資料庫
-   Bootstrap - 前端樣式框架
-   Jinja2 - 模板引擎
-   全球即時匯率 API - 取得最新匯率資訊
-   Matplotlib - 繪製股票資產佔比圖表

## 執行

1. 初始化資料庫: 執行 `db_setting.py` (僅第一次執行需要)
3. 執行應用程式: `flask run`
4. 在瀏覽器中開啟 `http://localhost:5000`

## 檔案結構

```
專案目錄
├── index.py（Flask 應用程式主要程式碼）
├── datafile.db
├── static (靜態檔案目錄 (如圖片、CSS、JavaScript))
│   └── result.jpg
└── templates（HTML 模板目錄）
    ├── base.html
    ├── cash.html
    ├── index.html
    └── stock.html
```
