## SMTP

SMTP 是簡單郵件傳輸協議(Simple Mail Transfer Protocol)的縮寫,是一種用於在網路上傳輸電子郵件的標準協議。它定義了電子郵件客戶端如何與郵件伺服器進行通信,以及不同郵件伺服器之間相互傳遞郵件的規則和流程。

SMTP 的主要作用包括:

1. 傳送電子郵件
2. 驗證發件人身份
3. 根據收件地址路由郵件
4. 管理郵件傳輸佇列

SMTP 是基於 TCP 協議工作,預設使用 25 號端口。發送郵件時,客戶端先連線到 SMTP 伺服器,伺服器再根據收件位址將郵件轉發給目標 SMTP 伺服器,最終由收件人收取。這種協議方式實現了全球電子郵件的無縫傳輸。

在 python 中，提供了 smtplib，他定義了 SMTP client seesion objject 去寄送 mail。

每一個大型 email 都有自己的 SMTP server:

> gmail：smtp.gmail.com
> microsoft：smtp.live.com

另外，因為 python 無法處理 google 的兩步驗證。因此 google 提供 ==app password== 去創造另一個密碼讓裝置可以 [access google account](https://support.google.com/accounts/answer/185833?hl=zh-Hant)

## 寄送 gmail

```python
===== 寄送gmail =====

import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class CFG:
    # 應用程式密碼
    app_password = "ancvaiccxmaixspe"
    # 寄件者
    sender = "3331363@gmail.com"
    # 收件者
    recipient = "10911221@gm.nttu.edu.tw"
    # 信件主旨
    title = "【來自幸運小狗的來信】"
    # 信件內容
    body = """
        <p>如果你收到這封信，你這一天將受到幸運小狗的照顧。</p>
        <p><img src="cid:image"></p>
    """

def main():
    # 创建 SMTP 对象，连接到 Gmail 的 SMTP 服务器，参数 "smtp.gmail.com" 是 Gmail 的 SMTP 服务器地址，端口号为 587
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    # EHLO 指令用于与 SMTP 服务器建立连接
    smtp_obj.ehlo()
    # 启动 TLS（传输层安全）加密连接
    smtp_obj.starttls()

    # TAG: tag1
    # 登入
    smtp_obj.login(CFG.sender,CFG.app_password)
    '''
    這邊可以嘗試輸出，
    print(smtp_obj.login("3331363@gmail.com","ancvaiccxmaixspe"))
    如果輸出(235, b'2.7.0 Accepted')，代表登入成功。
    但要注意smtp_obj.login("3331363@gmail.com","ancvaiccxmaixspe")只能出現一次，如果出現兩次，便變成503失敗
    '''


    # NOTE: 寄信
    # 創建 MIMEText 物件。
    # 這邊要釐清：寄送信件跟信件的MIMEText是兩個格式

    # 创建 MIMEMultipart 对象
    msg = MIMEMultipart()
    msg['Subject'] = CFG.title
    msg['From'] = CFG.sender
    msg['To'] = CFG.recipient

    # 添加 HTML 邮件内容
    body = MIMEText(CFG.body, 'html')
    msg.attach(body)

    # 读取本地图片文件
    with open('./dog.jpg', 'rb') as f:
        img = MIMEImage(f.read())
    img.add_header('Content-ID', '<image>')
    img.add_header('Content-Disposition', 'inline', filename='dog.jpg')
    msg.attach(img)

    # smtp_obj.sendmail(CFG.sender, CFG.recipient, msg.as_string())
    status = smtp_obj.sendmail(CFG.sender, CFG.recipient, msg.as_string())
    if status == {}: print('郵件傳送成功！')
    else: print('郵件傳送失敗...')
    smtp_obj.quit()


if __name__ == '__main__':
    recipient = input("幸運小狗寄件信箱：")
    CFG.recipient = recipient
    main()
```

> [!NOTE] tag1
> Contents
> 這邊為了示範，採用直接寫的方式：
> smtp_obj.login("3331363@gmail.com","ancvaiccxmaixspe")
> 那正常來說，會將帳密輸入改為，讓使用者在輸入端（終端）輸入帳密：
> user_name = input("請輸入帳號")
> password = getpass.getpass(input("請輸入密碼")) （import getpass）
> smtp_obj.login(user_name,password)

## 接收 gmail（imap）

imap：支持用戶在不用將信件下載，就可以直接操作
SSL（secure socket layer）：是一種加密協議，用於在互聯網上安全地傳輸數據。SSL 協議的主要目的是保護通信雙方之間的數據傳輸安全性和隱私性。

**criterion（找信的條件）**
在使用 IMAP 协议查找电子邮件时，您可以使用一系列条件来筛选符合特定要求的邮件。以下是一些常见的 IMAP 搜索条件：

1. **FROM**：发送者的邮箱地址。
2. **TO**：接收者的邮箱地址。
3. **SUBJECT**：邮件主题中包含特定关键词的邮件。
4. **BODY**：邮件正文中包含特定关键词的邮件。
5. **SENTSINCE**：发送日期在指定日期之后的邮件。
6. **SENTBEFORE**：发送日期在指定日期之前的邮件。
7. **UNSEEN**：未读的邮件。
8. **FLAGGED**：已标记为重要的邮件。
9. **ANSWERED**：已回复的邮件。
10. **DELETED**：已删除的邮件。
11. **SIZE**：邮件大小满足指定条件的邮件。

主要會使用到以下幾個函數：

-   M.list()：回傳 tuple（相關資訊），inbox 收件夾、trash can、draft 草稿
-   M.select(str)：從 M.list()選取目標資料夾
-   M.search(None, criterion（找信的條件）)：選取信件
-   M.fetch(id, "(RFC822)") 拿內容。RFC822 指的是我拿這封信件的 header 跟 message bady

```python
===== DOC: 接收gmail =====

import imaplib
import email # 使用imaplib巴下來的東西是以base64編碼的二進位資料，要解碼

class CFG:
    # 應用程式密碼
    app_password = "ancvaiccxmaixspe"
    # 寄件者
    gmail = "3331363@gmail.com"
    # 找信條件 imap criterion
    criterion = "FROM ypliang@cs.ccu.edu.tw"

def main():
    M = imaplib.IMAP4_SSL("imap.gmail.com")
    M.login(CFG.gmail, CFG.app_password)

    # NOTE: 顯示INBOX，Unwanted，Important 各種信件夾資料
    # print(M.list())
    M.select("INBOX") # 選擇收件夾

    # NOTE: 通過搜CFG給的搜尋條件，去尋找目標信件
    result, ids = M.search(None, CFG.criterion)


    if ids:
        # 經過搜尋，確定至少有一筆結果
        myString = ids[0].decode("utf-8") # 先將ids[0]做decode，從bytes變成string
        # print(myString) # 26411 26427 26430 26480 26533 26534 26675 26835 27158（每一個id都是 一封信）
        myEmailList = myString.split(" ") # 將string內部的數字分開

        # NOTE:  看你選擇哪一封信來做解析
        #這裡的index是可以改的，rest信件狀態，rest, content信件內容
        rest, content  = M.fetch(myEmailList[1], "(RFC822)")

        print(len(content)) # ２
        print(content[0]) # 主要內容
        print(content[1]) # 沒東西
        print(type(content[0])) # tuple
        print(content[0][0]) # email id
        print(content[0][1]) # content (binary)

        # NOTE:所以接下來就是要拿content[0][1]來解析
        # 創建郵件實例
        msg = email.message_from_bytes(content[0][1])
        for part in msg.walk():
            # print(part)
            content_type = part.get_content_type()
            # 根據不同類型處理
            if content_type == "text/plain":
                body = part.get_payload(decode=True)
                print(body.decode())
                print("----------")

                # NOTE: 內容寫進txt
                with open("./email_context.txt", mode="wb") as f:
                    f.write(body)
    else:
        print("未找到满足条件的邮件")

if __name__ == '__main__':
    main()



```
