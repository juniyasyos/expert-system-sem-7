"""
QUICK START GUIDE
Expert System & Fuzzy Logic Learning Project

Panduan cepat untuk memulai pembelajaran
"""

def print_welcome():
    """Tampilkan pesan selamat datang"""
    print("="*70)
    print(" " * 10 + "🎓 EXPERT SYSTEM & FUZZY LOGIC 🎓")
    print(" " * 15 + "Learning Project - Quick Start")
    print("="*70)


def print_prerequisites():
    """Cek prerequisites"""
    import sys
    
    print("\n📋 PREREQUISITES CHECK")
    print("-"*70)
    
    # Check Python version
    version = sys.version_info
    print(f"✓ Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("  ✓ Version OK (Python 3.7+)")
    else:
        print("  ✗ PERINGATAN: Disarankan Python 3.7+")
    
    # Check modules
    required_modules = ['math', 'collections', 'typing', 'json']
    print("\n✓ Required modules:")
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✓ {module}")
        except ImportError:
            print(f"  ✗ {module} (MISSING)")
    
    print("\n✓ Setup complete! Tidak perlu install package tambahan.")


def print_learning_path():
    """Tampilkan learning path"""
    print("\n" + "="*70)
    print("🗺️  LEARNING PATH - Ikuti urutan ini!")
    print("="*70)
    
    path = [
        ("LEVEL 1", "Expert System Basics", "1_expert_system/basic/", [
            "01_knowledge_base.py - Basis pengetahuan",
            "02_simple_rules.py - Aturan IF-THEN",
            "03_fact_matching.py - Pattern matching"
        ]),
        ("LEVEL 2", "Fuzzy Logic Fundamentals", "2_fuzzy_logic/", [
            "fuzzification/01_crisp_vs_fuzzy.py",
            "membership_functions/01_triangular.py",
            "fuzzy_operations/01_basic_operations.py"
        ]),
        ("LEVEL 3", "Mamdani Method", "3_mamdani/", [
            "core/01_mamdani_intro.py",
            "defuzzification/01_centroid.py",
            "examples/tipping_problem.py"
        ]),
        ("LEVEL 4", "Sugeno Method", "4_sugeno/", [
            "core/01_sugeno_intro.py",
            "core/02_zero_order.py",
            "core/03_first_order.py"
        ]),
        ("LEVEL 5", "Complete Projects", "5_projects/", [
            "hvac_control/ - Sistem kontrol AC",
            "traffic_light/ - Lampu lalu lintas",
            "medical_diagnosis/ - Diagnosis medis"
        ])
    ]
    
    for level, title, folder, files in path:
        print(f"\n{level}: {title}")
        print(f"{'─'*70}")
        print(f"📁 Lokasi: {folder}")
        print(f"📚 Materi:")
        for i, file in enumerate(files, 1):
            print(f"   {i}. {file}")


def print_quick_commands():
    """Tampilkan perintah-perintah cepat"""
    print("\n" + "="*70)
    print("⚡ QUICK COMMANDS")
    print("="*70)
    
    commands = [
        ("Mulai Level 1", "python 1_expert_system/basic/01_knowledge_base.py"),
        ("Test Fuzzy Logic", "python 2_fuzzy_logic/fuzzification/01_crisp_vs_fuzzy.py"),
        ("Demo Mamdani", "python 3_mamdani/core/01_mamdani_intro.py"),
        ("Cek Utilities", "python utils/fuzzy_utils.py"),
    ]
    
    print("\nUntuk memulai pembelajaran:")
    for desc, cmd in commands:
        print(f"\n  {desc}:")
        print(f"    $ {cmd}")


def print_tips():
    """Tampilkan tips pembelajaran"""
    print("\n" + "="*70)
    print("💡 TIPS PEMBELAJARAN")
    print("="*70)
    
    tips = [
        "Jangan skip - ikuti urutan dari Level 1 sampai 5",
        "Jalankan setiap file dan amati outputnya",
        "Kerjakan semua latihan (exercise) di setiap file",
        "Modifikasi kode untuk eksperimen",
        "Buat catatan tentang konsep yang dipelajari",
        "Gunakan print() untuk debug dan pemahaman",
        "Visualisasi konsep di kertas jika perlu",
        "Buat contoh kasus sendiri setelah paham",
        "Jangan ragu untuk kembali ke materi sebelumnya",
        "Take your time - pemahaman lebih penting dari kecepatan"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"  {i:2d}. {tip}")


def print_resources():
    """Tampilkan resources tambahan"""
    print("\n" + "="*70)
    print("📚 RESOURCES")
    print("="*70)
    
    print("\n📖 Dokumentasi Project:")
    print("  • README.md - Overview lengkap")
    print("  • requirements.txt - Dependencies (none required!)")
    print("  • Setiap folder punya README.md sendiri")
    
    print("\n🛠️  Utilities:")
    print("  • utils/fuzzy_utils.py - Helper functions")
    print("    (membership functions, operators, plotting)")
    
    print("\n❓ Troubleshooting:")
    print("  • Jika ada error: baca pesan error dengan teliti")
    print("  • Cek apakah Python 3.7+")
    print("  • Pastikan di folder yang benar")
    print("  • Lihat contoh di file yang sama")


def print_folder_structure():
    """Tampilkan struktur folder"""
    print("\n" + "="*70)
    print("📂 STRUKTUR FOLDER")
    print("="*70)
    
    structure = """
expert-system/
├── README.md                          ← BACA INI DULU!
├── QUICKSTART.py                      ← File ini
├── requirements.txt                   
├── .gitignore                         
│
├── 1_expert_system/                   ← LEVEL 1: Mulai di sini
│   ├── README.md
│   ├── basic/                         ← START HERE!
│   ├── forward_chaining/
│   ├── backward_chaining/
│   └── examples/
│
├── 2_fuzzy_logic/                     ← LEVEL 2: Fuzzy basics
│   ├── README.md
│   ├── fuzzification/
│   ├── membership_functions/
│   ├── fuzzy_operations/
│   └── examples/
│
├── 3_mamdani/                         ← LEVEL 3: Metode Mamdani
│   ├── README.md
│   ├── core/
│   ├── inference/
│   ├── defuzzification/
│   └── examples/
│
├── 4_sugeno/                          ← LEVEL 4: Metode Sugeno
│   ├── README.md
│   ├── core/
│   ├── inference/
│   └── examples/
│
├── 5_projects/                        ← LEVEL 5: Project lengkap
│   ├── README.md
│   ├── hvac_control/
│   ├── traffic_light/
│   └── medical_diagnosis/
│
└── utils/                             ← Helper functions
    └── fuzzy_utils.py
    """
    
    print(structure)


def print_next_steps():
    """Tampilkan langkah selanjutnya"""
    print("\n" + "="*70)
    print("🚀 NEXT STEPS - Mulai Sekarang!")
    print("="*70)
    
    print("\n1️⃣  Baca README.md utama")
    print("    $ cat README.md")
    
    print("\n2️⃣  Mulai Level 1")
    print("    $ cd 1_expert_system/basic")
    print("    $ python 01_knowledge_base.py")
    
    print("\n3️⃣  Lanjutkan secara berurutan")
    print("    Follow the numbers: 01, 02, 03, ...")
    
    print("\n4️⃣  Kerjakan latihan")
    print("    Setiap file punya exercise - kerjakan!")
    
    print("\n5️⃣  Eksperimen!")
    print("    Ubah parameter, buat contoh sendiri")


def main():
    """Fungsi utama"""
    print_welcome()
    print_prerequisites()
    print_learning_path()
    print_quick_commands()
    print_folder_structure()
    print_tips()
    print_resources()
    print_next_steps()
    
    print("\n" + "="*70)
    print(" " * 20 + "🎯 SELAMAT BELAJAR! 🎯")
    print(" " * 10 + "Enjoy the journey of understanding!")
    print("="*70)
    print()


if __name__ == "__main__":
    main()


"""
CATATAN PENTING:
---------------

1. JANGAN TERBURU-BURU
   Pahami setiap konsep sebelum lanjut

2. HANDS-ON ADALAH KUNCI
   Jangan hanya baca - jalankan dan modifikasi kode

3. BUAT CATATAN
   Document pembelajaran Anda

4. EKSPERIMEN
   Coba hal-hal di luar tutorial

5. NIKMATI PROSESNYA
   Learning should be fun!

Happy Learning! 🚀
"""
