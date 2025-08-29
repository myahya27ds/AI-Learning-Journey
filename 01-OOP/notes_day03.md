# 📘 Notes Hari ke-3: OOP Lanjutan (Encapsulation & Inheritance)

## 1. Encapsulation
- **Encapsulation** adalah cara menyembunyikan detail data (atribut) agar tidak bisa diakses langsung dari luar class.
- Gunakan konvensi:
  - `self._atribut` → **protected** (boleh diakses turunan, tapi tidak dianjurkan langsung dari luar).
  - `self.__atribut` → **private** (benar-benar tersembunyi, tidak bisa diakses langsung).
- Biasanya digunakan bersama **getter** dan **setter**.

### Contoh:
```python
class AkunBank:
    def __init__(self, saldo):
        self.__saldo = saldo   # private

    # Getter
    def get_saldo(self):
        return self.__saldo

    # Setter
    def set_saldo(self, jumlah):
        if jumlah >= 0:
            self.__saldo = jumlah
        else:
            print("Saldo tidak boleh negatif!")

akun = AkunBank(1000000)
print(akun.get_saldo())   # 1000000
akun.set_saldo(2000000)
print(akun.get_saldo())   # 2000000
