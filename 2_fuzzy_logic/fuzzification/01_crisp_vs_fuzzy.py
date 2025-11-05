"""
LEVEL 2.1: Crisp vs Fuzzy (Perbedaan Dasar)

Konsep:
--------
CRISP LOGIC (Logika Tegas):
- Nilai hanya 0 atau 1 (False atau True)
- Contoh: Suhu > 30°C = Panas (100% panas atau 0% panas)

FUZZY LOGIC (Logika Fuzzy):
- Nilai antara 0 dan 1 (derajat keanggotaan)
- Contoh: Suhu 28°C = 60% panas, 40% hangat

Tujuan:
-------
- Memahami keterbatasan crisp logic
- Mengenal konsep "derajat keanggotaan"
- Memahami mengapa fuzzy logic diperlukan
"""

def crisp_temperature(temp):
    """
    Klasifikasi suhu dengan CRISP logic
    
    Masalah: Transisi mendadak, tidak natural
    """
    print("\n" + "="*60)
    print("CRISP LOGIC: Klasifikasi Suhu")
    print("="*60)
    
    print(f"\nSuhu: {temp}°C")
    print("-"*60)
    
    # Aturan crisp (tegas)
    if temp <= 15:
        category = "DINGIN"
    elif temp <= 25:
        category = "HANGAT"
    else:
        category = "PANAS"
    
    print(f"Klasifikasi: {category}")
    print(f"Membership:")
    print(f"  • Dingin: {1 if temp <= 15 else 0}")
    print(f"  • Hangat: {1 if 15 < temp <= 25 else 0}")
    print(f"  • Panas:  {1 if temp > 25 else 0}")
    
    return category


def fuzzy_temperature(temp):
    """
    Klasifikasi suhu dengan FUZZY logic
    
    Keuntungan: Transisi halus, lebih natural
    """
    print("\n" + "="*60)
    print("FUZZY LOGIC: Klasifikasi Suhu")
    print("="*60)
    
    print(f"\nSuhu: {temp}°C")
    print("-"*60)
    
    # Fungsi keanggotaan triangular sederhana
    # Dingin: puncak di 10°C, turun ke 0 di 20°C
    if temp <= 10:
        dingin = 1.0
    elif temp <= 20:
        dingin = (20 - temp) / 10  # Menurun linear
    else:
        dingin = 0.0
    
    # Hangat: puncak di 20°C, turun ke 0 di 10°C dan 30°C
    if temp <= 10:
        hangat = 0.0
    elif temp <= 20:
        hangat = (temp - 10) / 10  # Naik linear
    elif temp <= 30:
        hangat = (30 - temp) / 10  # Turun linear
    else:
        hangat = 0.0
    
    # Panas: puncak di 35°C, naik dari 0 di 25°C
    if temp <= 25:
        panas = 0.0
    elif temp <= 35:
        panas = (temp - 25) / 10  # Naik linear
    else:
        panas = 1.0
    
    print(f"Membership (derajat keanggotaan):")
    print(f"  • Dingin: {dingin:.2f} ({dingin*100:.1f}%)")
    print(f"  • Hangat: {hangat:.2f} ({hangat*100:.1f}%)")
    print(f"  • Panas:  {panas:.2f} ({panas*100:.1f}%)")
    
    # Kategori dominan
    categories = [
        ("DINGIN", dingin),
        ("HANGAT", hangat),
        ("PANAS", panas)
    ]
    dominant = max(categories, key=lambda x: x[1])
    
    print(f"\nKategori dominan: {dominant[0]} ({dominant[1]*100:.1f}%)")
    
    return dingin, hangat, panas


def compare_crisp_vs_fuzzy():
    """
    Bandingkan crisp dan fuzzy untuk berbagai suhu
    """
    print("\n" + "="*60)
    print("PERBANDINGAN: Crisp vs Fuzzy")
    print("="*60)
    
    test_temps = [10, 15, 18, 20, 23, 25, 28, 30, 35]
    
    print("\n{:<8} {:<12} {:<30}".format("Suhu", "Crisp", "Fuzzy (D/H/P)"))
    print("-"*60)
    
    for temp in test_temps:
        # Crisp
        if temp <= 15:
            crisp_result = "DINGIN"
        elif temp <= 25:
            crisp_result = "HANGAT"
        else:
            crisp_result = "PANAS"
        
        # Fuzzy (simplified)
        if temp <= 10:
            d, h, p = 1.0, 0.0, 0.0
        elif temp <= 20:
            d = (20 - temp) / 10
            h = (temp - 10) / 10
            p = 0.0
        elif temp <= 30:
            d = 0.0
            h = (30 - temp) / 10
            p = (temp - 25) / 10 if temp > 25 else 0.0
        else:
            d, h = 0.0, 0.0
            p = min(1.0, (temp - 25) / 10)
        
        fuzzy_result = f"{d:.2f}/{h:.2f}/{p:.2f}"
        
        print(f"{temp}°C     {crisp_result:<12} {fuzzy_result}")
    
    print("\n" + "="*60)
    print("OBSERVASI:")
    print("="*60)
    print("• Crisp: Perubahan mendadak di threshold")
    print("  - 25°C = HANGAT, 26°C = PANAS (lompatan)")
    print("\n• Fuzzy: Transisi halus dan bertahap")
    print("  - 25°C = 50% Hangat, 50% Panas")
    print("  - Lebih mencerminkan realitas!")


