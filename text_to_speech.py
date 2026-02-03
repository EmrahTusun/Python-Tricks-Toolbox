import pyttsx3 #internet gerektirmeden çalışan seslendirme kütüphanesi.

engine = pyttsx3.init() #bilgisayarın ses moturunu başlatma

text = input("Sesli okunacak metni girin: ")

engine.say(text)# metni konuşmaya çevirme
engine.runAndWait() #sesli okuma burada başlar
