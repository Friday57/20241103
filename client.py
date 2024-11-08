import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))  # 连接到服务器
data = s.recv(1024)  # 接收数据，最多接收 1024 字节
print("服务器回复：", data.decode("utf-8"))  # 解码并打印接收到的数据
s.close()  # 关闭连接