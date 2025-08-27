# 🔢 Perfect Scientific Calculator (Python CLI)

Sebuah **scientific calculator berbasis CLI (Command Line Interface)** yang mendukung operasi matematika dasar, trigonometri, logaritma, hingga evaluasi ekspresi otomatis.  
Calculator ini juga memiliki fitur **riwayat perhitungan (history)** yang bisa disimpan dan dihapus sesuai kebutuhan.

---

## ✨ Fitur
- ✅ Operasi Aritmatika: Penjumlahan, Pengurangan, Perkalian, Pembagian, Modulus, Pangkat  
- ✅ Operasi Khusus: Akar kuadrat, Logaritma (basis 10)  
- ✅ Fungsi Trigonometri: Sin, Cos, Tan (pilihan **radian** atau **derajat**)  
- ✅ Kalkulasi otomatis dengan ekspresi (contoh: `sqrt(16) + sin(pi/2)`)  
- ✅ Riwayat perhitungan tersimpan di file `history.txt`  
- ✅ Menu interaktif dengan opsi untuk melihat dan menghapus riwayat  

---

## 📂 Struktur Project
```
.
├── calculator.py     # Script utama
├── history.txt       # Riwayat perhitungan (akan dibuat otomatis)
└── README.md         # Dokumentasi
```

---

## ▶️ Cara Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/myahya27ds/AI-Learning-Journey/tree/6869458dcc4f8a0318ddc1930ae3ff0f9986c019/mini-projects/perfect-scientific-calculator
   cd perfect-scientific-calculator
   ```

2. Jalankan program dengan Python:
   ```bash
   python main.py
   ```

---

## 📖 Menu Utama
| No | Menu                   | Deskripsi |
|----|------------------------|-----------|
| 1  | Automatic Calculation  | Evaluasi ekspresi langsung (contoh: `sqrt(25) + log(100)`) |
| 2  | Addition               | Penjumlahan |
| 3  | Subtraction            | Pengurangan |
| 4  | Multiplication         | Perkalian |
| 5  | Division               | Pembagian |
| 6  | Exponentiation         | Pangkat |
| 7  | Modulus                | Sisa bagi |
| 8  | Square Root            | Akar kuadrat |
| 9  | Logarithm              | Logaritma basis 10 |
| 10 | Sin                    | Sinus |
| 11 | Cos                    | Cosinus |
| 12 | Tan                    | Tangen |
| 13 | View History           | Melihat riwayat perhitungan |
| 14 | Clear History          | Menghapus riwayat |
| 0  | Exit                   | Keluar dari program |

---

## 🛠 Contoh Penggunaan
```text
==== Perfect Scientific Calculator ====
1. Automatic Calculation
2. Addition
...
0. Exit

Choose menu: 1
Expression: sqrt(16) + log(100)
sqrt(16) + log(100) = 6
```

---

## 📝 Catatan
- Program ini berjalan di **Python 3**.
- Riwayat tersimpan otomatis di file `history.txt`.
- Jika ingin menghapus riwayat, gunakan menu `Clear History`.

---

## 📜 Lisensi
MIT License – bebas digunakan, dimodifikasi, dan dikembangkan kembali.
