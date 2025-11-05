"""
LEVEL 1.2: Simple Rules (Aturan Sederhana)

Konsep:
--------
Aturan dalam sistem pakar mengikuti pola IF-THEN:
  IF kondisi1 AND kondisi2 ... THEN kesimpulan

Rule evaluation: Proses memeriksa apakah kondisi terpenuhi,
lalu mengeksekusi kesimpulan.

Tujuan:
-------
- Memahami struktur aturan IF-THEN
- Implementasi evaluasi aturan
- Menangani AND/OR dalam kondisi
"""

class Rule:
    """
    Representasi aturan IF-THEN
    """
    
    def __init__(self, name, conditions, conclusion, operator="AND"):
        """
        Args:
            name: Nama aturan
            conditions: List kondisi
            conclusion: Kesimpulan
            operator: "AND" atau "OR"
        """
        self.name = name
        self.conditions = conditions
        self.conclusion = conclusion
        self.operator = operator
    
    def evaluate(self, facts):
        """
        Evaluasi aturan berdasarkan fakta yang ada
        
        Returns:
            True jika aturan terpenuhi, False jika tidak
        """
        if self.operator == "AND":
            # Semua kondisi harus terpenuhi
            return all(condition in facts for condition in self.conditions)
        elif self.operator == "OR":
            # Minimal satu kondisi harus terpenuhi
            return any(condition in facts for condition in self.conditions)
        else:
            raise ValueError(f"Operator tidak dikenal: {self.operator}")
    
    def can_fire(self, facts):
        """
        Cek apakah aturan dapat dieksekusi
        Sama dengan evaluate, tapi lebih ekspresif
        """
        return self.evaluate(facts)
    
    def fire(self, facts):
        """
        Eksekusi aturan: tambahkan kesimpulan ke fakta
        
        Returns:
            True jika berhasil dieksekusi, False jika tidak
        """
        if self.can_fire(facts):
            if self.conclusion not in facts:
                facts.add(self.conclusion)
                print(f"  🔥 {self.name} FIRED! → '{self.conclusion}'")
                return True
            else:
                print(f"  ⊗ {self.name} (kesimpulan sudah ada)")
                return False
        else:
            print(f"  ✗ {self.name} (kondisi tidak terpenuhi)")
            return False
    
    def __str__(self):
        conditions_str = f" {self.operator} ".join(self.conditions)
        return f"{self.name}: IF {conditions_str} THEN {self.conclusion}"


def demo_simple_rules():
    """
    Demo: Evaluasi aturan sederhana
    """
    print("="*60)
    print("DEMO: Evaluasi Aturan Sederhana")
    print("="*60)
    
    # Fakta awal
    facts = {"hujan", "membawa payung"}
    
    print("\nFakta awal:")
    for fact in facts:
        print(f"  • {fact}")
    
    # Buat aturan dengan operator AND
    print("\n" + "-"*60)
    print("1. ATURAN dengan AND:")
    print("-"*60)
    
    rule1 = Rule(
        "R1",
        ["hujan", "membawa payung"],
        "tetap kering",
        operator="AND"
    )
    print(f"  {rule1}")
    
    print("\n  Evaluasi:")
    rule1.fire(facts)
    
    # Buat aturan dengan operator OR
    print("\n" + "-"*60)
    print("2. ATURAN dengan OR:")
    print("-"*60)
    
    rule2 = Rule(
        "R2",
        ["hujan", "badai"],
        "cuaca buruk",
        operator="OR"
    )
    print(f"  {rule2}")
    
    print("\n  Evaluasi:")
    rule2.fire(facts)
    
    # Aturan yang tidak terpenuhi
    print("\n" + "-"*60)
    print("3. ATURAN yang TIDAK TERPENUHI:")
    print("-"*60)
    
    rule3 = Rule(
        "R3",
        ["cerah", "panas"],
        "cuaca bagus",
        operator="AND"
    )
    print(f"  {rule3}")
    
    print("\n  Evaluasi:")
    rule3.fire(facts)
    
    # Fakta akhir
    print("\n" + "="*60)
    print("Fakta setelah evaluasi:")
    for fact in facts:
        print(f"  • {fact}")


