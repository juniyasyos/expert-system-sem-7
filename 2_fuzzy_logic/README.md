# Level 2: Fuzzy Logic

Folder ini berisi pembelajaran tentang fuzzy logic dari dasar.

## Subfolder

### 📁 fuzzification/
Proses mengubah crisp value menjadi fuzzy
- `01_crisp_vs_fuzzy.py` - Perbedaan crisp dan fuzzy logic
- `02_fuzzy_sets.py` - Himpunan fuzzy
- `03_fuzzification.py` - Proses fuzzifikasi

### 📁 membership_functions/
Berbagai jenis fungsi keanggotaan
- `01_triangular.py` - Fungsi triangular
- `02_trapezoidal.py` - Fungsi trapezoidal
- `03_gaussian.py` - Fungsi gaussian
- `04_custom_functions.py` - Membuat fungsi custom

### 📁 fuzzy_operations/
Operasi pada fuzzy sets
- `01_basic_operations.py` - AND, OR, NOT
- `02_t_norms.py` - T-norms dan T-conorms
- `03_composition.py` - Komposisi relasi fuzzy

### 📁 examples/
Contoh aplikasi sederhana
- Temperature control
- Speed classification
- Risk assessment

## Konsep Penting

### Derajat Keanggotaan
Nilai antara 0 dan 1 yang menunjukkan seberapa "cocok" suatu nilai dengan kategori tertentu.

### Fungsi Keanggotaan
Fungsi yang memetakan nilai crisp ke derajat keanggotaan fuzzy.

### Operasi Fuzzy
- **AND**: MIN atau PRODUCT
- **OR**: MAX atau Probabilistic Sum
- **NOT**: 1 - membership

## Urutan Pembelajaran

```
fuzzification/01_crisp_vs_fuzzy.py
    ↓
fuzzification/02_fuzzy_sets.py
    ↓
membership_functions/01_triangular.py
    ↓
membership_functions/02_trapezoidal.py
    ↓
fuzzy_operations/01_basic_operations.py
    ↓
examples/...
```

## Kapan Menggunakan Fuzzy Logic?

✅ **Gunakan Fuzzy** ketika:
- Ada ketidakpastian atau ambiguitas
- Transisi antar kategori tidak tegas
- Modeling pemikiran manusia
- Sistem kontrol yang smooth

❌ **Gunakan Crisp** ketika:
- Keputusan tegas diperlukan
- Data jelas terpisah
- Sistem sederhana cukup

Selamat belajar! 🌟
