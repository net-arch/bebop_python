import socket
import sys 
import termios
import tty

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)

sockets = []

hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
port = 8080

for h in hosts:
    sock = socket.socket()
    sock.connect((h, port))
    sockets.append(sock)


try:
    tty.setcbreak(sys.stdin.fileno())
    while True:
        ch = sys.stdin.read(1)
        for s in sockets:
            s.send(ch.encode('utf-8'))
        if ch == "q":
            break

finally:  
    termios.tcsetattr(fd, termios.TCSANOW, old)

print("end") 
