import time
import matplotlib.pyplot as plt

# ==========================================
# 1. Метод послідовного пошуку (Груба сила)
# ==========================================
def brute_force_search(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)
            
    return occurrences

# ==========================================
# 2. Алгоритм Кнута-Морріса-Пратта (КМП)
# ==========================================
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    occurrences = []
    
    i = 0  # індекс для text
    j = 0  # індекс для pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return occurrences

# ==========================================
# 3. Допоміжні функції для тестування
# ==========================================
def generate_worst_case_string(n, m):
    """
    Генерує найгірший випадок для алгоритму грубої сили.
    Текст: "AAAA...AAAA"
    Шаблон: "AAAA...AAAB"
    """
    text = "A" * n
    pattern = "A" * (m - 1) + "B"
    return text, pattern

def measure_time(search_func, text, pattern):
    start_time = time.time()
    search_func(text, pattern)
    end_time = time.time()
    return end_time - start_time

def compare_search_algorithms():
    # Масив розмірів тексту для тестування (від 10 тисяч до 500 тисяч символів)
    input_sizes = [10000, 50000, 100000, 200000, 500000]
    pattern_size = 1000  # Фіксована довжина підрядка
    
    bf_times = []
    kmp_times = []
    
    print("=== Розпочинаємо тестування алгоритмів (Найгірший випадок) ===\n")
    
    for size in input_sizes:
        text, pattern = generate_worst_case_string(size, pattern_size)
        
        # Вимірюємо час
        bf_time = measure_time(brute_force_search, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        
        bf_times.append(bf_time)
        kmp_times.append(kmp_time)
        
        # Вивід результатів у консоль (Трасування)
        print(f"Розмір тексту (N): {size:<7} | Довжина підрядка (M): {pattern_size}")
        print(f"Час Brute Force: {bf_time:.6f} сек")
        print(f"Час KMP:         {kmp_time:.6f} сек")
        print("-" * 50)
        
    # ==========================================
    # 4. Візуалізація результатів (Matplotlib)
    # ==========================================
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, bf_times, label="Послідовний пошук (Груба сила)", marker='o', color='orange', linewidth=2)
    plt.plot(input_sizes, kmp_times, label="КМП-алгоритм", marker='o', color='blue', linewidth=2)
    
    plt.title("Порівняння алгоритмів пошуку підрядка (Найгірший випадок)", fontsize=14)
    plt.xlabel("Довжина тексту (Кількість символів N)", fontsize=12)
    plt.ylabel("Час виконання (секунди)", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_search_algorithms()
