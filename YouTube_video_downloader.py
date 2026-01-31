from pytube import YouTube

url = input("Youtube video linkini giriniz: ") #kullanıcıdan video linkini alma

video = YouTube(url).streams.get_highest_resolution() #Bağlantıyı kurma ve en yüksek çözünürlüğü seçme

print(f"'{video.title}' indiriliyor...")
video.download()#İndirme 
print("Bitti!")