def demo_boundary_problem():
    """
    Demonstrasi masalah boundary di crisp logic
    """
    print("\n" + "="*60)
    print("MASALAH BOUNDARY di Crisp Logic")
    print("="*60)
    
    print("\nSkenario: Kontrol kipas berdasarkan suhu")
    print("-"*60)
    
    # Crisp rules
    print("\nAturan Crisp:")
    print("  IF temp <= 20°C THEN kipas = OFF")
    print("  IF temp > 20°C THEN kipas = ON")
    
    print("\n" + "-"*60)
    print("Suhu  | Crisp Decision | Masalah")
    print("-"*60)
    print("19°C  | OFF            | OK")
    print("20°C  | OFF            | OK")
    print("21°C  | ON             | Mendadak!")
    print("20°C  | OFF            | Flickering!")
    print("21°C  | ON             | Flickering!")
    
    print("\n" + "="*60)
    print("Masalah: Flickering di boundary!")
    print("="*60)
    
    # Fuzzy solution
    print("\nSolusi Fuzzy:")
    print("  Derajat keanggotaan memungkinkan:")
    print("  • 20°C: 50% OFF, 50% ON → Kipas kecepatan sedang")
    print("  • 21°C: 40% OFF, 60% ON → Kipas lebih kencang")
    print("  • Tidak ada flickering!")


def exercise_age_classification():
    """
    LATIHAN: Klasifikasi umur dengan crisp dan fuzzy
    
    TODO: Implementasikan fungsi ini!
    
    Buat klasifikasi:
    - Crisp: Anak (<18), Dewasa (18-60), Tua (>60)
    - Fuzzy: Transisi halus antar kategori
    
    Test dengan umur: 15, 18, 20, 55, 60, 65
    """
    print("\n" + "="*60)
    print("LATIHAN: Klasifikasi Umur")
    print("="*60)
    
    # TODO: Implementasi crisp classification
    def crisp_age(age):
        # Tulis kode di sini
        pass
    
    # TODO: Implementasi fuzzy classification
    def fuzzy_age(age):
        # Tulis kode di sini
        # Gunakan membership functions
        pass
    
    # TODO: Test dengan berbagai umur
    test_ages = [15, 18, 20, 55, 60, 65]
    # for age in test_ages:
    #     crisp_age(age)
    #     fuzzy_age(age)


def main():
    """Fungsi utama"""
    
    print("="*60)
    print("PENGENALAN: Crisp vs Fuzzy Logic")
    print("="*60)
    
    # Demo 1: Crisp
    crisp_temperature(23)
    
    # Demo 2: Fuzzy
    fuzzy_temperature(23)
    
    # Demo 3: Perbandingan
    compare_crisp_vs_fuzzy()
    
    # Demo 4: Boundary problem
    demo_boundary_problem()
    
    # Latihan (uncomment setelah mengerjakan)
    # exercise_age_classification()
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("="*60)
    print("✓ Crisp: Nilai 0 atau 1, transisi mendadak")
    print("✓ Fuzzy: Nilai 0-1, transisi halus")
    print("✓ Fuzzy lebih natural untuk model dunia nyata")
    print("✓ Derajat keanggotaan = seberapa 'cocok' dengan kategori")
    print("="*60)


if __name__ == "__main__":
    main()


"""
PERTANYAAN REFLEKSI:
-------------------
1. Mengapa crisp logic memiliki masalah di boundary?
2. Apa keuntungan menggunakan derajat keanggotaan?
3. Kapan crisp logic sudah cukup?
4. Bagaimana fuzzy mengatasi ketidakpastian?

NEXT STEP:
----------
Lanjut ke: 02_fuzzy_sets.py
Topik: Himpunan fuzzy dan operasinya
"""
