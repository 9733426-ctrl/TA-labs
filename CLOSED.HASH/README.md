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
    return get_key_sum(key) % m

def multiplication_hash(key: str, m: int = 16) -> int:
    k = get_key_sum(key)
    return math.floor(m * ((k * A) % 1))

def build_closed_hash_table(words: list, m: int, primary_hash_func) -> list:
    hash_table = [None] * m
    for word in words:
        start_address = primary_hash_func(word, m)
        for i in range(m):
            address = (start_address + i) % m
            if hash_table[address] is None:
                hash_table[address] = word
                break
        else:
            print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")
    return hash_table

def display_hash_table(table: list, title: str):
    print(f"\n--- {title} (Відкрита адресація, M={len(table)}) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")

if __name__ == "__main__":
    closed_table_div = build_closed_hash_table(WORDS, 13, division_hash)
    display_hash_table(closed_table_div, "Хеш-таблиця: Метод ділення")

    closed_table_mult = build_closed_hash_table(WORDS, 16, multiplication_hash)
    display_hash_table(closed_table_mult, "Хеш-таблиця: Метод множення")
