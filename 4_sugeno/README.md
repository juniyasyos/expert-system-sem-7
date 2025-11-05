# Level 4: Sugeno Fuzzy Inference System

Folder ini berisi pembelajaran tentang metode Sugeno.

## Apa itu Sugeno?

Sugeno FIS (juga disebut Takagi-Sugeno-Kang) adalah metode inferensi fuzzy yang:
- Output berupa **fungsi** (bukan fuzzy sets)
- Lebih efisien secara komputasi
- Cocok untuk adaptive systems dan ANFIS

## Perbedaan Mamdani vs Sugeno

| Aspek | Mamdani | Sugeno |
|-------|---------|--------|
| **Output** | Fuzzy sets | Linear/constant function |
| **Consequent** | Linguistic | Mathematical |
| **Defuzzification** | COG, Bisector, etc | Weighted Average |
| **Interpretability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Efisiensi** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Aplikasi** | Decision making | Prediction, Control |

## Tipe Sugeno

### Zero-Order Sugeno
```
IF x is A THEN y = k
```
Output adalah konstanta

### First-Order Sugeno
```
IF x is A AND z is B THEN y = px + qz + r
```
Output adalah fungsi linear

### Higher-Order Sugeno
```
IF x is A THEN y = f(x1, x2, ..., xn)
```
Output adalah fungsi nonlinear

## Proses Inferensi Sugeno

```
1. FUZZIFIKASI
   Crisp Input → Fuzzy Membership
   (Sama seperti Mamdani)

2. EVALUASI ATURAN
   Hitung firing strength untuk setiap rule
   (Sama seperti Mamdani)

3. HITUNG OUTPUT RULES
   zi = fi(x1, x2, ..., xn)
   (Berbeda dengan Mamdani!)

4. WEIGHTED AVERAGE
   y = Σ(wi × zi) / Σwi
   (Tidak perlu defuzzifikasi kompleks!)
```

## Subfolder

### 📁 core/
Implementasi inti Sugeno
- `01_sugeno_intro.py` - Pengenalan Sugeno
- `02_zero_order.py` - Zero-order Sugeno
- `03_first_order.py` - First-order Sugeno
- `04_mamdani_vs_sugeno.py` - Perbandingan langsung

### 📁 inference/
Inference engine
- Rule evaluation
- Weighted average calculation
- Optimization

### 📁 examples/
Studi kasus
- `prediction_model.py` - Model prediksi
- `adaptive_control.py` - Kontrol adaptif
- `investment_decision.py` - Keputusan investasi

## Contoh Aturan Sugeno

### Zero-Order
```python
# IF temperature is COLD THEN output = 100
# IF temperature is WARM THEN output = 50
# IF temperature is HOT THEN output = 0

rules = [
    ("COLD", lambda: 100),
    ("WARM", lambda: 50),
    ("HOT", lambda: 0)
]
```

### First-Order
```python
# IF temp is COLD THEN output = 2*temp + 30
# IF temp is WARM THEN output = 1*temp + 20
# IF temp is HOT THEN output = 0*temp + 0

rules = [
    ("COLD", lambda t: 2*t + 30),
    ("WARM", lambda t: 1*t + 20),
    ("HOT", lambda t: 0*t + 0)
]
```

## Formula Weighted Average

```
           w1×z1 + w2×z2 + ... + wn×zn
y_final = ─────────────────────────────
              w1 + w2 + ... + wn

Dimana:
- wi = firing strength dari rule i
- zi = output dari rule i (hasil fungsi)
```

## Kelebihan Sugeno

✅ Komputasi sangat efisien
✅ Cocok untuk mathematical modeling
✅ Mudah dioptimasi (ANFIS)
✅ Kontinuitas output terjamin
✅ Cocok untuk real-time systems

## Kekurangan Sugeno

❌ Kurang intuitif
❌ Output tidak linguistic
❌ Perlu pengetahuan matematika
❌ Sulit explain ke non-technical users

## Kapan Menggunakan Sugeno?

### Gunakan Sugeno untuk:
- **Prediction tasks** (forecasting, estimation)
- **Adaptive systems** (ANFIS, learning)
- **Real-time control** (kecepatan penting)
- **Mathematical modeling** (sudah ada formula)

### Gunakan Mamdani untuk:
- **Decision support** (interpretability penting)
- **Expert knowledge** (linguistic rules)
- **Classification** (output categorical)
- **Human interface** (explainability)

## Urutan Pembelajaran

```
core/01_sugeno_intro.py
    ↓
core/02_zero_order.py
    ↓
core/03_first_order.py
    ↓
core/04_mamdani_vs_sugeno.py
    ↓
examples/prediction_model.py
    ↓
examples/adaptive_control.py
```

## Tips Pembelajaran

1. **Pahami Mamdani dulu** - Sugeno adalah evolusi
2. **Mulai dari Zero-Order** - Paling sederhana
3. **Visualisasi fungsi output** - Lihat linear functions
4. **Bandingkan hasil** - Mamdani vs Sugeno untuk kasus sama
5. **Eksperimen coefficients** - Ubah p, q, r di first-order

## Example Comparison

```python
# MAMDANI
IF temp is COLD THEN heater is HIGH
# Output: Fuzzy set "HIGH" → Defuzzify → Crisp value

# SUGENO (Zero-Order)
IF temp is COLD THEN heater = 80
# Output: Konstanta 80

# SUGENO (First-Order)
IF temp is COLD THEN heater = -2*temp + 100
# Output: Linear function
```

## Advanced Topics

- **ANFIS** (Adaptive Neuro-Fuzzy Inference System)
- **Parameter optimization** (gradient descent)
- **Hybrid systems** (Mamdani + Sugeno)
- **TSK model identification**

Selamat belajar Sugeno! 🚀
