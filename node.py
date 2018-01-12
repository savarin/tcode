import socket


UDP_IP = ''
UDP_PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

while True:
    try:
        s.settimeout(10)
        data, addr = s.recvfrom(1024)
        print data
        print addr
    except socket.timeout:
        print '.'

