import os
aranacak_dosya_uzantisi = input("Dosya Uzantısını giriniz:")

aranan_dosya = []

for root, dirs, files in os.walk("C:/"):  
    for file in files:
        if file.lower().endswith(aranacak_dosya_uzantisi):
            aranan_dosya.append(os.path.join(root,file))

with open("aranan_dosyalar.txt", "w", encoding="utf-8") as aranan_file:
    for aranan_dos in aranan_dosya:
        aranan_file.write(aranan_dos + "\n")

print("Dosyalar başarıyla kaydedildi!")
