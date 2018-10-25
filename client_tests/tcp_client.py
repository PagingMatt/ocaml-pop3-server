#!/usr/bin/env python

# Simple TCP client used to test the server following guide at
# 'https://wiki.python.org/moin/TcpCommunication'.

import socket

# Connection details
conn = ('localhost', 110)
buffer_size = 1024

# Set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect
s.connect(conn)
greeting = s.recv(buffer_size)
print greeting

# Move through session
s.send("USER matt\r\n")
response = s.recv(buffer_size)
print response

s.send("PASS foo\r\n")
response = s.recv(buffer_size)
print response

s.send("QUIT\r\n")
response = s.recv(buffer_size)
print response

# Close connection after session is done
s.close()
print 'CLOSED'
