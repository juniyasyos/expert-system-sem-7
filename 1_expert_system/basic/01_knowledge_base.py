"""
LEVEL 1.1: Knowledge Base (Basis Pengetahuan)

Konsep:
--------
Knowledge Base adalah tempat penyimpanan pengetahuan dalam sistem pakar.
Pengetahuan direpresentasikan dalam bentuk FAKTA dan ATURAN.

Fakta: Informasi yang diketahui benar
Aturan: Hubungan logis IF-THEN

Tujuan:
-------
- Memahami cara merepresentasikan pengetahuan
- Membedakan fakta dan aturan
- Menyimpan dan mengakses knowledge base
"""

class KnowledgeBase:
    """
    Knowledge Base sederhana untuk menyimpan fakta dan aturan
    """
    
    def __init__(self):
        self.facts = set()  # Set untuk menyimpan fakta (unique)
        self.rules = []     # List untuk menyimpan aturan
    
    def add_fact(self, fact):
        """Menambahkan fakta ke knowledge base"""
        self.facts.add(fact)
        print(f"✓ Fakta ditambahkan: {fact}")
    
    def add_rule(self, rule_name, conditions, conclusion):
        """
        Menambahkan aturan ke knowledge base
        
        Args:
            rule_name: Nama aturan
            conditions: List kondisi (IF part)
            conclusion: Kesimpulan (THEN part)
        """
        rule = {
            'name': rule_name,
            'conditions': conditions,
            'conclusion': conclusion
        }
        self.rules.append(rule)
        print(f"✓ Aturan ditambahkan: {rule_name}")
    
    def has_fact(self, fact):
        """Mengecek apakah fakta ada di knowledge base"""
        return fact in self.facts
    
    def display_facts(self):
        """Menampilkan semua fakta"""
        print("\n=== FAKTA YANG DIKETAHUI ===")
        if not self.facts:
            print("  (tidak ada fakta)")
        for fact in self.facts:
            print(f"  • {fact}")
    
    def display_rules(self):
        """Menampilkan semua aturan"""
        print("\n=== ATURAN YANG TERSEDIA ===")
        if not self.rules:
            print("  (tidak ada aturan)")
        for rule in self.rules:
            conditions_str = " AND ".join(rule['conditions'])
            print(f"  {rule['name']}:")
            print(f"    IF {conditions_str}")
            print(f"    THEN {rule['conclusion']}")


def demo_animal_knowledge():
    """
    Contoh: Knowledge Base untuk identifikasi hewan
    """
    print("="*60)
    print("DEMO: Knowledge Base - Identifikasi Hewan")
    print("="*60)
    
    # Buat knowledge base
    kb = KnowledgeBase()
    
    # Tambahkan fakta-fakta yang diketahui
    print("\n1. Menambahkan Fakta:")
    print("-" * 40)
    kb.add_fact("memiliki bulu")
    kb.add_fact("memberi susu")
    kb.add_fact("karnivora")
    kb.add_fact("memiliki gigi tajam")
    
    # Tambahkan aturan-aturan
    print("\n2. Menambahkan Aturan:")
    print("-" * 40)
    kb.add_rule(
        "R1: Mamalia",
        ["memiliki bulu", "memberi susu"],
        "adalah mamalia"
    )
    
    kb.add_rule(
        "R2: Karnivora",
        ["karnivora", "memiliki gigi tajam"],
        "memakan daging"
    )
    
    kb.add_rule(
        "R3: Kucing",
        ["adalah mamalia", "memakan daging"],
        "adalah kucing"
    )
    
    # Tampilkan knowledge base
    kb.display_facts()
    kb.display_rules()
    
    # Test pengecekan fakta
    print("\n=== PENGECEKAN FAKTA ===")
    test_facts = ["memiliki bulu", "bisa terbang", "memberi susu"]
    for fact in test_facts:
        result = "✓ ADA" if kb.has_fact(fact) else "✗ TIDAK ADA"
        print(f"  '{fact}': {result}")


def exercise_plant_knowledge():
    """
    LATIHAN: Buat knowledge base untuk identifikasi tanaman
    
    TODO: Lengkapi fungsi ini!
    
    Buatlah knowledge base dengan:
    - Minimal 4 fakta tentang tanaman
    - Minimal 3 aturan untuk klasifikasi tanaman
    
    Contoh fakta:
    - "memiliki daun hijau"
    - "menghasilkan bunga"
    - "memiliki akar serabut"
    
    Contoh aturan:
    - IF "memiliki daun hijau" AND "menghasilkan bunga" THEN "adalah tumbuhan berbunga"
    """
    print("\n" + "="*60)
    print("LATIHAN: Buat Knowledge Base Tanaman")
    print("="*60)
    
    kb = KnowledgeBase()
    
    # TODO: Tambahkan fakta-fakta di sini
    # kb.add_fact("...")
    
    # TODO: Tambahkan aturan-aturan di sini
    # kb.add_rule("...", [...], "...")
    
    # Tampilkan hasil
    kb.display_facts()
    kb.display_rules()


def main():
    """Fungsi utama"""
    
    # Jalankan demo
    demo_animal_knowledge()
    
    # Jalankan latihan (uncomment setelah mengerjakan)
    # exercise_plant_knowledge()
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("="*60)
    print("✓ Knowledge Base = Fakta + Aturan")
    print("✓ Fakta = Informasi yang diketahui")
    print("✓ Aturan = Hubungan IF-THEN")
    print("✓ Ini adalah fondasi sistem pakar!")
    print("="*60)


if __name__ == "__main__":
    main()


"""
PERTANYAAN REFLEKSI:
-------------------
1. Apa perbedaan antara fakta dan aturan?
2. Mengapa kita menggunakan set() untuk fakta?
3. Bisakah satu aturan memiliki lebih dari satu kondisi?
4. Bagaimana cara merepresentasikan pengetahuan kompleks?

NEXT STEP:
----------
Lanjut ke: 02_simple_rules.py
Topik: Evaluasi aturan IF-THEN sederhana
"""
