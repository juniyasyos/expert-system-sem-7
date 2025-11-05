"""
EXAMPLE PROJECT: Simple Temperature Controller
Contoh project sederhana untuk memahami alur lengkap

Sistem: Kontrol kecepatan kipas berdasarkan suhu ruangan
Input: Suhu (°C)
Output: Kecepatan kipas (%)
"""

# Menggunakan pure Python, no external libraries!


class TriangularMF:
    """Membership function triangular sederhana"""
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def __call__(self, x):
        if x <= self.a or x >= self.c:
            return 0.0
        elif x <= self.b:
            return (x - self.a) / (self.b - self.a)
        else:
            return (self.c - x) / (self.c - self.b)


def main():
    print("="*60)
    print("SIMPLE TEMPERATURE CONTROLLER")
    print("Fuzzy Logic - Mamdani Method")
    print("="*60)
    
    # 1. Definisikan Fuzzy Sets untuk INPUT (Suhu)
    print("\n1. FUZZY SETS - INPUT (Temperature)")
    print("-"*60)
    
    temp_cold = TriangularMF(0, 10, 25)
    temp_warm = TriangularMF(20, 25, 30)
    temp_hot = TriangularMF(25, 35, 45)
    
    print("   COLD:  Triangular(0, 10, 25)")
    print("   WARM:  Triangular(20, 25, 30)")
    print("   HOT:   Triangular(25, 35, 45)")
    
    # 2. Definisikan Fuzzy Sets untuk OUTPUT (Kecepatan Kipas)
    print("\n2. FUZZY SETS - OUTPUT (Fan Speed)")
    print("-"*60)
    
    fan_slow = TriangularMF(0, 0, 50)
    fan_medium = TriangularMF(0, 50, 100)
    fan_fast = TriangularMF(50, 100, 100)
    
    print("   SLOW:   Triangular(0, 0, 50)")
    print("   MEDIUM: Triangular(0, 50, 100)")
    print("   FAST:   Triangular(50, 100, 100)")
    
    # 3. Definisikan Aturan
    print("\n3. FUZZY RULES")
    print("-"*60)
    print("   R1: IF temp is COLD   THEN fan is SLOW")
    print("   R2: IF temp is WARM   THEN fan is MEDIUM")
    print("   R3: IF temp is HOT    THEN fan is FAST")
    
    # 4. Test dengan input tertentu
    input_temp = 28
    
    print("\n" + "="*60)
    print(f"INFERENSI untuk Temperature = {input_temp}°C")
    print("="*60)
    
    # STEP 1: Fuzzifikasi
    print("\n4. FUZZIFIKASI")
    print("-"*60)
    
    cold_degree = temp_cold(input_temp)
    warm_degree = temp_warm(input_temp)
    hot_degree = temp_hot(input_temp)
    
    print(f"   Temperature = {input_temp}°C")
    print(f"     → COLD:  {cold_degree:.3f} ({cold_degree*100:.1f}%)")
    print(f"     → WARM:  {warm_degree:.3f} ({warm_degree*100:.1f}%)")
    print(f"     → HOT:   {hot_degree:.3f} ({hot_degree*100:.1f}%)")
    
    # STEP 2: Evaluasi Aturan (firing strength)
    print("\n5. RULE EVALUATION (Firing Strength)")
    print("-"*60)
    
    # R1: COLD → SLOW
    firing_r1 = cold_degree
    print(f"   R1: COLD → SLOW")
    print(f"       Firing strength = {firing_r1:.3f}")
    
    # R2: WARM → MEDIUM
    firing_r2 = warm_degree
    print(f"   R2: WARM → MEDIUM")
    print(f"       Firing strength = {firing_r2:.3f}")
    
    # R3: HOT → FAST
    firing_r3 = hot_degree
    print(f"   R3: HOT → FAST")
    print(f"       Firing strength = {firing_r3:.3f}")
    
    # STEP 3: Agregasi (MAX operator)
    print("\n6. AGREGASI (MAX)")
    print("-"*60)
    
    # Untuk setiap output fuzzy set, ambil max dari firing strengths
    slow_strength = firing_r1
    medium_strength = firing_r2
    fast_strength = firing_r3
    
    print(f"   SLOW:   {slow_strength:.3f}")
    print(f"   MEDIUM: {medium_strength:.3f}")
    print(f"   FAST:   {fast_strength:.3f}")
    
    # STEP 4: Defuzzifikasi (Centroid/COG)
    print("\n7. DEFUZZIFIKASI (Centroid)")
    print("-"*60)
    
    # Hitung centroid dengan diskretisasi
    numerator = 0.0
    denominator = 0.0
    
    for speed in range(0, 101, 1):  # 0-100%
        # Untuk setiap nilai, hitung membership setelah clipping
        membership = 0.0
        
        # Clipping untuk SLOW
        membership = max(membership, min(slow_strength, fan_slow(speed)))
        
        # Clipping untuk MEDIUM
        membership = max(membership, min(medium_strength, fan_medium(speed)))
        
        # Clipping untuk FAST
        membership = max(membership, min(fast_strength, fan_fast(speed)))
        
        # Akumulasi untuk centroid
        numerator += membership * speed
        denominator += membership
    
    if denominator > 0:
        crisp_output = numerator / denominator
    else:
        crisp_output = 0
    
    print(f"   Crisp Output = {crisp_output:.2f}%")
    
    # Hasil Akhir
    print("\n" + "="*60)
    print("HASIL AKHIR")
    print("="*60)
    print(f"   Input:  Temperature = {input_temp}°C")
    print(f"   Output: Fan Speed   = {crisp_output:.1f}%")
    print("="*60)
    
    # Test beberapa suhu lainnya
    print("\n" + "="*60)
    print("TEST BERBAGAI SUHU")
    print("="*60)
    
    test_temps = [15, 20, 25, 28, 32, 38]
    
    print("\n  Suhu  |  Fan Speed")
    print("-"*30)
    
    for temp in test_temps:
        # Fuzzifikasi
        c = temp_cold(temp)
        w = temp_warm(temp)
        h = temp_hot(temp)
        
        # Agregasi
        s_str = c
        m_str = w
        f_str = h
        
        # Defuzzifikasi
        num = 0.0
        den = 0.0
        for spd in range(0, 101, 1):
            mem = max(
                min(s_str, fan_slow(spd)),
                min(m_str, fan_medium(spd)),
                min(f_str, fan_fast(spd))
            )
            num += mem * spd
            den += mem
        
        output = num / den if den > 0 else 0
        
        print(f"  {temp:4d}°C | {output:6.1f}%")
    
    print("\n" + "="*60)
    print("OBSERVASI:")
    print("-"*60)
    print("✓ Suhu rendah → kipas lambat")
    print("✓ Suhu sedang → kipas sedang")
    print("✓ Suhu tinggi → kipas cepat")
    print("✓ Transisi halus (tidak ada lompatan!)")
    print("="*60)


if __name__ == "__main__":
    main()


"""
ANALISIS PROJECT INI:
--------------------

1. INPUT VARIABLES
   - 1 variabel: temperature (°C)
   - 3 fuzzy sets: COLD, WARM, HOT

2. OUTPUT VARIABLES
   - 1 variabel: fan speed (%)
   - 3 fuzzy sets: SLOW, MEDIUM, FAST

3. RULES
   - 3 aturan sederhana (1-to-1 mapping)
   - Mudah dipahami dan diinterpretasi

4. METHOD
   - Mamdani FIS
   - Fuzzifikasi → Evaluasi → Agregasi → Defuzzifikasi

5. DEFUZZIFIKASI
   - Centroid (Center of Gravity)
   - Paling umum dan balanced

EKSPERIMEN:
-----------
1. Ubah parameter membership functions (a, b, c)
2. Tambah fuzzy set baru (misal: VERY_HOT)
3. Buat aturan lebih kompleks
4. Coba defuzzifikasi method lain
5. Tambah input variable (misal: humidity)

NEXT STEP:
----------
Setelah paham project ini, lanjut ke:
- 3_mamdani/examples/tipping_problem.py (lebih kompleks)
- 5_projects/ (real-world applications)
"""
