"""
LEVEL 3.1: Mamdani Fuzzy Inference System - Introduction

Konsep:
--------
Mamdani Fuzzy Inference System (FIS) adalah metode inferensi fuzzy
yang menggunakan fuzzy sets untuk output.

Tahapan Mamdani:
1. FUZZIFIKASI: Crisp input → Fuzzy sets
2. RULE EVALUATION: Evaluasi aturan fuzzy
3. AGREGASI: Gabungkan hasil semua aturan
4. DEFUZZIFIKASI: Fuzzy output → Crisp output

Contoh Aplikasi:
- Kontrol AC (input: suhu, kelembaban → output: kecepatan kipas)
- Tip calculator (input: service, food → output: tip)
- Decision making systems

Tujuan:
-------
- Memahami alur lengkap sistem Mamdani
- Implementasi sederhana dari nol
- Menguasai setiap tahapan
"""

class TriangularMF:
    """Triangular Membership Function (untuk referensi)"""
    
    def __init__(self, a, b, c, name=""):
        self.a, self.b, self.c = a, b, c
        self.name = name
    
    def membership(self, x):
        if x <= self.a:
            return 0.0
        elif x <= self.b:
            return (x - self.a) / (self.b - self.a)
        elif x <= self.c:
            return (self.c - x) / (self.c - self.b)
        else:
            return 0.0
    
    def __call__(self, x):
        return self.membership(x)


class MamdaniSystem:
    """
    Simple Mamdani Fuzzy Inference System
    """
    
    def __init__(self):
        self.input_vars = {}   # Input variables dan fuzzy sets
        self.output_vars = {}  # Output variables dan fuzzy sets
        self.rules = []        # Aturan fuzzy
    
    def add_input(self, var_name, fuzzy_sets):
        """
        Tambahkan variabel input dengan fuzzy sets
        
        Args:
            var_name: Nama variabel (misal: "temperature")
            fuzzy_sets: Dict of {label: MembershipFunction}
        """
        self.input_vars[var_name] = fuzzy_sets
    
    def add_output(self, var_name, fuzzy_sets):
        """Tambahkan variabel output dengan fuzzy sets"""
        self.output_vars[var_name] = fuzzy_sets
    
    def add_rule(self, antecedents, consequent):
        """
        Tambahkan aturan fuzzy
        
        Args:
            antecedents: Dict {var_name: fuzzy_label}
            consequent: Dict {var_name: fuzzy_label}
        """
        rule = {
            'antecedent': antecedents,
            'consequent': consequent
        }
        self.rules.append(rule)
    
    def fuzzify(self, var_name, value):
        """
        STEP 1: Fuzzifikasi - ubah crisp value ke fuzzy
        
        Returns:
            Dict {label: membership_degree}
        """
        if var_name not in self.input_vars:
            raise ValueError(f"Unknown variable: {var_name}")
        
        fuzzy_sets = self.input_vars[var_name]
        result = {}
        
        for label, mf in fuzzy_sets.items():
            result[label] = mf(value)
        
        return result
    
    def evaluate_rules(self, inputs):
        """
        STEP 2: Evaluasi aturan
        
        Args:
            inputs: Dict {var_name: fuzzy_values}
        
        Returns:
            List of (consequent, firing_strength)
        """
        results = []
        
        for rule in self.rules:
            # Hitung firing strength (min dari semua antecedent)
            firing_strengths = []
            
            for var_name, fuzzy_label in rule['antecedent'].items():
                if var_name in inputs and fuzzy_label in inputs[var_name]:
                    firing_strengths.append(inputs[var_name][fuzzy_label])
                else:
                    firing_strengths.append(0.0)
            
            # Gunakan MIN untuk AND operator
            firing_strength = min(firing_strengths) if firing_strengths else 0.0
            
            if firing_strength > 0:
                results.append((rule['consequent'], firing_strength))
        
        return results
    
    def aggregate(self, fired_rules, output_var):
        """
        STEP 3: Agregasi hasil aturan dengan MAX
        
        Args:
            fired_rules: List of (consequent, firing_strength)
            output_var: Nama variabel output
        
        Returns:
            Dict {label: max_firing_strength}
        """
        aggregated = {}
        
        for consequent, strength in fired_rules:
            if output_var in consequent:
                label = consequent[output_var]
                
                if label not in aggregated:
                    aggregated[label] = strength
                else:
                    # Gunakan MAX untuk agregasi
                    aggregated[label] = max(aggregated[label], strength)
        
        return aggregated
    
    def defuzzify_centroid(self, aggregated, output_var, x_min=0, x_max=100, steps=100):
        """
        STEP 4: Defuzzifikasi dengan metode Centroid (COG)
        
        Formula: x* = Σ(μ(x) * x) / Σμ(x)
        """
        if not aggregated:
            return 0.0
        
        output_sets = self.output_vars[output_var]
        
        numerator = 0.0
        denominator = 0.0
        step_size = (x_max - x_min) / steps
        
        for i in range(steps):
            x = x_min + i * step_size
            
            # Hitung membership untuk x (ambil max dari semua aggregated sets)
            membership = 0.0
            for label, firing_strength in aggregated.items():
                if label in output_sets:
                    # Clipping: ambil min antara firing strength dan MF value
                    mf_value = output_sets[label](x)
                    clipped = min(firing_strength, mf_value)
                    membership = max(membership, clipped)
            
            numerator += membership * x
            denominator += membership
        
        if denominator == 0:
            return 0.0
        
        return numerator / denominator
    
    def infer(self, input_values, output_var, verbose=False):
        """
        Lakukan inferensi lengkap (all steps)
        
        Args:
            input_values: Dict {var_name: crisp_value}
            output_var: Nama variabel output
            verbose: Print detail proses
        
        Returns:
            Crisp output value
        """
        if verbose:
            print("\n" + "="*60)
            print("MAMDANI INFERENCE PROCESS")
            print("="*60)
        
        # Step 1: Fuzzifikasi
        if verbose:
            print("\n1. FUZZIFIKASI")
            print("-"*60)
        
        fuzzy_inputs = {}
        for var_name, value in input_values.items():
            fuzzy_inputs[var_name] = self.fuzzify(var_name, value)
            
            if verbose:
                print(f"\n{var_name} = {value}")
                for label, degree in fuzzy_inputs[var_name].items():
                    if degree > 0:
                        print(f"  {label}: {degree:.3f}")
        
        # Step 2: Evaluasi aturan
        if verbose:
            print("\n2. EVALUASI ATURAN")
            print("-"*60)
        
        fired_rules = self.evaluate_rules(fuzzy_inputs)
        
        if verbose:
            for i, (consequent, strength) in enumerate(fired_rules, 1):
                print(f"Rule {i}: {consequent} → strength = {strength:.3f}")
        
        # Step 3: Agregasi
        if verbose:
            print("\n3. AGREGASI")
            print("-"*60)
        
        aggregated = self.aggregate(fired_rules, output_var)
        
        if verbose:
            for label, strength in aggregated.items():
                print(f"  {label}: {strength:.3f}")
        
        # Step 4: Defuzzifikasi
        if verbose:
            print("\n4. DEFUZZIFIKASI (Centroid)")
            print("-"*60)
        
        crisp_output = self.defuzzify_centroid(aggregated, output_var)
        
        if verbose:
            print(f"  Crisp output: {crisp_output:.2f}")
            print("="*60)
        
        return crisp_output


