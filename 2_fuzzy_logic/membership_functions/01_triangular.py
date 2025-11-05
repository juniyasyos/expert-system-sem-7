"""
LEVEL 2.2: Triangular Membership Function

Konsep:
--------
Fungsi keanggotaan Triangular adalah fungsi berbentuk segitiga
yang paling sederhana dan banyak digunakan.

Bentuk:
    1.0 |      /\
        |     /  \
        |    /    \
    0.0 |___/______\___
        a    b     c

Dimana:
- a: titik awal (membership = 0)
- b: puncak (membership = 1)
- c: titik akhir (membership = 0)

Tujuan:
-------
- Implementasi fungsi triangular dari nol
- Memahami parameter a, b, c
- Visualisasi dengan ASCII art
"""

class TriangularMF:
    """
    Triangular Membership Function
    
    Fungsi keanggotaan berbentuk segitiga
    """
    
    def __init__(self, a, b, c, name=""):
        """
        Args:
            a: Titik awal (kiri)
            b: Puncak
            c: Titik akhir (kanan)
            name: Nama fuzzy set
        """
        if not (a <= b <= c):
            raise ValueError("Harus memenuhi: a <= b <= c")
        
        self.a = a
        self.b = b
        self.c = c
        self.name = name
    
    def membership(self, x):
        """
        Hitung derajat keanggotaan untuk nilai x
        
        Returns:
            float antara 0.0 dan 1.0
        """
        # Sebelum a: membership = 0
        if x <= self.a:
            return 0.0
        
        # Antara a dan b: naik linear
        elif x <= self.b:
            return (x - self.a) / (self.b - self.a)
        
        # Antara b dan c: turun linear
        elif x <= self.c:
            return (self.c - x) / (self.c - self.b)
        
        # Setelah c: membership = 0
        else:
            return 0.0
    
    def __call__(self, x):
        """Shortcut untuk membership()"""
        return self.membership(x)
    
    def visualize_ascii(self, x_min=None, x_max=None, width=50):
        """
        Visualisasi fungsi dengan ASCII art
        """
        if x_min is None:
            x_min = self.a - (self.c - self.a) * 0.2
        if x_max is None:
            x_max = self.c + (self.c - self.a) * 0.2
        
        print(f"\n{self.name} Membership Function")
        print(f"Parameters: a={self.a}, b={self.b}, c={self.c}")
        print("-" * (width + 10))
        
        # Buat grid
        for i in range(10, -1, -1):
            y = i / 10
            line = f"{y:.1f} |"
            
            for j in range(width):
                x = x_min + (x_max - x_min) * j / (width - 1)
                membership_val = self.membership(x)
                
                if abs(membership_val - y) < 0.05:
                    line += "*"
                else:
                    line += " "
            
            print(line)
        
        # X-axis
        print("    " + "-" * width)
        print(f"    {x_min:.1f}" + " " * (width - 10) + f"{x_max:.1f}")
    
    def __str__(self):
        return f"Triangular({self.a}, {self.b}, {self.c})"


def demo_basic_triangular():
    """
    Demo: Fungsi triangular dasar
    """
    print("="*60)
    print("DEMO: Triangular Membership Function")
    print("="*60)
    
    # Buat fungsi "HANGAT"
    hangat = TriangularMF(15, 25, 35, name="HANGAT")
    
    print(f"\nFungsi: {hangat}")
    
    # Test beberapa nilai
    print("\nTest nilai:")
    test_values = [10, 15, 20, 25, 30, 35, 40]
    
    for x in test_values:
        membership = hangat(x)
        print(f"  {x}°C → membership = {membership:.2f} ({membership*100:.1f}%)")
    
    # Visualisasi
    hangat.visualize_ascii()


