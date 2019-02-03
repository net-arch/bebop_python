import socket
import sys 
import termios
import tty

def send_to(t):
    if t == 0:
        print("send to all drones.")
        while True:
                command = sys.stdin.read(1)
                if command == "c":
                    break
                for s in sockets:
                    s.send(command.encode('utf-8'))
                if command == "q":
                    break
    elif t <= 3:
        print("send to drone %s" %target)
        while True:
            command = sys.stdin.read(1)
            if command == "c":
                break
            sockets[t-1].send(command.encode('utf-8'))
            if command == "q":
                break
    else:
        return



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
        print("select target(1~3). 0:all 9:end")
        target = sys.stdin.read(1) # 1文字読み込み
        if target.isdecimal(): # 入力が数字かどうか判定
            if int(target) == 9:
                print("end")
                command = "q"
                for s in sockets:
                    s.send(command.encode('utf-8'))
                break
            else:
                send_to(int(target))if target == 9:
            print("end")
            command = "q"
            for s in sockets:
                s.send(command.encode('utf-8'))
            break
        else:
            print("invalid literal!")

finally:  
    termios.tcsetattr(fd, termios.TCSANOW, old)

print("end") 
