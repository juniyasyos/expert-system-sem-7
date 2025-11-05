# Expert System & Fuzzy Logic Learning Project

Project ini dirancang untuk mempelajari **Sistem Pakar** dan **Fuzzy Logic** (Mamdani & Sugeno) dari dasar **tanpa menggunakan library eksternal** - murni implementasi Python native.

## 📚 Tujuan Pembelajaran

1. Memahami konsep dasar sistem pakar (expert system)
2. Memahami dan mengimplementasikan fuzzy logic dari nol
3. Menguasai metode Mamdani dan Sugeno
4. Membangun intuisi tentang reasoning dan inference

## 🗂️ Struktur Project

```
expert-system/
├── 1_expert_system/          # Sistem Pakar
│   ├── basic/                # Konsep dasar
│   ├── forward_chaining/     # Forward chaining
│   ├── backward_chaining/    # Backward chaining
│   └── examples/             # Contoh kasus
├── 2_fuzzy_logic/            # Fuzzy Logic Dasar
│   ├── fuzzification/        # Proses fuzzifikasi
│   ├── membership_functions/ # Fungsi keanggotaan
│   ├── fuzzy_operations/     # Operasi fuzzy
│   └── examples/             # Contoh sederhana
├── 3_mamdani/                # Metode Mamdani
│   ├── core/                 # Implementasi inti
│   ├── inference/            # Inference engine
│   ├── defuzzification/      # Defuzzifikasi
│   └── examples/             # Studi kasus
├── 4_sugeno/                 # Metode Sugeno
│   ├── core/                 # Implementasi inti
│   ├── inference/            # Inference engine
│   └── examples/             # Studi kasus
├── 5_projects/               # Project lengkap
│   ├── hvac_control/         # Kontrol AC
│   ├── traffic_light/        # Lampu lalu lintas
│   └── medical_diagnosis/    # Diagnosis medis
└── utils/                    # Helper functions
```

## 🎯 Alur Pembelajaran

### **Level 1: Expert System Basics (Minggu 1-2)**

#### 1.1 Konsep Dasar Sistem Pakar
- Pahami knowledge base (basis pengetahuan)
- Inference engine (mesin inferensi)
- Rule-based reasoning

📁 Mulai dari: `1_expert_system/basic/`

**Latihan:**
1. `01_knowledge_base.py` - Memahami representasi pengetahuan
2. `02_simple_rules.py` - Membuat aturan IF-THEN sederhana
3. `03_fact_matching.py` - Mencocokkan fakta dengan aturan

#### 1.2 Forward Chaining
- Data-driven reasoning
- Dari fakta menuju kesimpulan

📁 Lanjut ke: `1_expert_system/forward_chaining/`

**Latihan:**
1. `01_basic_forward.py` - Implementasi forward chaining sederhana
2. `02_conflict_resolution.py` - Menangani konflik aturan
3. `03_animal_identification.py` - Contoh: identifikasi hewan

#### 1.3 Backward Chaining
- Goal-driven reasoning
- Dari tujuan mundur ke fakta

📁 Lanjut ke: `1_expert_system/backward_chaining/`

**Latihan:**
1. `01_basic_backward.py` - Implementasi backward chaining
2. `02_goal_tree.py` - Membuat pohon tujuan
3. `03_medical_diagnosis.py` - Contoh: diagnosis penyakit

---

### **Level 2: Fuzzy Logic Fundamentals (Minggu 3-4)**

#### 2.1 Pengenalan Fuzzy Logic
- Perbedaan crisp vs fuzzy
- Fuzzy sets (himpunan fuzzy)
- Degree of membership

📁 Mulai dari: `2_fuzzy_logic/fuzzification/`

**Latihan:**
1. `01_crisp_vs_fuzzy.py` - Memahami perbedaan dasar
2. `02_fuzzy_sets.py` - Membuat himpunan fuzzy
3. `03_fuzzification.py` - Proses fuzzifikasi nilai crisp