def demo_chaining_rules():
    """
    Demo: Rantai aturan (rule chaining)
    Output dari satu aturan menjadi input untuk aturan lain
    """
    print("\n" + "="*60)
    print("DEMO: Rantai Aturan (Rule Chaining)")
    print("="*60)
    
    facts = set()
    
    # Definisikan aturan-aturan
    rules = [
        Rule("R1", ["pagi"], "matahari terbit", "AND"),
        Rule("R2", ["matahari terbit"], "terang", "AND"),
        Rule("R3", ["terang", "mata terbuka"], "bisa melihat", "AND"),
    ]
    
    print("\nAturan yang tersedia:")
    for rule in rules:
        print(f"  {rule}")
    
    # Tambahkan fakta awal
    print("\n" + "-"*60)
    print("Fakta awal:")
    facts.add("pagi")
    facts.add("mata terbuka")
    for fact in facts:
        print(f"  • {fact}")
    
    # Evaluasi aturan satu per satu
    print("\n" + "-"*60)
    print("Proses Inferensi:")
    print("-"*60)
    
    for i, rule in enumerate(rules, 1):
        print(f"\nLangkah {i}: Evaluasi {rule.name}")
        rule.fire(facts)
    
    # Hasil akhir
    print("\n" + "="*60)
    print("Fakta akhir:")
    for fact in facts:
        print(f"  • {fact}")
    print("="*60)


def exercise_weather_rules():
    """
    LATIHAN: Buat sistem aturan untuk prediksi cuaca
    
    TODO: Lengkapi fungsi ini!
    
    Buat aturan-aturan untuk:
    1. Jika "mendung" AND "angin kencang" → "akan hujan"
    2. Jika "akan hujan" OR "gerimis" → "bawa payung"
    3. Jika "panas" AND "cerah" → "gunakan sunscreen"
    4. Aturan custom Anda sendiri!
    """
    print("\n" + "="*60)
    print("LATIHAN: Sistem Aturan Cuaca")
    print("="*60)
    
    facts = {"mendung", "angin kencang", "panas"}
    
    print("\nFakta awal:")
    for fact in facts:
        print(f"  • {fact}")
    
    # TODO: Buat aturan-aturan di sini
    rules = [
        # Rule("R1", [...], "...", "AND"),
        # Rule("R2", [...], "...", "OR"),
        # Tambahkan lebih banyak!
    ]
    
    # TODO: Evaluasi setiap aturan
    print("\n" + "-"*60)
    print("Evaluasi Aturan:")
    print("-"*60)
    # for rule in rules:
    #     rule.fire(facts)
    
    print("\n" + "="*60)
    print("Fakta akhir:")
    for fact in facts:
        print(f"  • {fact}")


def main():
    """Fungsi utama"""
    
    # Demo 1: Aturan sederhana
    demo_simple_rules()
    
    # Demo 2: Rantai aturan
    demo_chaining_rules()
    
    # Latihan (uncomment setelah mengerjakan)
    # exercise_weather_rules()
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("="*60)
    print("✓ Aturan IF-THEN adalah dasar reasoning")
    print("✓ Operator AND: semua kondisi harus terpenuhi")
    print("✓ Operator OR: minimal satu kondisi terpenuhi")
    print("✓ Rule chaining: output → input aturan lain")
    print("="*60)


if __name__ == "__main__":
    main()


"""
PERTANYAAN REFLEKSI:
-------------------
1. Apa bedanya AND dan OR dalam evaluasi aturan?
2. Bagaimana rule chaining bisa menghasilkan kesimpulan kompleks?
3. Apa yang terjadi jika ada circular dependency antar aturan?
4. Kapan sebaiknya menggunakan AND vs OR?

NEXT STEP:
----------
Lanjut ke: 03_fact_matching.py
Topik: Pattern matching dan unification
"""