def demo_simple_tip_system():
    """
    Demo: Sistem tip restoran sederhana
    
    Input: service quality (0-10)
    Output: tip percentage (0-30)
    """
    print("="*60)
    print("DEMO: Simple Tipping System")
    print("="*60)
    
    # Buat sistem
    fis = MamdaniSystem()
    
    # Input variable: service
    print("\nMendefinisikan fuzzy sets...")
    fis.add_input("service", {
        "poor": TriangularMF(0, 0, 5, "poor"),
        "good": TriangularMF(0, 5, 10, "good"),
        "excellent": TriangularMF(5, 10, 10, "excellent")
    })
    
    # Output variable: tip
    fis.add_output("tip", {
        "low": TriangularMF(0, 0, 15, "low"),
        "medium": TriangularMF(0, 15, 30, "medium"),
        "high": TriangularMF(15, 30, 30, "high")
    })
    
    # Aturan fuzzy
    print("Menambahkan aturan...")
    fis.add_rule({"service": "poor"}, {"tip": "low"})
    fis.add_rule({"service": "good"}, {"tip": "medium"})
    fis.add_rule({"service": "excellent"}, {"tip": "high"})
    
    # Test berbagai input
    print("\n" + "="*60)
    print("TEST CASES")
    print("="*60)
    
    test_cases = [2, 5, 7, 10]
    
    for service_quality in test_cases:
        tip = fis.infer({"service": service_quality}, "tip", verbose=False)
        print(f"\nService quality: {service_quality}/10 → Tip: {tip:.1f}%")
    
    # Detail untuk satu case
    print("\n" + "="*60)
    print("DETAIL PROSES (Service = 7)")
    print("="*60)
    fis.infer({"service": 7}, "tip", verbose=True)


def main():
    """Fungsi utama"""
    
    demo_simple_tip_system()
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("="*60)
    print("✓ Mamdani FIS: 4 tahap (Fuzzify → Evaluate → Aggregate → Defuzzify)")
    print("✓ Fuzzifikasi: Crisp → Fuzzy")
    print("✓ Evaluasi: MIN untuk AND, MAX untuk agregasi")
    print("✓ Defuzzifikasi: Centroid (COG) paling populer")
    print("✓ Output: Fuzzy set (berbeda dengan Sugeno!)")
    print("="*60)


if __name__ == "__main__":
    main()


"""
PERTANYAAN REFLEKSI:
-------------------
1. Mengapa Mamdani menggunakan fuzzy sets untuk output?
2. Apa fungsi dari setiap tahapan (4 steps)?
3. Mengapa kita gunakan MIN untuk AND dan MAX untuk agregasi?
4. Apa kelebihan dan kekurangan Mamdani?

NEXT STEP:
----------
Lanjut ke: 02_rule_evaluation.py
Topik: Detail evaluasi aturan fuzzy
"""
