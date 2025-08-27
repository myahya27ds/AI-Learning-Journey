# 📝 Text Analysis Tool

Sebuah program **Python** sederhana untuk melakukan analisis teks baik dalam bahasa **Inggris** maupun **Indonesia**.  
Fitur ini cocok untuk latihan **Natural Language Processing (NLP)** dasar, misalnya menghitung jumlah karakter, kata, vokal, konsonan, serta menampilkan kata yang paling sering muncul.  

---

## ✨ Fitur Utama
- 🧹 **Pembersihan teks** (lowercase + hapus tanda baca)  
- 🔤 **Hitung karakter** (dengan & tanpa spasi)  
- 📊 **Hitung jumlah kata**  
- 🛑 **Opsi mengabaikan stopwords** (Inggris / Indonesia)  
- 🔎 **Hitung jumlah vokal dan konsonan**  
- 📈 **Menampilkan Top-N kata yang paling sering muncul**  
- 💾 **Menyimpan hasil analisis ke file `.txt`**

---

## 🚀 Cara Menjalankan Program

1. **Clone repository**
   ```bash
   git clone https://github.com/username/text-analysis-tool.git
   cd text-analysis-tool

2. **Jalankan program**
   ```bash
   python main.py

3. Ikuti instruksi di menu program
   - Input teks manual atau dari file
   - Pilih bahasa (English/Indonesian)
   - Pilih apakah mau mengabaikan stopwords atau tidak
   - Lihat hasil analisis langsung di terminal

# 📂 Project Structure
   ```bash
   text-analysis-tool/
   │── main.py        # Program utama analisis teks
   │── README.md      # Dokumentasi project (Bahasa Inggris)
   │── README_ID.md   # Dokumentasi project (Bahasa Indonesia)
   ```

# 📸 Contoh Output
   ```bash
   --- Analysis Results ---
   Total Characters: 120
   Characters without spaces: 98
   Total Word Count: 20
   Vowel Count: 45
   Consonant Count: 53

   Top 5 Most Frequent Words:
   - data: 4
   - python: 3
   - text: 2
   - analysis: 2
   - simple: 1
   ```

# 🎯 Tujuan Project
Project ini dibuat sebagai latihan:
- Pemrosesan teks sederhana (basic NLP)
- Manipulasi string di Python
- Menerapkan struktur program dengan fungsi-fungsi modular
- Membiasakan workflow push project ke GitHub sebagai portofolio

# 📜 License
Project ini bebas digunakan untuk pembelajaran 🚀
