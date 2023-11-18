import socket

def get_banner(ip, port):
    sock = socket.socket()
    sock.settimeout(10)

    try:
        sock.connect((ip, port))
        sock.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
        banner = sock.recv(1024)
    except Exception as e:
        return f"연결 오류: {str(e)}"
    finally:
        sock.close()

    return banner.decode().strip()

ip = input("분석할 IP를 입력해주세요: ")
print("SSH(22포트):", get_banner(ip, 22))
print("HTTP(80포트):", get_banner(ip, 80))
print("HTTPS(443포트):", get_banner(ip, 443))
