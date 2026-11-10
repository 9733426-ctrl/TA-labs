import math

A = (math.sqrt(5) - 1) / 2
WORDS = ["ЛЮДИНА", "БЕЗ", "ДРУЗІВ", "ЯК", "ДЕРЕВО", "БЕЗ", "КОРІННЯ"]

LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10, 
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 
    'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29, 'Щ': 30, 
    'Ь': 31, 'Ю': 32, 'Я': 33
}

def get_key_sum(key: str) -> int:
    sum_of_positions = 0
    for char in key.upper():
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    return sum_of_positions

def division_hash(key: str, m: int = 13) -> int:
    k = get_key_sum(key)
    return k % m

def multiplication_hash(key: str, m: int = 16) -> int:
    k = get_key_sum(key)
    fractional_part = (k * A) % 1
    return math.floor(m * fractional_part)

def build_open_hash_table(words: list, m: int, hash_func) -> list:
    hash_table = [[] for _ in range(m)]
    for word in words:
        address = hash_func(word, m)
        hash_table[address].append(word)
    return hash_table

def display_hash_table(table: list, title: str):
    print(f"\n--- {title} (Таблиця M={len(table)}) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

if __name__ == "__main__":
    open_table_div = build_open_hash_table(WORDS, 13, division_hash)
    display_hash_table(open_table_div, "Результат відкритого хешування: Метод ділення")

    open_table_mult = build_open_hash_table(WORDS, 16, multiplication_hash)
    display_hash_table(open_table_mult, "Результат відкритого хешування: Метод множення")
