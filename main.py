def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n, counters):
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        
        counters['comparisons'] += 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
            
        counters['comparisons'] += 1
        if arr[k] >= arr[j]:
            break
            
        swap(arr, k, j)
        counters['assignments'] += 3
        k = j

def heapsort(arr):
    n = len(arr)
    counters = {'comparisons': 0, 'assignments': 0}
    print(f"Початковий масив: {arr}\n")
    
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range((n // 2) - 1, -1, -1):
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        sink(arr, i, n, counters)
        
    print(f"\nМасив після побудови купи: {arr}\n")
    
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        counters['assignments'] += 3
        
        print(f"Розмір купи зменшився до {i}. Відновлюємо властивості купи.")
        sink(arr, 0, i, counters)
        print(f"Масив на поточному кроці: {arr}\n")
        
    return arr, counters

if __name__ == "__main__":
    A = [41, 68, 67, 10, 7, 69, 95, 43, 98]
    sorted_A, counters = heapsort(A.copy())
    print(f"Відсортований масив: {sorted_A}")
    print(f"Кількість порівнянь: {counters['comparisons']}")
    print(f"Кількість присвоювань: {counters['assignments']}")
