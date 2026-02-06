import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"Bilgisayar Adı : {hostname}")
print(f"Yerel IP Adresi: {ip}")