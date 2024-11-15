import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.bind((host, port))  # 绑定端口
s.listen(5)  # 等待客户端连接

print(f"服务器在 {host}:{port} 上等待连接...")

while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    message = '欢迎访问菜鸟教程！'.encode("utf-8")
    c.sendall(message)  # 使用 sendall 确保发送完整消息
    c.close()  # 关闭连接