def demo_temperature_sets():
    """
    Demo: Tiga fuzzy sets untuk suhu
    """
    print("\n" + "="*60)
    print("DEMO: Sistem Fuzzy untuk Suhu")
    print("="*60)
    
    # Definisikan 3 fuzzy sets
    dingin = TriangularMF(0, 10, 20, name="DINGIN")
    hangat = TriangularMF(15, 25, 35, name="HANGAT")
    panas = TriangularMF(30, 40, 50, name="PANAS")
    
    print("\nFuzzy Sets:")
    print(f"  1. {dingin}")
    print(f"  2. {hangat}")
    print(f"  3. {panas}")
    
    # Test untuk suhu tertentu
    test_temp = 28
    print(f"\n{'='*60}")
    print(f"Fuzzifikasi untuk suhu: {test_temp}°C")
    print('='*60)
    
    print("\nDerajat keanggotaan:")
    d = dingin(test_temp)
    h = hangat(test_temp)
    p = panas(test_temp)
    
    print(f"  • Dingin: {d:.3f} ({d*100:.1f}%)")
    print(f"  • Hangat: {h:.3f} ({h*100:.1f}%)")
    print(f"  • Panas:  {p:.3f} ({p*100:.1f}%)")
    
    # Visualisasi semua
    print("\n" + "="*60)
    print("VISUALISASI SEMUA FUZZY SETS")
    print("="*60)
    
    for fs in [dingin, hangat, panas]:
        fs.visualize_ascii(0, 50, 50)


def demo_overlapping():
    """
    Demo: Mengapa overlapping penting
    """
    print("\n" + "="*60)
    print("DEMO: Pentingnya Overlapping")
    print("="*60)
    
    print("\nTanpa overlapping (GAP):")
    cold = TriangularMF(0, 10, 20, name="COLD")
    warm = TriangularMF(25, 30, 35, name="WARM")  # GAP: 20-25
    
    test_val = 22
    print(f"\nNilai: {test_val}")
    print(f"  Cold: {cold(test_val):.2f}")
    print(f"  Warm: {warm(test_val):.2f}")
    print("  ⚠️  MASALAH: Tidak termasuk kategori manapun!")
    
    print("\n" + "-"*60)
    print("Dengan overlapping (BAIK):")
    cold2 = TriangularMF(0, 10, 25, name="COLD")
    warm2 = TriangularMF(20, 30, 40, name="WARM")  # Overlap: 20-25
    
    print(f"\nNilai: {test_val}")
    c = cold2(test_val)
    w = warm2(test_val)
    print(f"  Cold: {c:.2f} ({c*100:.1f}%)")
    print(f"  Warm: {w:.2f} ({w*100:.1f}%)")
    print(f"  ✓ Total coverage: {c+w:.2f}")


def exercise_speed_classification():
    """
    LATIHAN: Klasifikasi kecepatan kendaraan
    
    TODO: Buat fuzzy sets untuk:
    - LAMBAT: 0-30 km/h (puncak 15)
    - SEDANG: 20-60 km/h (puncak 40)
    - CEPAT: 50-120 km/h (puncak 85)
    
    Test dengan kecepatan: 10, 25, 45, 70, 100
    """
    print("\n" + "="*60)
    print("LATIHAN: Klasifikasi Kecepatan")
    print("="*60)
    
    # TODO: Definisikan fuzzy sets
    # lambat = TriangularMF(...)
    # sedang = TriangularMF(...)
    # cepat = TriangularMF(...)
    
    # TODO: Test dengan berbagai kecepatan
    # test_speeds = [10, 25, 45, 70, 100]
    # for speed in test_speeds:
    #     print(f"\nKecepatan: {speed} km/h")
    #     print(f"  Lambat: {lambat(speed):.2f}")
    #     print(f"  Sedang: {sedang(speed):.2f}")
    #     print(f"  Cepat:  {cepat(speed):.2f}")
    
    # TODO: Visualisasi
    # lambat.visualize_ascii(0, 120)
    
    pass


def main():
    """Fungsi utama"""
    
    # Demo 1: Dasar
    demo_basic_triangular()
    
    # Demo 2: Multiple sets
    demo_temperature_sets()
    
    # Demo 3: Overlapping
    demo_overlapping()
    
    # Latihan (uncomment setelah mengerjakan)
    # exercise_speed_classification()
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("="*60)
    print("✓ Triangular MF: bentuk segitiga dengan 3 parameter")
    print("✓ Parameter: a (mulai), b (puncak), c (akhir)")
    print("✓ Overlapping: penting untuk coverage penuh")
    print("✓ Sederhana tapi powerful untuk banyak kasus!")
    print("="*60)


if __name__ == "__main__":
    main()


"""
PERTANYAAN REFLEKSI:
-------------------
1. Mengapa kita butuh parameter a, b, c?
2. Apa yang terjadi jika a = b atau b = c?
3. Mengapa overlapping antar fuzzy sets penting?
4. Kapan triangular MF cocok digunakan?

NEXT STEP:
----------
Lanjut ke: 02_trapezoidal.py
Topik: Fungsi keanggotaan trapezoidal
"""
