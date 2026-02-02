import qrcode
data = input("QR koda dönüştürülecek linki veya metni girin: ")#1. QR koda dönüştürülecek veri (Link veya Metin)

qr = qrcode.QRCode(version=1, box_size=10, border=5)#2. QR kod ayarları
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")#3. Görseli oluştur ve kaydet
filename = "my_qrcode.png"
img.save(filename)

print(f"QR kodunuz '{filename}' adıyla kaydedildi.")