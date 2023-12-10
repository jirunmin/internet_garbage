import socket
import time
import threading
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))

s.listen(5)
# print('Waiting for connection...')
x = random.randint(1, 10000)

def tcplink(sock, addr):
    print("Please guess a number, which ranges from 1 to 10000.")
    cnt = 0
    # print('Accept new connection from %s:%s...' % addr)
    # sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data:
            break

        number = int(data.decode())
        result = None
        cnt += 1

        if number == x:
            result = "correct"
        elif number > x:
            result = "large"
        else:
            result = "small"

        time.sleep(1)
        print("The number", number, "is", result)
        if result == "correct":
            print("You guess", cnt ,"time(s)")

        sock.send(result.encode())
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    # print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()