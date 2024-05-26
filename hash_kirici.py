import subprocess
from tkinter import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def hash_ogren():
    # Firefox tarayıcısını başlatmak için Selenium WebDriver'ı kullan
    driver = webdriver.Firefox()
    # GitHub sayfasına git
    url = "https://github.com/dogukantss00/hash_bulma"
    driver.get(url)

def hash_kirici():
    # Kullanıcı tarafından girilen hash algoritması, hash dosyası ve wordlist dosyası yollarını al
    hash_algorithm = ent3.get()
    hash_file = ent1.get()
    wordlist_file = ent2.get()
    try:
        # Hashcat komutunu çalıştır
        result = subprocess.run(
            ["hashcat", "-m", hash_algorithm, "-a", "0", "-o", "found.txt", hash_file, wordlist_file],
            capture_output=True, text=True, check=True
        )
        # Hashcat çıktısını metin kutusuna ekle
        output_text.insert(END, result.stdout)
    except subprocess.CalledProcessError as e:
        # Hata durumunda hata mesajını metin kutusuna ekle
        output_text.insert(END, f"Hata: {e.stderr}\n")

# Tkinter ana penceresini oluştur
pencere1 = Tk()
pencere1.title("Hash Kırma")
pencere1.geometry("750x400+400+0")

# Hash dosyası yolu için etiket ve giriş alanı oluştur
label1 = Label(pencere1, text="Hash dosyası yolu:")
label1.pack()
ent1 = Entry(pencere1, width=75)
ent1.pack()

# Wordlist dosyası yolu için etiket ve giriş alanı oluştur
label2 = Label(pencere1, text="Wordlist dosyası yolu:")
label2.pack()
ent2 = Entry(pencere1, width=75)
ent2.pack()

# Hash algoritması için etiket ve giriş alanı oluştur
label3 = Label(pencere1, text="Hash algoritması (Örn: 1400 - SHA256):")
label3.pack()
ent3 = Entry(pencere1)
ent3.pack()

# Hash kırma işlemini başlatmak için buton oluştur
buton1 = Button(pencere1, text="Hash Kırmak İçin Tıklayın", command=hash_kirici)
buton1.pack()

# Hashcat çıktısını göstermek için metin kutusu oluştur
output_text = Text(pencere1, height=10, width=100)
output_text.pack()

# Hash türünü öğrenmek için buton ve etiket oluştur
label4 = Label(pencere1, text="Hash türü öğrenmek için tıklayın")
label4.pack()
buto2 = Button(pencere1, text="Tıklayın", command=hash_ogren)
buto2.pack()

# Tkinter ana döngüsünü başlat
pencere1.mainloop()