#### 2.2 Fungsi Keanggotaan
- Triangular membership function
- Trapezoidal membership function
- Gaussian membership function

📁 Lanjut ke: `2_fuzzy_logic/membership_functions/`

**Latihan:**
1. `01_triangular.py` - Implementasi fungsi triangular
2. `02_trapezoidal.py` - Implementasi fungsi trapezoidal
3. `03_gaussian.py` - Implementasi fungsi gaussian
4. `04_custom_functions.py` - Membuat fungsi custom

#### 2.3 Operasi Fuzzy
- AND (minimum/product)
- OR (maximum/probabilistic sum)
- NOT (complement)

📁 Lanjut ke: `2_fuzzy_logic/fuzzy_operations/`

**Latihan:**
1. `01_basic_operations.py` - AND, OR, NOT
2. `02_t_norms.py` - T-norms dan T-conorms
3. `03_composition.py` - Komposisi fuzzy relations

---

### **Level 3: Mamdani Fuzzy Inference (Minggu 5-6)**

#### 3.1 Sistem Mamdani
- Fuzzifikasi input
- Evaluasi aturan (rule evaluation)
- Agregasi output
- Defuzzifikasi

📁 Mulai dari: `3_mamdani/core/`

**Latihan:**
1. `01_mamdani_intro.py` - Pengenalan sistem Mamdani
2. `02_rule_evaluation.py` - Evaluasi aturan fuzzy
3. `03_aggregation.py` - Agregasi hasil
4. `04_complete_system.py` - Sistem lengkap

#### 3.2 Metode Defuzzifikasi
- Centroid (Center of Gravity)
- Bisector
- Mean of Maximum (MOM)
- Smallest/Largest of Maximum

📁 Lanjut ke: `3_mamdani/defuzzification/`

**Latihan:**
1. `01_centroid.py` - Metode centroid
2. `02_bisector.py` - Metode bisector
3. `03_mom.py` - Mean of Maximum
4. `04_comparison.py` - Perbandingan metode

#### 3.3 Studi Kasus Mamdani

📁 Lanjut ke: `3_mamdani/examples/`

**Project:**
1. `tipping_problem.py` - Menentukan tip restoran
2. `temperature_control.py` - Kontrol suhu ruangan
3. `washing_machine.py` - Logika mesin cuci

---

### **Level 4: Sugeno Fuzzy Inference (Minggu 7-8)**

#### 4.1 Sistem Sugeno
- Perbedaan dengan Mamdani
- Zero-order Sugeno
- First-order Sugeno
- Weighted average defuzzification

📁 Mulai dari: `4_sugeno/core/`

**Latihan:**
1. `01_sugeno_intro.py` - Pengenalan Sugeno
2. `02_zero_order.py` - Implementasi zero-order
3. `03_first_order.py` - Implementasi first-order
4. `04_mamdani_vs_sugeno.py` - Perbandingan

#### 4.2 Studi Kasus Sugeno

📁 Lanjut ke: `4_sugeno/examples/`

**Project:**
1. `prediction_model.py` - Model prediksi
2. `adaptive_control.py` - Kontrol adaptif
3. `investment_decision.py` - Keputusan investasi

---

### **Level 5: Project Komprehensif (Minggu 9-10)**

#### 5.1 HVAC Control System
Sistem kontrol AC berdasarkan suhu dan kelembaban

📁 Lokasi: `5_projects/hvac_control/`

#### 5.2 Traffic Light Controller
Pengaturan lampu lalu lintas cerdas

📁 Lokasi: `5_projects/traffic_light/`

#### 5.3 Medical Diagnosis System
Sistem diagnosis penyakit dengan expert system + fuzzy

📁 Lokasi: `5_projects/medical_diagnosis/`

---

## 🚀 Cara Memulai

### 1. Setup Environment
```bash
# Tidak perlu install package eksternal!
# Hanya gunakan Python standard library
python3 --version  # Pastikan Python 3.7+
```

### 2. Pilih Mode Pembelajaran

