# Level 5: Complete Projects

Folder ini berisi project-project lengkap yang mengintegrasikan semua konsep yang telah dipelajari.

## Projects

### 🌡️ 1. HVAC Control System
**Folder**: `hvac_control/`

**Deskripsi**: Sistem kontrol AC pintar menggunakan fuzzy logic

**Input Variables**:
- Suhu ruangan (°C)
- Kelembaban (%)
- Jumlah orang dalam ruangan

**Output Variables**:
- Kecepatan kipas (RPM)
- Suhu target (°C)

**Teknik**:
- Mamdani FIS untuk kontrol
- Multiple inputs, multiple outputs
- Real-world constraints

**Pembelajaran**:
- Multi-input fuzzy systems
- Energy efficiency rules
- Comfort optimization

---

### 🚦 2. Traffic Light Controller
**Folder**: `traffic_light/`

**Deskripsi**: Pengaturan lampu lalu lintas adaptif

**Input Variables**:
- Jumlah kendaraan per jalur
- Waktu tunggu rata-rata
- Waktu dalam hari (peak/off-peak)

**Output Variables**:
- Durasi lampu hijau (detik)
- Prioritas jalur

**Teknik**:
- Sugeno FIS untuk prediksi
- Dynamic rule weighting
- Time-based adaptation

**Pembelajaran**:
- Sequential decision making
- Multi-objective optimization
- Real-time constraints

---

### 🏥 3. Medical Diagnosis System
**Folder**: `medical_diagnosis/`

**Deskripsi**: Sistem diagnosis penyakit dengan expert system dan fuzzy logic

**Components**:
- **Expert System**: Rule-based diagnosis
- **Fuzzy Logic**: Severity assessment
- **Hybrid**: Confidence scoring

**Input**:
- Symptoms (boolean dan fuzzy)
- Vital signs (crisp values)
- Patient history

**Output**:
- Possible diseases (ranked)
- Confidence level (0-100%)
- Recommended actions

**Teknik**:
- Forward chaining (symptoms → diseases)
- Backward chaining (disease → verify symptoms)
- Mamdani for severity
- Certainty factors

**Pembelajaran**:
- Combining expert system + fuzzy
- Uncertainty handling
- Knowledge representation
- Explanation generation

---

## Struktur Project

Setiap project memiliki struktur:

```
project_name/
├── README.md           # Dokumentasi project
├── knowledge_base.py   # Rules dan facts
├── fuzzy_system.py     # FIS implementation
├── main.py             # Program utama
├── test_cases.py       # Unit tests
└── examples/           # Contoh penggunaan
    ├── scenario_1.py
    ├── scenario_2.py
    └── ...
```

## Cara Menggunakan

### 1. Pilih Project
Mulai dari project yang paling menarik bagi Anda

### 2. Baca README
Pahami requirement dan spesifikasi

### 3. Jalankan Examples
```bash
cd 5_projects/hvac_control
python examples/scenario_1.py
```

### 4. Eksperimen
- Ubah rules
- Tambah input variables
- Adjust membership functions
- Test edge cases

### 5. Extend
- Tambah fitur baru
- Improve accuracy
- Optimize performance
- Add visualization

## Learning Path

```
Jika tertarik KONTROL → Mulai dari HVAC
    ↓
Jika tertarik OPTIMIZATION → Mulai dari Traffic Light
    ↓
Jika tertarik AI MEDICAL → Mulai dari Medical Diagnosis
    ↓
Selesaikan semua 3 projects!
```

## Challenges

Setelah menguasai projects:

1. **Integration Challenge**
   - Gabungkan 2-3 project menjadi smart building system
   
2. **Optimization Challenge**
   - Tune parameters untuk performance maksimal
   
3. **Extension Challenge**
   - Tambah machine learning untuk adaptive rules
   
4. **Real-world Challenge**
   - Deploy ke hardware (Raspberry Pi, Arduino)

## Project Ideas (Your Own!)

Setelah selesai, coba buat project sendiri:

- 🏭 **Industrial Control**: Pabrik automation
- 🌾 **Agriculture**: Irrigation system
- 💰 **Finance**: Investment advisor
- 🎮 **Gaming**: AI opponent
- 🏠 **Smart Home**: Complete home automation
- 🚗 **Autonomous Vehicle**: Lane keeping, cruise control
- 📊 **Risk Assessment**: Credit scoring
- ⚡ **Energy Management**: Smart grid
- 🍳 **Cooking**: Recipe recommendation
- 🏋️ **Fitness**: Workout planner

## Evaluation Criteria

Evaluasi project Anda berdasarkan:

1. **Correctness** (40%)
   - Logic benar?
   - Output masuk akal?
   - Edge cases handled?

2. **Code Quality** (20%)
   - Clean code?
   - Well documented?
   - Reusable?

3. **Innovation** (20%)
   - Unique approach?
   - Creative rules?
   - Interesting features?

4. **Completeness** (20%)
   - All requirements met?
   - Tests included?
   - Examples provided?

## Tips untuk Success

1. **Start Simple**: Mulai dengan 2 input, 1 output
2. **Iterative**: Tambah kompleksitas bertahap
3. **Test Often**: Jangan tunggu selesai baru test
4. **Document**: Tulis alasan di balik design decisions
5. **Visualize**: Plot membership functions dan results
6. **Compare**: Bandingkan Mamdani vs Sugeno
7. **Validate**: Test dengan data real atau realistic

## Resources

### Datasets (untuk testing)
- Temperature/humidity logs
- Traffic data
- Medical symptom databases

### Validation
- Compare dengan:
  - Human expert decisions
  - Classical algorithms (PID, etc)
  - Other fuzzy implementations

### Documentation
- Explain your rules
- Justify membership functions
- Show example traces
- Performance metrics

---

**Selamat mengerjakan projects! 🎉**

Ini adalah kulminasi dari semua pembelajaran Anda. Take your time, enjoy the process, dan bangga dengan hasilnya!

**Ingat**: Tujuan bukan hanya working code, tapi **understanding** yang mendalam! 💡
