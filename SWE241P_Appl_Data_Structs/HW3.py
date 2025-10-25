#Algorithms HW3 
#--------------------------------------------------------------------------------

# Given an array of strings Strings, 
# group the words that are anagrams to each other. You can return the answer in any order. 
#implement the function  groupAnagram(List<String> strings) 
# that takes a list of strings and returns a list of lists of strings

#Task 1
# -----------------------------------------

def mergesort(arr):
    #base case: a list of 0 or 1 items
    if len(arr) <=1:
        return arr
    
    #split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #recursively sort each half
    left_sorted = mergesort(left_half)
    right_sorted = mergesort(right_half)

    #merge the two sorted halves
    return merge(left_sorted,right_sorted)
   
def merge(left,right):
    result = []
    i = j = 0

    # compare elements and merge the two halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    #add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ============================================
# || Quicksort Methods                      ||      
# ============================================
def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# ------------------------------------------------------


wordlist =  ["bucket","rat","mango","tango","ogtan","tar",'tuckeb']

    # var in parametrs is used for selecting the sorting method, with 1 being merge sort and 2 being quicksort
def groupanagram(words: list[str],var) -> list[list[str]]:
    sortMethod =  var

        # keys[i] = the sorted “root” form (the anagram signature)
        # result[i] = the list of original words that match that signature
    result = []             
    keys = []               

    for word in words:
        # Convert to list of ASCII numbers
        formatted = [ord(x) for x in word]
        match sortMethod:
            case 1:
               
                formatted =mergesort(formatted)
                
            case 2:
               
                print("Quicksort selected")
                quickSort(formatted, 0, len(formatted) - 1)
             


        # Convert sorted numbers back to string key
        formatted = ''.join(chr(x) for x in formatted)

        # Check if this key already has a bucket
        if formatted in keys:
            idx = keys.index(formatted)
            result[idx].append(word)
        else:
            # Create new bucket for this key
            keys.append(formatted)
            result.append([word])

    print(result)
    return result

print(groupanagram(wordlist,2) ==  groupanagram(wordlist,1))
