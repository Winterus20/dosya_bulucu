import os

mp4_files = []
txt_files = []
pdf_files = []

for root, dirs, files in os.walk("C:/"):  
    for file in files:
        if file.lower().endswith(".mp4"):
            mp4_files.append(os.path.join(root))
        elif file.lower().endswith(".txt"):
            txt_files.append(os.path.join(root))
        elif file.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(root))

with open("mp4_dosyalari.txt", "w", encoding="utf-8") as mp4_file:
    for mp4 in mp4_files:
        mp4_file.write(mp4 + "\n")

with open("txt_dosyalari.txt", "w", encoding="utf-8") as txt_file:
    for txt in txt_files:
        txt_file.write(txt + "\n")

with open("pdf_dosyalari.txt", "w", encoding="utf-8") as pdf_file:
    for pdf in pdf_files:
        pdf_file.write(pdf + "\n")

print("Dosyalar başarıyla kaydedildi!")
