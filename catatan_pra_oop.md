# 📘 Catatan Belajar – Pra OOP

## 1. Dasar Python
- **Variabel & Tipe Data**  
  - `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`.  
  - Contoh:  
    ```python
    nama = "Yahya"
    umur = 24
    mahasiswa = True
    ```
- **Operator**  
  - Aritmatika: `+ - * / % // **`  
  - Perbandingan: `== != > < >= <=`  
  - Logika: `and, or, not`  

- **Input & Output**  
  ```python
  nama = input("Masukkan nama: ")
  print("Halo,", nama)
  ```

---

## 2. Struktur Kontrol
- **Percabangan (if-elif-else)**  
  ```python
  if umur >= 18:
      print("Dewasa")
  else:
      print("Belum dewasa")
  ```
- **Perulangan (for, while)**  
  ```python
  for i in range(5):
      print(i)
  ```

- **Loop dengan kondisi**  
  ```python
  angka = 1
  while angka <= 5:
      print(angka)
      angka += 1
  ```

---

## 3. Fungsi
- **Definisi & Pemanggilan**  
  ```python
  def tambah(a, b):
      return a + b

  print(tambah(3, 4))
  ```
- **Parameter default & keyword arguments**  
  ```python
  def salam(nama="User"):
      print(f"Halo {nama}")

  salam()
  salam("Yahya")
  ```

- **Scope variabel (lokal & global)**

---

## 4. Struktur Data
- **List**  
  - Bisa diubah (mutable).  
  - Operasi: `append`, `remove`, `sort`, slicing.  
- **Tuple**  
  - Immutable (tidak bisa diubah).  
- **Set**  
  - Tidak ada duplikat.  
- **Dictionary**  
  - Key-value pair.  
  ```python
  mhs = {"nama": "Yahya", "umur": 24}
  print(mhs["nama"])
  ```

---

## 5. Dasar Statistik untuk Data Science
- **Ukuran Pemusatan**: mean, median, mode.  
- **Ukuran Penyebaran**: range, variance, standard deviation.  
- **Visualisasi Awal**: histogram, scatter plot, boxplot.  
- **Distribusi Data**: normal distribution, skewness.  

---

## 6. Pandas & Numpy (Intro)
- **Numpy**: operasi array, vektor, matriks.  
- **Pandas**: DataFrame, series, indexing, filtering.  
- Contoh:
  ```python
  import pandas as pd
  df = pd.DataFrame({
      "Nama": ["A", "B", "C"],
      "Nilai": [90, 85, 88]
  })
  print(df.head())
  ```

---

## 7. Visualisasi Data (Intro Matplotlib/Seaborn)
- `plt.plot()`, `plt.scatter()`, `plt.hist()`.  
- Seaborn untuk visualisasi yang lebih estetik (`sns.barplot`, `sns.heatmap`).  

---

✍️ **Catatan:** Semua materi di atas adalah *fondasi* sebelum masuk ke OOP. Jadi kamu sudah punya bekal Python, statistik dasar, dan library utama (NumPy, Pandas, Matplotlib).  
