#!/usr/bin/env python3
import socket
from task_1 import crawler
"""
    We create a socket program to run the crawler from task_1.
    
    To create a system service copy the task_2.service in 
    /etc/systemd/system/task_2.service
    adapt the correct paths in it and then run
    
    systemctl daemon-reload && systemctl enable task_2 && systemctl start task_2 --no-block

    Test-run it with the task_2_client.py
"""

HOST = 'ws://localhost:8000/temperature'
PORT = 6379

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, addr = s.accept()
    with connection:
        while True:

            # We receive the requested website and keyword and store them in data
            data = connection.recv(1024)
            if not data:
                break
            website = str(str(data).split(' ')[0][2:])
            keyword = str(str(data).split(' ')[:-1])
            reply = crawler(website, keyword)
            reply_encoded = reply.encode()

            # Send the crawled data back
            connection.sendall(reply_encoded)