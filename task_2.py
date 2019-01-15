#!/usr/bin/env python3
import socket
from task_1 import crawler

HOST = '127.0.0.1'
PORT = 2999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, addr = s.accept()
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            website = str(str(data).split(' ')[0][2:])
            keyword = str(str(data).split(' ')[:-1])
            reply = crawler(website, keyword)
            print(reply)
            reply_encoded = reply.encode()
            connection.sendall(reply_encoded)