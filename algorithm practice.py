# def reversing_k(array, k):
#     # Normalizing k
#     k = k % len(array)
    
#     # Reversing the first part of the array
#     array = array[::-1]
    
#     # Moving forst element to k position 
#     array[:k] = array[:k][::-1]
    
#     array[k:] = array[k:][::-1]
    
#     return array

# print(reversing_k([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
# print(reversing_k([1, 2, 3], 4))              # Output: [3, 1, 2]
# print(reversing_k([1, 2], 1))                 # Output: [2, 1]
# print(reversing_k([1], 10))                   # Output: [1]



def first_duplicate(arr):
    # Create an empty set to track elements seen so far
    seen = set()
    
    for char in arr:
        if char in seen:
            return char  # Found the first duplicate
        seen.add(char)
    
    return -1  



print(first_duplicate([2, 5, 1, 2, 3, 5, 1, 2, 4]))  # Output: 2
print(first_duplicate([1, 2, 3, 4]))               # Output: -1
print(first_duplicate([3, 3, 3]))                  # Output: 3
print(first_duplicate([]))                         # Output: -1

    




    