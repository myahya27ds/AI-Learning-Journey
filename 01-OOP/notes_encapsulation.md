# 📘 OOP Python – Encapsulation

## 🔹 Konsep Encapsulation
Encapsulation = **menyembunyikan data** agar tidak bisa diakses sembarangan dari luar class.  
👉 Tujuan: keamanan data & hanya bisa diubah lewat method (getter & setter).

### 🔑 Tingkatan Akses Atribut
- `self.atribut` → **public** → bebas diakses dari luar class.
- `self._atribut` → **protected** → konvensi: jangan diakses langsung (hanya untuk internal / turunan class).
- `self.__atribut` → **private** → tidak bisa diakses langsung dari luar class.

---

## 🔹 Contoh: Rekening Bank
```python
class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama              # public
        self.__saldo = saldo          # private

    # Getter
    def lihat_saldo(self):
        return f"Saldo {self.nama}: Rp{self.__saldo}"

    # Setter - setor uang
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            return f"Berhasil setor Rp{jumlah}. Saldo sekarang: Rp{self.__saldo}"
        return "Jumlah setor harus positif!"

    # Setter - tarik uang
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return f"Berhasil tarik Rp{jumlah}. Saldo sekarang: Rp{self.__saldo}"
        return "Saldo tidak cukup atau jumlah tidak valid!"
```

### 📝 Pemakaian
```python
rekening1 = RekeningBank("Yahya", 100000)

print(rekening1.lihat_saldo())  
print(rekening1.setor(50000))  
print(rekening1.tarik(30000))  

# Coba akses langsung (akan error)
# print(rekening1.__saldo)
```

---

## 🔹 Output
```
Saldo Yahya: Rp100000
Berhasil setor Rp50000. Saldo sekarang: Rp150000
Berhasil tarik Rp30000. Saldo sekarang: Rp120000
```

---

## 🔹 Kesimpulan
- Encapsulation membuat data lebih **aman**.  
- Gunakan **getter & setter** untuk mengatur akses.  
- `__atribut` (private) **tidak bisa** diakses langsung dari luar class.  
