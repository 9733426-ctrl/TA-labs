import time
import random
import matplotlib.pyplot as plt

# ==========================================
# 1. Алгоритми пошуку
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
    if m == 0: return []
    lps = compute_lps(pattern)
    occurrences = []
    i = 0
    j = 0
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

def measure_time(search_func, text, pattern):
    start = time.time()
    search_func(text, pattern)
    return time.time() - start

# ==========================================
# 2. ПУНКТ 5: Трасування (Вивід у консоль)
# ==========================================
print("=== Трасування: Перевірка коректності роботи ===")
test_text = "ABABDABACDABABCABAB"
test_pattern = "ABABCABAB"
print(f"Текст:  {test_text}")
print(f"Шаблон: {test_pattern}")
print(f"Знайдені індекси (Груба сила): {brute_force_search(test_text, test_pattern)}")
print(f"Знайдені індекси (КМП):        {kmp_search(test_text, test_pattern)}")
print("-" * 50)

# ==========================================
# 3. ПУНКТ 6: Візуалізація на різних вхідних даних (Стовпчаста діаграма)
# ==========================================
N_fixed = 100000
M_fixed = 1000

# Найгірший випадок
t_worst = "A" * N_fixed
p_worst = "A" * (M_fixed - 1) + "B"

# Випадковий текст (Average case)
t_rand = ''.join(random.choice("ABC") for _ in range(N_fixed))
p_rand = t_rand[-M_fixed:]

# Найкращий випадок (патерн на початку)
t_best = "B" * M_fixed + "A" * (N_fixed - M_fixed)
p_best = "B" * M_fixed

cases = ["Найкращий випадок", "Випадковий текст", "Найгірший випадок"]
bf_bars = [measure_time(brute_force_search, t_best, p_best),
           measure_time(brute_force_search, t_rand, p_rand),
           measure_time(brute_force_search, t_worst, p_worst)]

kmp_bars = [measure_time(kmp_search, t_best, p_best),
            measure_time(kmp_search, t_rand, p_rand),
            measure_time(kmp_search, t_worst, p_worst)]

x = range(len(cases))
plt.figure(figsize=(10, 5))
plt.bar([pos - 0.2 for pos in x], bf_bars, 0.4, label='Груба сила', color='orange')
plt.bar([pos + 0.2 for pos in x], kmp_bars, 0.4, label='КМП-алгоритм', color='blue')
plt.xticks(x, cases)
plt.ylabel('Час виконання (секунди)')
plt.title(f'Пункт 6: Перевірка роботи на різних вхідних даних (N={N_fixed})')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# ==========================================
# 4. ПУНКТ 7: Візуалізація результатів складності (Лінійний графік)
# ==========================================
input_sizes = [10000, 50000, 100000, 200000]
bf_lines = []
kmp_lines = []

for size in input_sizes:
    txt = "A" * size
    pat = "A" * (M_fixed - 1) + "B"
    bf_lines.append(measure_time(brute_force_search, txt, pat))
    kmp_lines.append(measure_time(kmp_search, txt, pat))

plt.figure(figsize=(10, 5))
plt.plot(input_sizes, bf_lines, label="Груба сила O(N*M)", marker='o', color='orange', linewidth=2)
plt.plot(input_sizes, kmp_lines, label="КМП O(N+M)", marker='o', color='blue', linewidth=2)
plt.title("Пункт 7: Залежність часу виконання від довжини тексту")
plt.xlabel("Довжина тексту N")
plt.ylabel("Час виконання (секунди)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Виводимо обидва графіки
plt.show()
