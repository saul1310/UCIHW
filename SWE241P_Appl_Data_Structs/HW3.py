import time
import tracemalloc
import random
import string
import matplotlib.pyplot as plt
#Sources:
# - LeetCode Problem 49: Group Anagrams
# - Standard merge sort and quick sort algorithm pseudocode

# ------------------- Sorting Algorithms -------------------
  
       
    # Time complexity- Worst: O(n log n)
#     Merge Sort splits the array in half recursively (logn levels) 
# and merges all elements at each level (O(n) work), giving O(n log n) time.
    # Space Complexity: O(n)  (due to temporary arrays created during merge)
def mergesort(arr):
    # If the array has more than one element, it needs to be split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Recursively sort the left half
    left_sorted = mergesort(arr[:mid])
    # Recursively sort the right half
    right_sorted = mergesort(arr[mid:])
    # Merge the two sorted halves together
    return merge(left_sorted, right_sorted)

# Time Complexity: O(n)
# Space Complexity: O(n)
def merge(left, right):
    result = [] # Final merged sorted list
    i = j = 0  # Pointers for left and right lists
    # Compare elements from both lists and append the smaller one
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


"""Quick sort section"""
# --------------------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
#Helper function for quicksort that swaps two elements
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# Time Complexity: O(n)
# Space Complexity: O(1)
#rearranges the elemnts of an array such that -->
    # all the elements smaller than the pivot come beofre it
    #all of the elements larger than the pivot come after it
    #the pivot ends up in the final sorted position
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

# Time Complexity:
#     - Best: O(n log n)
#     - Average: O(n log n)
#     - Worst: O(n^2)  (when pivot choices are poor)
# Space Complexity:
#     - O(log n) on average (due to recursion stack)

#     - O(n) in the worst case
#start with an entire array. call partition left and right of the current subarray being handled.
def quickSort(arr, low, high):
    # Check if the current subarray has more than one element.
    # (If low >= high, the subarray is size 0 or 1 — already sorted.)
    if low < high:
        # Partition the array around a pivot element.
        # After this call, all elements smaller than the pivot are on its left,
        # and all greater elements are on its right.
        # The function returns the final index position of the pivot (pi).
        pi = partition(arr, low, high)
        # Recursively apply QuickSort to the left subarray (elements before the pivot).
        # This sorts all elements smaller than the pivot
        quickSort(arr, low, pi - 1)
        # Recursively apply QuickSort to the right subarray (elements after the pivot).
        # This sorts all elements greater than the pivot.
        quickSort(arr, pi + 1, high)

# ------------------- Group Anagrams with Timing & Memory -------------------
#    Time Complexity:
#         Let:
#             n = number of words
#             k = average length of each word
#         Sorting each word: O(k log k)
#         Total sorting for all words: O(n * k log k)
#         Grouping and lookup (using list.index): O(n^2) in worst case (since keys.index is linear)
#         Overall: O(n^2 + n * k log k)
#     Space Complexity:
#         O(n * k) for storing formatted keys and result lists
#         + sorting overhead (O(k) for MergeSort, O(log k) for QuickSort)
def groupanagram(words: list[str], sortMethod: int) -> tuple[list[list[str]], float, float]:
    result = [] # List to store groups of anagrams (or words with the same sorted key)
    keys = []# List to store the sorted "key" for each group

    #helper function for benchmark data
    tracemalloc.start()
    start_time = time.perf_counter()

    for word in words:
        #turns the word into a list of ints
        formatted = [ord(x) for x in word]
        #sorts list of ints
        if sortMethod == 1:
            formatted = mergesort(formatted)
        elif sortMethod == 2:
            quickSort(formatted, 0, len(formatted) - 1)
        #turns ints back into characters, forming root word anagram
        formatted_key = ''.join(chr(x) for x in formatted)
        #if its already in our list-->
        if formatted_key in keys:
            #add our word to the correct bucket
            idx = keys.index(formatted_key)
            result[idx].append(word)
        #if its not in our list already
        else:
            #add a new one
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
print("\n=== FUNCTIONAL CORRECTNESS TEST ===\n")
example_input = ["bucket", "rat", "mango", "tango", "ogtan", "tar"]
expected_output = [["bucket"], ["rat", "tar"], ["mango"], ["tango", "ogtan"]]

# Test using MergeSort
result_merge, t1, m1 = groupanagram(example_input, 1)
print("MergeSort result:", result_merge)
print("Matches expected?", sorted([sorted(g) for g in result_merge]) == sorted([sorted(g) for g in expected_output]))
print(f"Time: {t1:.6f}s | Memory: {m1:.2f} KB\n")

# Test using QuickSort
result_quick, t2, m2 = groupanagram(example_input, 2)
print("QuickSort result:", result_quick)
print("Matches expected?", sorted([sorted(g) for g in result_quick]) == sorted([sorted(g) for g in expected_output]))
print(f"Time: {t2:.6f}s | Memory: {m2:.2f} KB\n")

result, _, _ = groupanagram(example_input, 1)
print("Example test (MergeSort):", result)

result, _, _ = groupanagram(example_input, 2)
print("Example test (QuickSort):", result)
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
