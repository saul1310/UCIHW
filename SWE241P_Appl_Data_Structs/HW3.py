import time
import tracemalloc
import random
import string
import matplotlib.pyplot as plt

# ------------------- Sorting Algorithms -------------------

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_sorted = mergesort(arr[:mid])
    right_sorted = mergesort(arr[mid:])
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# ------------------- Group Anagrams with Timing & Memory -------------------

def groupanagram(words: list[str], sortMethod: int) -> tuple[list[list[str]], float, float]:
    result = []
    keys = []

    tracemalloc.start()
    start_time = time.perf_counter()

    for word in words:
        formatted = [ord(x) for x in word]
        if sortMethod == 1:
            formatted = mergesort(formatted)
        elif sortMethod == 2:
            quickSort(formatted, 0, len(formatted) - 1)

        formatted_key = ''.join(chr(x) for x in formatted)
        if formatted_key in keys:
            idx = keys.index(formatted_key)
            result[idx].append(word)
        else:
            keys.append(formatted_key)
            result.append([word])

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    peak_memory_kb = peak / 1024

    return result, elapsed_time, peak_memory_kb

# ------------------- Test Data Generation -------------------

def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_word_list(num_words, word_length_range=(3,8)):
    return [random_word(random.randint(*word_length_range)) for _ in range(num_words)]

# ------------------- Benchmarking -------------------

input_sizes = [100, 500, 1000, 2000, 4000]
merge_times = []
quick_times = []
merge_memory = []
quick_memory = []

for size in input_sizes:
    test_list = generate_word_list(size)
    
    _, t_merge, m_merge = groupanagram(test_list, 1)
    _, t_quick, m_quick = groupanagram(test_list, 2)
    
    merge_times.append(t_merge)
    quick_times.append(t_quick)
    merge_memory.append(m_merge)
    quick_memory.append(m_quick)

# ------------------- Plotting -------------------

plt.figure(figsize=(12,5))

# Time plot
plt.subplot(1,2,1)
plt.plot(input_sizes, merge_times, marker='o', label='MergeSort')
plt.plot(input_sizes, quick_times, marker='x', label='QuickSort')
plt.xlabel("Number of words")
plt.ylabel("Time (seconds)")
plt.title("Time vs Input Size")
plt.legend()
plt.grid(True)

# Memory plot
plt.subplot(1,2,2)
plt.plot(input_sizes, merge_memory, marker='o', label='MergeSort')
plt.plot(input_sizes, quick_memory, marker='x', label='QuickSort')
plt.xlabel("Number of words")
plt.ylabel("Peak Memory (KB)")
plt.title("Memory Usage vs Input Size")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
