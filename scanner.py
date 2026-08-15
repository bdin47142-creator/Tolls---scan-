import socket

host = input("Enter IP address: ")
print(f"Scanning {host}...\n")

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((host, port)) == 0:
        print(f"[+] Port {port} is OPEN")
    sock.close()
