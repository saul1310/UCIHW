#Algorithms HW3 
#--------------------------------------------------------------------------------

# Given an array of strings Strings, 
# group the words that are anagrams to each other. You can return the answer in any order. 
#implement the function  groupAnagram(List<String> strings) 
# that takes a list of strings and returns a list of lists of strings

#Task 1
# -----------------------------------------

def mergesort(input):
    pass

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


input =  ["bucket","rat","mango","tango","ogtan","tar"]
def groupanagram(input:list) -> list[str]:

    #turn word into sortable form(numbers) 
    for word in input:
        formatted = [ord(x) for x in word + ',']
        formatted.pop(-1) # remove the trailing comma lol

        # call your prefered sorting algo on the numbers
        quickSort(formatted, 0, len(formatted) - 1)
        #turn the sorted numbers back into a string, now the root word anagram
        formatted = [chr(x) for x in formatted]
        formatted="".join(formatted)
        
        print(formatted)


groupanagram(input) 