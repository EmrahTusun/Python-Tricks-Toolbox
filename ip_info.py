import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Bilgisayar adı:", hostname)
print("IP adresi:", ip)
