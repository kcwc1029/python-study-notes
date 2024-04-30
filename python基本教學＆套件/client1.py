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
