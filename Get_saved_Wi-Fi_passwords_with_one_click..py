import subprocess

def wifi_sifrelerini_getir():
    datalar = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiller = [i.split(":")[1][1:-1] for i in datalar if "All User Profile" in i]

    print("\n   KAYITLI WIFI ŞİFRELERİ   \n")
    for isim in profiller:
        sonuclar = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', isim, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        sifre = [b.split(":")[1][1:-1] for b in sonuclar if "Key Content" in b]
        
        try:
            print(f"Ağ Adı: {isim:<20} | Şifre: {sifre[0]}")
        except IndexError:
            print(f"Ağ Adı: {isim:<20} | Şifre: [ŞİFRE BULUNAMADI]")

    input("\nKapatmak için Enter'a bas...")

wifi_sifrelerini_getir()