#### 🎓 Mode Interaktif (Jupyter Notebook) - **RECOMMENDED**
```bash
# Buka VS Code di folder ini
# Lalu buka notebook yang ingin dipelajari:
# - 1_expert_system/01_Expert_System_Basics.ipynb
# - 2_fuzzy_logic/02_Fuzzy_Logic_Basics.ipynb
```

**Keuntungan Notebook:**
- ✅ Interaktif - jalankan cell per cell
- ✅ Visualisasi langsung
- ✅ Mudah eksperimen
- ✅ Dokumentasi terintegrasi

#### 📝 Mode Script (.py files)
```bash
# Untuk yang prefer file Python biasa
cd 1_expert_system/basic
python3 01_knowledge_base.py

# Ikuti urutan file berdasarkan nomor
```

### 3. Eksperimen dan Modifikasi
- Ubah parameter untuk melihat efeknya
- Tambahkan aturan baru
- Coba buat contoh kasus sendiri

---

## 📖 Konsep Kunci yang Akan Dipelajari

### Expert System
- **Knowledge Representation**: Cara merepresentasikan pengetahuan
- **Inference Engine**: Mesin untuk melakukan reasoning
- **Forward Chaining**: Reasoning dari data ke kesimpulan
- **Backward Chaining**: Reasoning dari tujuan ke data

### Fuzzy Logic
- **Fuzzification**: Mengubah nilai crisp menjadi fuzzy
- **Membership Function**: Fungsi yang mendefinisikan derajat keanggotaan
- **Fuzzy Rules**: Aturan berbasis logika fuzzy (IF-THEN)
- **Inference**: Proses evaluasi aturan
- **Defuzzification**: Mengubah output fuzzy menjadi crisp

### Mamdani vs Sugeno
| Aspek | Mamdani | Sugeno |
|-------|---------|--------|
| Output | Fuzzy set | Fungsi linear/konstan |
| Defuzzification | COG, Bisector, MOM | Weighted Average |
| Interpretabilitas | Lebih intuitif | Lebih matematis |
| Komputasi | Lebih berat | Lebih ringan |
| Use Case | Kontrol, decision making | Prediksi, adaptive systems |

---

## 💡 Tips Belajar

1. **Jangan Skip**: Ikuti urutan dari Level 1 sampai 5
2. **Hands-on**: Jalankan setiap kode, ubah parameter, amati hasilnya
3. **Visualisasi**: Gambar membership functions di kertas untuk pemahaman
4. **Debug**: Gunakan print() untuk melihat step-by-step proses
5. **Eksperimen**: Setelah paham, buat contoh kasus sendiri
6. **Dokumentasi**: Buat catatan tentang apa yang dipelajari

---

## 🎓 Resource Tambahan

### Buku Referensi (Opsional)
- "Expert Systems: Principles and Programming" - Giarratano & Riley
- "Fuzzy Logic with Engineering Applications" - Timothy J. Ross
- "Introduction to Fuzzy Logic using MATLAB" - Sivanandam et al.

### Konsep Matematika
- Set theory (teori himpunan)
- Boolean logic
- Integral (untuk centroid defuzzification)

---

## 📝 Evaluasi Pembelajaran

Setelah menyelesaikan setiap level, coba jawab:

1. **Level 1**: Bisakah Anda membuat sistem pakar untuk domain tertentu?
2. **Level 2**: Bisakah Anda menjelaskan perbedaan crisp dan fuzzy?
3. **Level 3**: Bisakah Anda membuat sistem Mamdani dari nol?
4. **Level 4**: Kapan menggunakan Mamdani vs Sugeno?
5. **Level 5**: Bisakah Anda membuat aplikasi praktis?

---

## 🤝 Kontribusi

Ini adalah project pembelajaran pribadi. Silakan:
- Tambahkan contoh kasus baru
- Improve dokumentasi
- Buat visualisasi
- Share hasil pembelajaran

---

**Selamat Belajar! 🚀**

Ingat: Tujuan utama adalah **memahami konsep**, bukan sekedar copy-paste code. Take your time dan enjoy the learning process!
