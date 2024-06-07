 ## ip 地址的分类

![upgit_20240421_1713641894.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/04/upgit_20240421_1713641894.png)

### @ A 類 IP 地址

一個 A 類 IP 地址由 1 字節的網絡地址和 3 字節主機地址組成，網絡地址的最高位必須是“0”，

地址範圍 1.0.0.1-126.255.255.254

二進制表示為：00000001 00000000 00000000 00000001 - 01111110 11111111 11111111 11111110

可用的 A 類網絡有 126 個，每個網絡能容納 1677214 個主機

### @ B 類 IP 地址

一個 B 類 IP 地址由 2 個字節的網絡地址和 2 個字節的主機地址組成，網絡地址的最高位必須是“10”，

地址範圍 128.1.0.1-191.255.255.254

二進制表示為：10000000 00000001 00000000 00000001 - 10111111 11111111 11111111 11111110

可用的 B 類網絡有 16384 個，每個網絡能容納 65534 主機

### @ C 類 IP 地址

一個 C 類 IP 地址由 3 字節的網絡地址和 1 字節的主機地址組成，網絡地址的最高位必須是“110”

範圍 192.0.1.1-223.255.255.254

二進制表示為: 11000000 00000000 00000001 00000001 - 11011111 11111111 11111110 11111110

C 類網絡可達 2097152 個，每個網絡能容納 254 個主機

### @ D 類地址用於多點廣播

D 類 IP 地址第一個字節以“1110”開始，它是一個專門保留的地址。

它並不指向特定的網絡，目前這一類地址被用在多點廣播（Multicast）中

多點廣播地址用來一次尋址一組計算機 s 地址範圍 224.0.0.1-239.255.255.254

### @ E 類 IP 地址

以“1111”開始，為將來使用保留

E 類地址保留，僅作實驗和開發用

### @ 私有 ip

在這麽多網絡 IP 中，國際規定有一部分 IP 地址是用於我們的局域網使用，也就

是屬於私網 IP，不在公網中使用的，它們的範圍是：

10.0.0.0 ～ 10.255.255.255

172.16.0.0 ～ 172.31.255.255

192.168.0.0 ～ 192.168.255.255

### @ 注意

IP 地址 127．0．0．1~127．255．255．255 用於回路測試，

如：127.0.0.1 可以代表本機 IP 地址，用http://127.0.0.1就可以測試本機中配置的Web服務器。

## 查看或配置网卡信息：ifconfig

＄ 我们只是敲：ifconfig，它会显示所有网卡的信息。

## 測試遠端主機連通性：ping

＄通常用 ping 来检测网络是否正常

## 端口

-   80 端口分配给 HTTP 服务
-   21 端口分配给 FTP 服务

## 不同電腦上的進程之間如何通信

＄ TCP/IP 協議族已經幫我們解決了這個問題，網絡層的“ip 地址”可以唯一標識網絡中的主機，而傳輸層的“協議+端口”可以唯一標識主機中的應用進程（進程）。

## 什麼是 Socket

＄ Socket 是計算機網路中實現程序之間通信的一種機制,是軟件構件之間溝通的基礎。Socket 允許運行在不同主機上的程序進行通信,換句話說,它們是網路通信的基礎 API。

＄ Socket 工作在 TCP/IP 協議之上。

＄ 指定 ip、port（區分要送到哪一個應用上）

