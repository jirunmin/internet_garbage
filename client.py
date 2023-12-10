import socket
import time

server_host = '127.0.0.1'
server_port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_host, server_port))

l = 1
r = 10000

while l <= r:
    mid = l + r >> 1

    time.sleep(1)
    print("I guess", mid)

    s.send(str(mid).encode())
    data = s.recv(1024)
    if data:
        result = data.decode()
        if result == "correct":
            break
        elif result == "large":
            r = mid - 1
        else:
            l = mid + 1

