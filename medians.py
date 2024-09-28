"""
This Python script implements the deterministic "Median of Medians" algorithm
for finding the k-th smallest element in an array. The algorithm guarantees
a worst-case time complexity of O(n) by selecting an optimal pivot.
The code includes detailed comments and explanations for better clarity.
"""

def partition(arr, low, high, pivot_index):
    """
    Partition the array around the chosen pivot index.
    Moves all elements smaller than the pivot to its left
    and all elements greater than the pivot to its right.
    """
    pivot_value = arr[pivot_index]  # Get the pivot value
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move the pivot to the end
    store_index = low  # This will keep track of the boundary between smaller and larger elements
    
    # Iterate through the array to rearrange elements
    for i in range(low, high):
        if arr[i] < pivot_value:  # If element is smaller than pivot, swap it
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1  # Increment the boundary
    
    arr[store_index], arr[high] = arr[high], arr[store_index]  # Move the pivot to its final place
    return store_index  # Return the final position of the pivot

def select_median_of_medians(arr, low, high, k):
    """
    Recursively selects the k-th smallest element using the Median of Medians algorithm.
    This function divides the array into groups of 5, finds the median of each group,
    and then recursively finds the median of the medians.
    """
    if low == high:  # Base case: if the list contains only one element, return it
        return arr[low]
    
    # Step 1: Divide the array into groups of 5 and find the medians of these groups
    medians = []  # List to store the medians of groups
    for i in range(low, high + 1, 5):
        group = sorted(arr[i: min(i + 5, high + 1)])  # Sort each group of 5 elements
        medians.append(group[len(group) // 2])  # Find the median of the group and add it to medians
    
    # Step 2: Find the median of the medians
    if len(medians) == 1:  # If there's only one median, use it as the pivot
        median_of_medians = medians[0]
    else:
        median_of_medians = select_median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)
    
    # Find the actual index of the median of medians in the original array
    pivot_index = arr.index(median_of_medians, low, high + 1)
    
    # Step 3: Partition the array using the median of medians as the pivot
    pivot_index = partition(arr, low, high, pivot_index)
    
    # Step 4: Recursively select the k-th smallest element
    if k == pivot_index:  # If the pivot is the k-th element, return it
        return arr[k]
    elif k < pivot_index:  # If k-th element is on the left side, recursively select from the left
        return select_median_of_medians(arr, low, pivot_index - 1, k)
    else:  # If k-th element is on the right side, recursively select from the right
        return select_median_of_medians(arr, pivot_index + 1, high, k)

def deterministic_select(arr, k):
    """
    This function acts as a wrapper to call the Median of Medians algorithm.
    It adjusts the k index to zero-based and initiates the selection process.
    """
    return select_median_of_medians(arr, 0, len(arr) - 1, k - 1)  # Adjust k for zero-based indexing

# Example usage
arr = [12, 3, 5, 7, 19, 26, 4, 9]  # Example array
k = 4  # We want the 4th smallest element
print(f"The {k}th smallest element using deterministic implementation is {deterministic_select(arr, k)}")



"""
This Python script implements a randomized Quickselect algorithm for finding the k-th smallest element
in an array. The algorithm has expected linear time complexity due to its random pivot selection.
It handles edge cases like arrays with duplicate elements and provides line-by-line comments for clarity.
"""

import random

def partition_random(arr, low, high):
    """
    Randomly selects a pivot from the array and partitions it into elements smaller
    and larger than the pivot. This is similar to the partition step in quicksort.
    """
    pivot_index = random.randint(low, high)  # Choose a random pivot index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move the pivot to the end
    pivot = arr[high]  # Set pivot to the value at the high index
    i = low - 1  # Initialize the smaller element boundary
    
    # Rearrange elements based on the pivot value
    for j in range(low, high):
        if arr[j] <= pivot:  # If current element is smaller or equal to the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements to maintain order
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot in its correct position
    return i + 1  # Return the final pivot position

def randomized_select(arr, low, high, k):
    """
    Selects the k-th smallest element using the Randomized Quickselect algorithm.
    This algorithm randomly selects a pivot and recursively selects elements based on the pivot position.
    """
    if low == high:  # Base case: if there is only one element, return it
        return arr[low]
    
    pivot_index = partition_random(arr, low, high)  # Partition the array around a random pivot
    
    if pivot_index == k:  # If pivot is the k-th element, return it
        return arr[pivot_index]
    elif k < pivot_index:  # If k-th element is on the left, recurse on the left partition
        return randomized_select(arr, low, pivot_index - 1, k)
    else:  # If k-th element is on the right, recurse on the right partition
        return randomized_select(arr, pivot_index + 1, high, k)

def randomized_quickselect(arr, k):
    """
    Wrapper function to initiate the Randomized Quickselect algorithm.
    Adjusts k for zero-based indexing and calls the recursive selection function.
    """
    return randomized_select(arr, 0, len(arr) - 1, k - 1)  # Adjust k to zero-based indexing

# Example usage
arr = [12, 3, 5, 7, 19, 26, 4, 9]  # Example array
k = 4  # We want the 4th smallest element
print(f"The {k}th smallest element using randomized implementation is {randomized_quickselect(arr, k)}")


