"""
LEVEL 1.3: Fact Matching (Pencocokan Fakta)

Konsep:
--------
Fact matching adalah proses mencocokkan fakta dengan pola dalam aturan.
Ini penting untuk sistem pakar yang lebih kompleks dengan variabel dan parameter.

Pattern: "?x adalah mamalia"
Fact: "kucing adalah mamalia"
Match: ?x = kucing

Tujuan:
-------
- Memahami pattern matching
- Implementasi variable binding
- Membuat aturan yang lebih fleksibel
"""

class Fact:
    """
    Representasi fakta dengan predicate dan arguments
    
    Contoh: Fact("is", ["kucing", "mamalia"])
    Artinya: "kucing is mamalia" atau "kucing adalah mamalia"
    """
    
    def __init__(self, predicate, arguments):
        """
        Args:
            predicate: Predikat/hubungan (misal: "is", "has", "eats")
            arguments: List argumen
        """
        self.predicate = predicate
        self.arguments = arguments if isinstance(arguments, list) else [arguments]
    
    def __eq__(self, other):
        if not isinstance(other, Fact):
            return False
        return (self.predicate == other.predicate and 
                self.arguments == other.arguments)
    
    def __hash__(self):
        return hash((self.predicate, tuple(self.arguments)))
    
    def __str__(self):
        args_str = ", ".join(str(arg) for arg in self.arguments)
        return f"{self.predicate}({args_str})"
    
    def matches(self, pattern, bindings=None):
        """
        Cek apakah fakta ini cocok dengan pola
        
        Args:
            pattern: Pola fakta (bisa mengandung variabel)
            bindings: Dictionary binding variabel
        
        Returns:
            Dictionary bindings jika cocok, None jika tidak
        """
        if bindings is None:
            bindings = {}
        
        # Predikat harus sama
        if self.predicate != pattern.predicate:
            return None
        
        # Jumlah argumen harus sama
        if len(self.arguments) != len(pattern.arguments):
            return None
        
        # Cek setiap argumen
        new_bindings = bindings.copy()
        for fact_arg, pattern_arg in zip(self.arguments, pattern.arguments):
            # Jika pattern_arg adalah variabel (dimulai dengan ?)
            if isinstance(pattern_arg, str) and pattern_arg.startswith("?"):
                var_name = pattern_arg
                
                # Jika variabel sudah ada binding
                if var_name in new_bindings:
                    # Cek apakah konsisten
                    if new_bindings[var_name] != fact_arg:
                        return None
                else:
                    # Tambah binding baru
                    new_bindings[var_name] = fact_arg
            else:
                # Bukan variabel, harus exact match
                if fact_arg != pattern_arg:
                    return None
        
        return new_bindings


class FactBase:
    """
    Database fakta dengan kemampuan pattern matching
    """
    
    def __init__(self):
        self.facts = set()
    
    def add(self, fact):
        """Tambahkan fakta"""
        self.facts.add(fact)
    
    def query(self, pattern):
        """
        Query fakta berdasarkan pola
        
        Args:
            pattern: Pola fakta yang dicari
        
        Returns:
            List of (fact, bindings) yang cocok
        """
        results = []
        for fact in self.facts:
            bindings = fact.matches(pattern)
            if bindings is not None:
                results.append((fact, bindings))
        return results
    
    def display(self):
        """Tampilkan semua fakta"""
        print("\nFakta dalam database:")
        if not self.facts:
            print("  (kosong)")
        for fact in self.facts:
            print(f"  • {fact}")


def demo_simple_matching():
    """
    Demo: Pattern matching sederhana
    """
    print("="*60)
    print("DEMO: Pattern Matching Sederhana")
    print("="*60)
    
    # Buat fact base
    fb = FactBase()
    
    # Tambahkan fakta-fakta
    print("\n1. Menambahkan Fakta:")
    print("-"*60)
    
    facts_to_add = [
        Fact("is", ["kucing", "mamalia"]),
        Fact("is", ["anjing", "mamalia"]),
        Fact("is", ["burung", "aves"]),
        Fact("has", ["kucing", "ekor"]),
        Fact("has", ["anjing", "ekor"]),
    ]
    
    for fact in facts_to_add:
        fb.add(fact)
        print(f"  ✓ {fact}")
    
    fb.display()
    
    # Query 1: Cari semua mamalia
    print("\n" + "="*60)
    print("2. QUERY: Siapa yang adalah mamalia?")
    print("   Pattern: is(?x, mamalia)")
    print("-"*60)
    
    pattern1 = Fact("is", ["?x", "mamalia"])
    results1 = fb.query(pattern1)
    
    print(f"  Ditemukan {len(results1)} hasil:")
    for fact, bindings in results1:
        print(f"    • {fact}")
        print(f"      Bindings: {bindings}")
    
    # Query 2: Cek fakta spesifik
    print("\n" + "="*60)
    print("3. QUERY: Apakah kucing punya ekor?")
    print("   Pattern: has(kucing, ekor)")
    print("-"*60)
    
    pattern2 = Fact("has", ["kucing", "ekor"])
    results2 = fb.query(pattern2)
    
    if results2:
        print("  ✓ YA, kucing punya ekor")
    else:
        print("  ✗ TIDAK, tidak ditemukan")
    
    # Query 3: Cari yang punya ekor
    print("\n" + "="*60)
    print("4. QUERY: Siapa yang punya ekor?")
    print("   Pattern: has(?x, ekor)")
    print("-"*60)
    
    pattern3 = Fact("has", ["?x", "ekor"])
    results3 = fb.query(pattern3)
    
    print(f"  Ditemukan {len(results3)} hasil:")
    for fact, bindings in results3:
        animal = bindings["?x"]
        print(f"    • {animal}")


