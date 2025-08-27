# 📒 Catatan Belajar – Hari 1

## 1. Identitas
- 📅 Tanggal: 27 Agustus 2025
- ⏰ Waktu belajar: 20.00 – 22.30
- 🎯 Topik: Python OOP – Class & Object
- 📌 Tujuan: Memahami konsep class dan object, bisa membuat class sederhana dengan atribut & method.

---

## 2. Ringkasan Materi
- Class = blueprint / cetakan untuk membuat object.
- Object = instance nyata dari class.
- `__init__` → constructor, otomatis dipanggil saat object dibuat.
- `self` → mereferensikan object itu sendiri.

---

## 3. Catatan Kode
```python
# Membuat class sederhana
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        return f"Hi, my name is {self.name} and I study {self.major}."

# Membuat object
s1 = Student("Yahya", "Economics Education")
print(s1.introduce())
```
```perl
Hi, my name is Yahya and I study Economics Education.

```

## 4. Praktik / Mini-Project
🎯 Buat `class` Book dengan atribut: `title`, `author`, `year`.
Tambahkan method `get_info()` untuk menampilkan data buku.
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.year}"

book1 = Book("Practical Statistics for Data Scientists", "Peter Bruce", 2020)
print(book1.get_info())
```
```csharp
'Practical Statistics for Data Scientists' by Peter Bruce, 2020
```

## 5. Insight / Refleksi
- Awalnya bingung kenapa harus ada `self`, ternyata itu pointer ke object sendiri.
- Paham bahwa class = definisi, object = hasil nyata.
- Masih perlu latihan membedakan atribut (data) vs method (fungsi).

---

## 6. Next Step
📌 Besok: OOP – Inheritance (pewarisan class).
🎯 Tujuan: Bisa membuat class turunan & gunakan `super()`.

---