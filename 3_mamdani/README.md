# Level 3: Mamdani Fuzzy Inference System

Folder ini berisi pembelajaran tentang metode Mamdani.

## Apa itu Mamdani?

Mamdani FIS adalah metode inferensi fuzzy yang:
- Output berupa **fuzzy sets** (bukan fungsi)
- Menggunakan **linguistic rules**
- Defuzzifikasi untuk mendapat crisp output

## 4 Tahapan Mamdani

```
1. FUZZIFIKASI
   Crisp Input → Fuzzy Membership

2. EVALUASI ATURAN
   IF-THEN rules → Firing Strength

3. AGREGASI
   Gabung semua output rules (MAX)

4. DEFUZZIFIKASI
   Fuzzy Output → Crisp Value
```

## Subfolder

### 📁 core/
Implementasi inti Mamdani
- `01_mamdani_intro.py` - Pengenalan sistem Mamdani
- `02_rule_evaluation.py` - Detail evaluasi aturan
- `03_aggregation.py` - Metode agregasi
- `04_complete_system.py` - Sistem lengkap

### 📁 inference/
Inference engine
- Rule base management
- Inference algorithms
- Optimization techniques

### 📁 defuzzification/
Metode defuzzifikasi
- `01_centroid.py` - Center of Gravity (COG)
- `02_bisector.py` - Bisector method
- `03_mom.py` - Mean of Maximum
- `04_comparison.py` - Perbandingan metode

### 📁 examples/
Studi kasus
- `tipping_problem.py` - Sistem tip restoran
- `temperature_control.py` - Kontrol suhu AC
- `washing_machine.py` - Logika mesin cuci

## Operator yang Digunakan

### AND (T-norm)
- **MIN**: min(μA(x), μB(x))
- **PRODUCT**: μA(x) × μB(x)

### OR (T-conorm)
- **MAX**: max(μA(x), μB(x))
- **Prob Sum**: μA(x) + μB(x) - μA(x)×μB(x)

### Agregasi
- **MAX**: Paling umum untuk Mamdani
- **SUM**: Alternative (probabilistic)

## Metode Defuzzifikasi

| Metode | Karakteristik | Kapan Digunakan |
|--------|---------------|-----------------|
| **Centroid (COG)** | Center of gravity | Default, balanced |
| **Bisector** | Membagi area 2 sama | Alternative to COG |
| **MOM** | Mean of maximum | Penekanan pada puncak |
| **SOM/LOM** | Smallest/Largest | Edge cases |

## Contoh Aturan Mamdani

```
IF temperature is COLD THEN heater is HIGH
IF temperature is WARM THEN heater is MEDIUM
IF temperature is HOT THEN heater is OFF
```

## Kelebihan Mamdani

✅ Intuitif dan mudah dipahami
✅ Linguistic rules natural
✅ Cocok untuk decision making
✅ Interpretable output

## Kekurangan Mamdani

❌ Komputasi lebih berat (defuzzifikasi)
❌ Tidak cocok untuk real-time yang sangat cepat
❌ Butuh banyak rules untuk sistem kompleks

## Urutan Pembelajaran

```
core/01_mamdani_intro.py
    ↓
core/02_rule_evaluation.py
    ↓
defuzzification/01_centroid.py
    ↓
examples/tipping_problem.py
    ↓
examples/temperature_control.py
```

## Tips

1. Mulai dengan sistem sederhana (1-2 input, 1 output)
2. Visualisasi membership functions
3. Trace manual untuk satu input
4. Eksperimen dengan berbagai defuzzification methods
5. Bandingkan hasil dengan intuisi manusia

Selamat belajar Mamdani! 🎯
