import qrcode
data = input("QR koda dönüştürülecek linki veya metni girin: ")#1. QR koda dönüştürülecek veri (Link veya Metin)

qr = qrcode.QRCode(version=1, box_size=10, border=5)#2. QR kod ayarları
qr.add_data(data)
qr.make(fit=True)

color =input("QR kodunuz hangi renkte olsun.[ ör: blue ]  :")
img = qr.make_image(fill_color=color, back_color="white")#3. Görseli oluştur ve kaydet
filename = input("lütfen QR kod adı giriniz: ") + ".png"
img.save(filename)

print(f"QR kodunuz '{filename}' adıyla kaydedildi.")