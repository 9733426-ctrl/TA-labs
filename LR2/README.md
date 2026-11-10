def merge_sort_iterative(a):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            j += 2 * i
        i *= 2
    return a, comparisons, assignments

def merge(a, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2
    it1 = 0
    it2 = 0
    k = left
    assignments += 3
    while it1 < n1 and it2 < n2:
        comparisons += 1
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        assignments += 2
        k += 1
        assignments += 1
    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 2
    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 2
    return comparisons, assignments

def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    mid = len(arr) // 2
    assignments += 1
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    merged_arr, c_merge, a_merge = merge_recursive_helper(left_half, right_half)
    comparisons += c_merge
    assignments += a_merge
    return merged_arr, comparisons, assignments, recursive_calls

def merge_recursive_helper(left, right):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 1
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 1
    return merged_arr, comparisons, assignments

def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1
        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    return comparisons, assignments, recursive_calls

def partition(a, l, r):
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    i = l - 1
    j = r + 1
    assignments += 2
    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1
        if i >= j:
            return j, comparisons, assignments
        a[i], a[j] = a[j], a[i]
        assignments += 3

if __name__ == "__main__":
    my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
    
    print("--- Сортування злиттям (Ітеративне) ---")
    sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Порівнянь: {comps}, Присвоювань: {assigs}\n")

    print("--- Сортування злиттям (Рекурсивне) ---")
    sorted_list_r, comps_r, assigs_r, rec_calls_r = merge_sort_recursive(my_list.copy())
    print("Відсортований список:", sorted_list_r)
    print(f"Порівнянь: {comps_r}, Присвоювань: {assigs_r}, Викликів: {rec_calls_r}\n")

    print("--- Швидке сортування (Хоара) ---")
    qs_list = my_list.copy()
    comps_q, assigs_q, rec_calls_q = quicksort(qs_list, 0, len(qs_list) - 1)
    print("Відсортований список:", qs_list)
    print(f"Порівнянь: {comps_q}, Присвоювань: {assigs_q}, Викликів: {rec_calls_q}\n")
