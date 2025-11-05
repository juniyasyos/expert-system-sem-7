"""
Utilities untuk Expert System dan Fuzzy Logic

Module ini berisi helper functions yang dapat digunakan
di berbagai bagian project.
"""

import math
from typing import List, Dict, Tuple, Callable


# ============================================
# MEMBERSHIP FUNCTIONS
# ============================================

def triangular_mf(x: float, a: float, b: float, c: float) -> float:
    """
    Fungsi keanggotaan triangular
    
    Args:
        x: Input value
        a: Left point (start)
        b: Peak point
        c: Right point (end)
    
    Returns:
        Membership degree [0, 1]
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:  # b < x < c
        return (c - x) / (c - b)


def trapezoidal_mf(x: float, a: float, b: float, c: float, d: float) -> float:
    """
    Fungsi keanggotaan trapezoidal
    
    Args:
        x: Input value
        a: Left start
        b: Left peak
        c: Right peak
        d: Right end
    
    Returns:
        Membership degree [0, 1]
    """
    if x <= a or x >= d:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1.0
    else:  # c < x < d
        return (d - x) / (d - c)


def gaussian_mf(x: float, mean: float, sigma: float) -> float:
    """
    Fungsi keanggotaan Gaussian
    
    Args:
        x: Input value
        mean: Mean (center)
        sigma: Standard deviation (width)
    
    Returns:
        Membership degree [0, 1]
    """
    return math.exp(-0.5 * ((x - mean) / sigma) ** 2)


# ============================================
# FUZZY OPERATIONS (T-norms & T-conorms)
# ============================================

def fuzzy_and_min(a: float, b: float) -> float:
    """Fuzzy AND dengan operator MIN"""
    return min(a, b)


def fuzzy_and_product(a: float, b: float) -> float:
    """Fuzzy AND dengan operator PRODUCT"""
    return a * b


def fuzzy_or_max(a: float, b: float) -> float:
    """Fuzzy OR dengan operator MAX"""
    return max(a, b)


def fuzzy_or_probsum(a: float, b: float) -> float:
    """Fuzzy OR dengan probabilistic sum"""
    return a + b - a * b


def fuzzy_not(a: float) -> float:
    """Fuzzy NOT (complement)"""
    return 1.0 - a


# ============================================
# DEFUZZIFICATION METHODS
# ============================================

def centroid_defuzzification(
    membership_func: Callable[[float], float],
    x_min: float,
    x_max: float,
    steps: int = 100
) -> float:
    """
    Defuzzifikasi dengan metode Centroid (Center of Gravity)
    
    Formula: x* = Σ(μ(x) * x) / Σμ(x)
    
    Args:
        membership_func: Fungsi yang return membership untuk x
        x_min: Batas bawah
        x_max: Batas atas
        steps: Jumlah diskretisasi
    
    Returns:
        Crisp value
    """
    numerator = 0.0
    denominator = 0.0
    step_size = (x_max - x_min) / steps
    
    for i in range(steps):
        x = x_min + i * step_size
        membership = membership_func(x)
        numerator += membership * x
        denominator += membership
    
    if denominator == 0:
        return (x_min + x_max) / 2  # Return midpoint
    
    return numerator / denominator


def bisector_defuzzification(
    membership_func: Callable[[float], float],
    x_min: float,
    x_max: float,
    steps: int = 100
) -> float:
    """
    Defuzzifikasi dengan metode Bisector
    Membagi area di bawah kurva menjadi 2 bagian sama besar
    """
    step_size = (x_max - x_min) / steps
    
    # Hitung total area
    total_area = 0.0
    for i in range(steps):
        x = x_min + i * step_size
        total_area += membership_func(x)
    
    half_area = total_area / 2
    
    # Cari titik yang membagi area
    cumulative = 0.0
    for i in range(steps):
        x = x_min + i * step_size
        cumulative += membership_func(x)
        if cumulative >= half_area:
            return x
    
    return (x_min + x_max) / 2


def mom_defuzzification(
    membership_func: Callable[[float], float],
    x_min: float,
    x_max: float,
    steps: int = 100
) -> float:
    """
    Mean of Maximum (MOM) defuzzification
    Rata-rata dari semua x dengan membership maksimal
    """
    step_size = (x_max - x_min) / steps
    
    # Cari nilai maksimum
    max_membership = 0.0
    for i in range(steps):
        x = x_min + i * step_size
        membership = membership_func(x)
        max_membership = max(max_membership, membership)
    
    # Kumpulkan semua x dengan membership maksimal
    max_x_values = []
    for i in range(steps):
        x = x_min + i * step_size
        if abs(membership_func(x) - max_membership) < 1e-6:
            max_x_values.append(x)
    
    if not max_x_values:
        return (x_min + x_max) / 2
    
    return sum(max_x_values) / len(max_x_values)


# ============================================
# VISUALIZATION HELPERS
# ============================================

def plot_ascii(
    func: Callable[[float], float],
    x_min: float,
    x_max: float,
    width: int = 60,
    height: int = 10,
    title: str = ""
):
    """
    Plot fungsi dengan ASCII art
    
    Args:
        func: Fungsi yang akan diplot
        x_min: Batas kiri
        x_max: Batas kanan
        width: Lebar plot (karakter)
        height: Tinggi plot (baris)
        title: Judul plot
    """
    if title:
        print(f"\n{title}")
    
    print("-" * (width + 10))
    
    for i in range(height, -1, -1):
        y = i / height
        line = f"{y:.1f} |"
        
        for j in range(width):
            x = x_min + (x_max - x_min) * j / (width - 1)
            val = func(x)
            
            if abs(val - y) < (1.0 / height):
                line += "*"
            else:
                line += " "
        
        print(line)
    
    # X-axis
    print("    " + "-" * width)
    print(f"    {x_min:.1f}" + " " * (width - 10) + f"{x_max:.1f}")


# ============================================
# RULE HELPERS
# ============================================

def evaluate_rule_and(conditions: List[float]) -> float:
    """
    Evaluasi kondisi aturan dengan AND (MIN)
    """
    return min(conditions) if conditions else 0.0


def evaluate_rule_or(conditions: List[float]) -> float:
    """
    Evaluasi kondisi aturan dengan OR (MAX)
    """
    return max(conditions) if conditions else 0.0


# ============================================
# AGGREGATION HELPERS
# ============================================

def aggregate_max(memberships: List[float]) -> float:
    """Agregasi dengan MAX (untuk Mamdani)"""
    return max(memberships) if memberships else 0.0


def aggregate_sum(memberships: List[float]) -> float:
    """Agregasi dengan SUM (untuk probabilistic)"""
    return min(1.0, sum(memberships))


# ============================================
# VALIDATION HELPERS
# ============================================

def validate_membership(value: float) -> bool:
    """Cek apakah nilai membership valid [0, 1]"""
    return 0.0 <= value <= 1.0


def normalize_membership(value: float) -> float:
    """Normalisasi nilai ke range [0, 1]"""
    return max(0.0, min(1.0, value))


# ============================================
# CONVERSION HELPERS
# ============================================

def crisp_to_fuzzy_dict(
    value: float,
    fuzzy_sets: Dict[str, Callable[[float], float]]
) -> Dict[str, float]:
    """
    Convert crisp value ke fuzzy memberships
    
    Args:
        value: Crisp input value
        fuzzy_sets: Dict of {label: membership_function}
    
    Returns:
        Dict of {label: membership_degree}
    """
    result = {}
    for label, mf in fuzzy_sets.items():
        result[label] = mf(value)
    return result


# ============================================
# TESTING HELPERS
# ============================================

def test_membership_function(
    mf: Callable[[float], float],
    test_values: List[float],
    name: str = "MF"
):
    """
    Test membership function dengan berbagai nilai
    """
    print(f"\nTesting {name}:")
    print("-" * 40)
    for x in test_values:
        membership = mf(x)
        print(f"  x = {x:6.2f} → μ(x) = {membership:.3f}")


if __name__ == "__main__":
    # Demo utilities
    print("="*60)
    print("UTILITIES DEMO")
    print("="*60)
    
    # Test triangular MF
    print("\n1. Triangular MF (10, 20, 30)")
    test_values = [5, 10, 15, 20, 25, 30, 35]
    for x in test_values:
        y = triangular_mf(x, 10, 20, 30)
        print(f"   x={x:4.1f} → μ={y:.2f}")
    
    # Test fuzzy operations
    print("\n2. Fuzzy Operations")
    a, b = 0.7, 0.4
    print(f"   a = {a}, b = {b}")
    print(f"   AND (min): {fuzzy_and_min(a, b)}")
    print(f"   AND (prod): {fuzzy_and_product(a, b):.2f}")
    print(f"   OR (max): {fuzzy_or_max(a, b)}")
    print(f"   NOT a: {fuzzy_not(a)}")
    
    # Test ASCII plot
    print("\n3. ASCII Plot")
    plot_ascii(
        lambda x: triangular_mf(x, 10, 20, 30),
        0, 40,
        title="Triangular(10, 20, 30)"
    )
    
    print("\n" + "="*60)
    print("Utilities siap digunakan!")
    print("="*60)