> [!NOTE] 教學影片
> [(1013) TCP/IP 网络通信之 Socket 编程入门 - YouTube](https://www.youtube.com/watch?v=ST6WLZFSHXs)
> （裡面就有教使用 socket 庫程式碼）

## TCP & UDP 概述

＄ TCP & UDP 統整

-   TCP：穩定可靠。可用於傳輸文件、發送郵件、瀏覽網頁
-   UDP：速度快，但可能丟包。可用於域名查詢、語音通話、視屏直撥、隧道網路（VPN）
    ＄ TCP & UDP 接工作在傳輸層，主要任務為「在程序中傳輸數據」如文件、影片、圖片。

## UDP 協議

＄ 基於非連接的（就是將數據包一下，就從網卡丟出去了）

-   性能損耗少
-   cpu 資源沾用少
-   穩定性弱
    ＄ 可以把它想成「寫信」

## TCP 協議

＄ TCP 協議，傳輸控制協議（英語：Transmission Control Protocol，縮寫為 TCP）是一種面向連接的、可靠的、基於字節流的傳輸層通信協議，由 IETF 的 RFC 793 定義。

＄ 可以把它想成「接電話 」，從電話接通、互相通話、結束掛斷這三項都可以得到及時反饋。

### @ 三次握手（開始）

![upgit_20240422_1713716548.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/04/upgit_20240422_1713716548.png)

＄ 如果用兩次握手會發生什麼事

-   客戶端第一次發送 syn 給伺服器 -> 假設因為某些原因滯留。
-   客戶端第二次發送 syn 給伺服器 -> 這次成功發送 -> 伺服器回覆 syn+ack -> 建立連接
-   但這時第一次發送的 syn 抵達到伺服器 -> 伺服器會以為這是客戶發送的新連接 -> 回覆 syn+ack -> 建立連接
-   此時，客戶開一個連接，但伺服器卻開了兩個連接。

### @ 傳輸確認

＄ 會有丟包問題、亂序問題（包前後到達順序不同）
![upgit_20240422_1713716523.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/04/upgit_20240422_1713716523.png)

### @ 四次揮手（結束）

＄ 客戶跟伺服器都可以請求關閉連接。
![upgit_20240422_1713716689.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/04/upgit_20240422_1713716689.png)

＄ 為什麼需要等待到超時時間（第四次揮手）：是為了防止最後的 ack 丟失。若 ack 丟失，伺服器將處於最後確認狀態（last-ack）

### @ tcp 長連接和短連接

＄ TCP 短連接：短連接一般只會在 client/server 間傳遞一次讀寫操作！

-   client 向 server 發起連接請求
-   server 接到請求，雙方建立連接
-   client 向 server 發送消息
-   server 回應 client
-   一次讀寫完成，此時雙方任何一個都可以發起 close 操作（一般都是 client 先發起 close 操作）。
-   範例：WEB 網站的 http 服務一般都用短鏈接，因為長連接對於服務端來說會耗費一定的資源

＄ TCP 長連接：

-   client 向 server 發起連接
-   server 接到請求，雙方建立連接
-   client 向 server 發送消息
-   server 回應 client
-   一次讀寫完成，連接不關閉
-   後續讀寫操作...
-   長時間操作之後 client 發起關閉請求
-   長連接可以省去較多的 TCP 建立和關閉的操作，減少浪費，節約時間。
-   隨著客戶端連接越來越多，server 早晚有扛不住的時候，這時候 server 端需要采取一些策略，如關閉一些長時間沒有讀寫事件發生的連接，或是以客戶端機器為顆粒度，限制每個客戶端的最大長連接數。
-   範例：數據庫的連接用長連接，如果用短連接頻繁的通信會造成 socket 錯誤。

## 使用 socket 做 UDP 通訊

```python
# 使用UDP server端
import socket

# 創建一個 UDP 套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 獲取本地主機名稱和端口
host = '127.0.0.1'
port = 8080

# 綁定地址和端口
server_socket.bind((host, port))

# 進入無限迴圈，等待客戶端發送消息
while True:
    try:
        print("等待客戶端發送消息...")
        # 接收客戶端的消息
        data, addr = server_socket.recvfrom(1024)
        print("收到的消息:", data.decode())
        print("客戶端地址:", addr)
    except KeyboardInterrupt:
        # 使用者按下 Ctrl+C，退出迴圈
        break
    except Exception as e:
        # 處理其他異常
        print("發生異常:", e)

# 關閉套接字
server_socket.close()

```

```python
# 使用UDP client端
import socket

# 創建一個 UDP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 獲取本地主機名稱和端口
host = '127.0.0.1'
port = 8080

# 發送消息給服務器
message = "Hello, server!"
client_socket.sendto(message.encode(), (host, port))


# 關閉套接字
client_socket.close()

```

## 使用 socket 做 TCP 通訊(Server 同時間只能服務一個 Client)

```python
# 使用TCP server端
import socket

# 創建一個 TCP 套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 獲取本地主機名稱和端口
host = '127.0.0.1'
port = 8080

# 綁定地址和端口
server_socket.bind((host, port))

# 進入無限迴圈，等待客戶端發送消息
while True:
    try:
        print("等待客戶端發送消息...")
        # 接收客戶端的消息
        data, addr = server_socket.recvfrom(1024)
        print("收到的消息:", data.decode())
        print("客戶端地址:", addr)
    except KeyboardInterrupt:
        # 使用者按下 Ctrl+C，退出迴圈
        break
    except Exception as e:
        # 處理其他異常
        print("發生異常:", e)

# 關閉套接字
server_socket.close()

```

```python
# 使用TCP client端
import socket

# 創建一個 TCP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 獲取服務器的主機名稱和端口
host = '127.0.0.1'
port = 8080

# 連接到服務器
client_socket.connect((host, port))

# 發送消息給服務器
message = "i am client1"
client_socket.send(message.encode())

# 接收服務器的回覆
response = client_socket.recv(1024)
print("服務器的回覆:", response.decode())

# 關閉套接字
client_socket.close()

```

## 使用 socket 做 TCP 通訊(Server 同時間服務多個 Client)

```python
import socket
import threading

# server.py
def handle_client(client_socket, client_id):
    while True:
        try:
            # 接收客户端消息
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"client {client_id} send message: {data.decode()}")
            # 回复客户端
            client_socket.sendall(b"Message received")
        except Exception as e:
            print(f"client {client_id} error: {e}")
            break
    # 关闭客户端套接字
    client_socket.close()

# 创建 TCP 套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名和端口
host = '127.0.0.1'
port = 8080

# 绑定地址和端口
server_socket.bind((host, port))

# 设置最大等待连接数
server_socket.listen(5)
print("waiting for connection...")

client_id = 1

while True:
    try:
        # 接受客户端连接
        client_socket, addr = server_socket.accept()
        print(f"add connection from {addr}")
        # 创建一个线程处理客户端请求
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_id))
        client_thread.start()
        client_id += 1
    except KeyboardInterrupt:
        # 用户按下 Ctrl+C，退出循环
        break
    except Exception as e:
        print("ERROR:", e)

# 关闭套接字
server_socket.close()

```

```python
# client1.py
import socket

# 创建 TCP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取服务器的主机名和端口
host = '127.0.0.1'
port = 8080

# 连接到服务器
client_socket.connect((host, port))

# 发送消息给服务器
message = "Hello, server from client 1!"
client_socket.send(message.encode())

# 接收服务器的回复
response = client_socket.recv(1024)
print("服务器的回复:", response.decode())

# 关闭套接字
client_socket.close()

```

```python
# client2.py

import socket

# 创建 TCP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取服务器的主机名和端口
host = '127.0.0.1'
port = 8080

# 连接到服务器
client_socket.connect((host, port))

# 发送消息给服务器
message = "Hello, server from client 2!"
client_socket.send(message.encode())

# 接收服务器的回复
response = client_socket.recv(1024)
print("服务器的回复:", response.decode())

# 关闭套接字
client_socket.close()

```
