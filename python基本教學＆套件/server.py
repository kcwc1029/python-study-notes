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
