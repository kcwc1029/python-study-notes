from flask import Flask, render_template, request
import sqlite3
from flask import g
from flask import redirect 
import requests
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("agg")





DATABASE = './datafile.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()




# =============================================================================
# router
# =============================================================================


@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    # 取得目前現金資料庫資料
    cash_result = cursor.execute("SELECT * FROM cash")
    cash_result = cash_result.fetchall()
    # 計算台幣與美金總額
    NTD = 0
    US = 0
    for i in cash_result:
        NTD+=i[1]
        US+=i[2]
    # 全球即時匯率API
    r=requests.get('https://tw.rter.info/capi.php')
    currency=r.json()
    currency = currency["USDTWD"]["Exrate"] # 匯率
    total = math.floor(NTD+US*currency)

    # 取得目前股票資料庫資料
    stock_result = cursor.execute("SELECT * FROM stock")
    stock_result = stock_result.fetchall()
    # print(stock_result)

    # 取得所有股票代號
    unique_stock_list = []
    for i in stock_result:
        if i[1] not in unique_stock_list: unique_stock_list.append(i[1])

    # 計算股票總市值
    total_stock_value = 0
    # 計算單一股票資訊
    stock_info = []
    for i in unique_stock_list:
        result = cursor.execute("SELECT * FROM stock WHERE stock_id = ?", (i,))
        result = result.fetchall()
        stock_cost = 0 # 計算單一股票總花費
        shares = 0 # 單一股票股數
        for j in result: # 查詢單個股票之所有資訊
            shares += j[2]
            stock_cost += j[2] * j[3] + j[4] + j[5]
        # 取得目前股價
        url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo="+i
        response = requests.get(url)
        data=response.json()
        # print(data)
        price_list = data["data"]
        current_price = float(price_list[-1][6]) # 股價
        # 單一股票總市值 
        total_stock_value += int((current_price * shares))
        # 單一股票平均成本
        average_cost = round(stock_cost/shares, 2)
        # 單一股票報酬率 
        rate_of_return = round((int((current_price * shares)) - stock_cost)*100 / stock_cost, 2)
        stock_info.append({"stock_id":i, "stock_cost":stock_cost, "total_value":int((current_price * shares)), "average_cost":average_cost, "shares":shares, "current_price":current_price, "rate_of_return":rate_of_return})

    for i in stock_info:
        i["value_precentage"] = round(i["total_value"]*100/total_stock_value,2)

    # 股票圓餅圖
    if len(unique_stock_list)!=0:
        labels = tuple(unique_stock_list)
        sizes = [x["total_value"] for x in stock_info]
        # fig, ax = plt.subplots(figsize=(6,5))
        # ax.pie(sizes,labels=labels, autopct=None, shadow=None)
        # fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        # plt.savefig("./static/result.jpg")
        # 创建图形和子图
        plt.subplots(figsize=(3,2))
        plt.pie(sizes, labels=labels, textprops={'size':6}) # 绘制饼图
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.savefig("./static/result.jpg", dpi=200) # 保存图形




    # 傳回數值給index.html
    data = {"NTD":NTD, "US":US,"currency":currency,"total":total, "cash_result":cash_result,
            "stock_info":stock_info}
    return render_template("index.html", data=data)

@app.route('/cash')
def cash_form():
    return render_template("cash.html")

@app.route('/cash', methods=["POST"])
def submit_cash():
    print(request.values)
    # 取得資料
    NTD = 0
    US = 0
    note = 0
    date = ""
    if request.values["NTD"]!= "": NTD = request.values["NTD"]
    if request.values["US"]!= "": US = request.values["US"]
    if request.values["note"]!= "": note = request.values["note"]
    if request.values["date"]!= "": date = request.values["date"]
    # 更新資料
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cash (taiwanese_dollars, us_dollars, note, date_info) VALUES (?, ?, ?, ?)", (NTD, US, note, date))
    conn.commit()

    # 導回頁面
    return redirect("/")

@app.route("/cash_delete", methods=["POST"])
def cash_delete():
    id = request.values["id"]
    print(id)
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cash WHERE transaction_id = ?", (id,))
    conn.commit()
    return redirect("/")


# =============================================================================
# 股票相關route
# =============================================================================


@app.route('/stock')
def stock_form():
    return render_template("stock.html")

@app.route('/stock', methods=["POST"])
def submit_stock():
    print(request.values)
    # 取得資料
    stock_id = 0
    stock_num = 0
    stock_price = 0
    processing_fee = 0
    tax = 0
    date = ""
    if request.values["stock-id"]!= "": stock_id = request.values["stock-id"]
    if request.values["stock-num"]!= "": stock_num = request.values["stock-num"]
    if request.values["stock-price"]!= "": stock_price = request.values["stock-price"]
    if request.values["processing-fee"]!= "": processing_fee = request.values["processing-fee"]
    if request.values["tax"]!= "": tax = request.values["tax"]
    if request.values["date"]!= "": date = request.values["date"]
    print(stock_id, stock_num, stock_price, processing_fee, tax, date)
    # 更新資料
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stock (stock_id, stock_num, stock_price, processing_fee, tax, date_info) VALUES (?, ?, ?, ?, ?, ?)", 
                   (stock_id, stock_num, stock_price, processing_fee, tax, date))
    conn.commit()

    # 導回頁面
    return redirect("/")
    
# =============================================================================
# 單獨清空每一個資料表
# =============================================================================
@app.route('/test')
def delete():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM stock")
    conn.commit()
    conn.close()
    return " 已清除"


if __name__ == "__main__":
    app.run(debug=True)