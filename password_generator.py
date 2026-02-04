import random
harf = "qwertyuıopğüasdfghjklşizxcvbnmöç"
Harf = harf.upper()
sayi = "0123456789"
sembol = "_?=)(/&%+^'!|][{$#"

toplam = harf+Harf+sayi+sembol
uzunluk=int(input("şifre uzunluğunu giriniz:"))
sifre = random.choices(toplam , k=uzunluk)
sifre = "".join(sifre)

print(sifre)