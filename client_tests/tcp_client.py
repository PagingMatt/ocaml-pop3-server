#!/usr/bin/env python

# Simple TCP client used to test the server following guide at
# 'https://wiki.python.org/moin/TcpCommunication'.

import socket

# Connection details
conn = ('localhost', 110)
bufer_size = 1024

# Set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect
s.connect(conn)
greeting = s.recv(buf)

# Move through session
print greeting
s.send("USER matt")
response = s.recv(buf)
print response

# Close connection after session is done
s.close()
print 'CLOSED'