def demo_complex_matching():
    """
    Demo: Pattern matching kompleks dengan multiple variables
    """
    print("\n" + "="*60)
    print("DEMO: Pattern Matching Kompleks")
    print("="*60)
    
    fb = FactBase()
    
    # Tambahkan relasi yang lebih kompleks
    print("\n1. Menambahkan Fakta Relasional:")
    print("-"*60)
    
    facts = [
        Fact("eats", ["kucing", "ikan"]),
        Fact("eats", ["anjing", "daging"]),
        Fact("eats", ["kelinci", "wortel"]),
        Fact("lives_in", ["kucing", "rumah"]),
        Fact("lives_in", ["anjing", "rumah"]),
        Fact("lives_in", ["kelinci", "kandang"]),
    ]
    
    for fact in facts:
        fb.add(fact)
        print(f"  ✓ {fact}")
    
    # Query dengan dua variabel
    print("\n" + "="*60)
    print("2. QUERY: Siapa makan apa?")
    print("   Pattern: eats(?animal, ?food)")
    print("-"*60)
    
    pattern = Fact("eats", ["?animal", "?food"])
    results = fb.query(pattern)
    
    for fact, bindings in results:
        animal = bindings["?animal"]
        food = bindings["?food"]
        print(f"  • {animal} makan {food}")


def exercise_family_tree():
    """
    LATIHAN: Buat sistem family tree dengan pattern matching
    
    TODO: Lengkapi fungsi ini!
    
    Buat fakta-fakta untuk family tree:
    - parent(John, Mary)  -> John adalah parent Mary
    - parent(Mary, Tom)   -> Mary adalah parent Tom
    - male(John), female(Mary), dll
    
    Kemudian query:
    - Siapa anak dari John?
    - Siapa yang laki-laki?
    - Siapa parent dari Tom?
    """
    print("\n" + "="*60)
    print("LATIHAN: Family Tree dengan Pattern Matching")
    print("="*60)
    
    fb = FactBase()
    
    # TODO: Tambahkan fakta-fakta
    # fb.add(Fact("parent", ["John", "Mary"]))
    # fb.add(Fact("male", ["John"]))
    # ... tambahkan lebih banyak
    
    # TODO: Lakukan query
    # print("\nSiapa anak dari John?")
    # pattern = Fact("parent", ["John", "?child"])
    # results = fb.query(pattern)
    # for fact, bindings in results:
    #     print(f"  • {bindings['?child']}")
    
    pass


def main():
    """Fungsi utama"""
    
    # Demo 1: Matching sederhana
    demo_simple_matching()
    
    # Demo 2: Matching kompleks
    demo_complex_matching()
    
    # Latihan (uncomment setelah mengerjakan)
    # exercise_family_tree()
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("="*60)
    print("✓ Pattern matching = mencocokkan pola dengan fakta")
    print("✓ Variabel (?x) = placeholder untuk nilai apapun")
    print("✓ Binding = pemetaan variabel ke nilai")
    print("✓ Ini dasar untuk query dalam sistem pakar!")
    print("="*60)


if __name__ == "__main__":
    main()


"""
PERTANYAAN REFLEKSI:
-------------------
1. Apa bedanya pattern dengan fakta biasa?
2. Bagaimana variable binding bekerja?
3. Bisakah satu pattern menghasilkan multiple matches?
4. Apa keuntungan menggunakan pattern matching?

NEXT STEP:
----------
Lanjut ke: 1_expert_system/forward_chaining/
Topik: Forward chaining inference
"""
