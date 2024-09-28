"""
This Python script implements two algorithms to find the k-th smallest element in an array:
1. Deterministic "Median of Medians" algorithm, which guarantees O(n) time complexity in the worst case.
2. Randomized Quickselect algorithm, which has O(n) expected time complexity.

The script also empirically compares their performance on different input sizes and distributions
(random, sorted, reverse-sorted), and generates a graph to show the results, which is saved as an image.
It also prints the results for review.
"""

import random
import time
import matplotlib.pyplot as plt

# Deterministic Algorithm (Median of Medians)

def partition(arr, low, high, pivot_index):
    """
    Partition the array around the chosen pivot index.
    Moves all elements smaller than the pivot to its left
    and all elements greater than the pivot to its right.
    """
    pivot_value = arr[pivot_index]  # Get the pivot value
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move the pivot to the end
    store_index = low  # Initialize the boundary between smaller and larger elements
    
    # Iterate through the array to rearrange elements
    for i in range(low, high):
        if arr[i] < pivot_value:  # If the current element is smaller than the pivot, swap it
            arr[i], arr[store_index] = arr[store_index], arr[i]  # Swap with the boundary element
            store_index += 1  # Move the boundary up
    
    arr[store_index], arr[high] = arr[high], arr[store_index]  # Move the pivot to its final place
    return store_index  # Return the final pivot position

def select_median_of_medians(arr, low, high, k):
    """
    Recursively selects the k-th smallest element using the Median of Medians algorithm.
    Divides the array into groups of 5, finds the median of each group,
    and then recursively finds the median of the medians.
    """
    if low == high:  # Base case: if there's only one element, return it
        return arr[low]
    
    # Step 1: Divide the array into groups of 5 and find the median of each group
    medians = []  # List to store the medians of groups
    for i in range(low, high + 1, 5):
        group = sorted(arr[i: min(i + 5, high + 1)])  # Sort each group of 5 elements
        medians.append(group[len(group) // 2])  # Add the median of the group to the medians list

    # Step 2: Find the median of the medians recursively
    if len(medians) == 1:  # If there's only one median, use it as the pivot
        median_of_medians = medians[0]
    else:
        median_of_medians = select_median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)

    # Step 3: Find the index of the median of medians in the original array
    pivot_index = arr.index(median_of_medians, low, high + 1)
    
    # Step 4: Partition the array around the median of medians
    pivot_index = partition(arr, low, high, pivot_index)

    # Step 5: Recursively select the k-th smallest element
    if k == pivot_index:  # If the pivot is the k-th element, return it
        return arr[k]
    elif k < pivot_index:  # If k-th element is on the left, recurse on the left
        return select_median_of_medians(arr, low, pivot_index - 1, k)
    else:  # If k-th element is on the right, recurse on the right
        return select_median_of_medians(arr, pivot_index + 1, high, k)

def deterministic_select(arr, k):
    """
    Wrapper function to call the Median of Medians algorithm.
    It adjusts the k index to zero-based and initiates the selection process.
    """
    return select_median_of_medians(arr, 0, len(arr) - 1, k - 1)  # Adjust k for zero-based indexing


# Randomized Algorithm (Quickselect)

def partition_random(arr, low, high):
    """
    Randomly selects a pivot and partitions the array around it.
    Moves elements smaller than the pivot to the left and larger to the right.
    """
    pivot_index = random.randint(low, high)  # Choose a random pivot index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move the pivot to the end
    pivot = arr[high]  # Set the pivot to the value at the high index
    i = low - 1  # Initialize the boundary for smaller elements
    
    # Rearrange elements based on the pivot
    for j in range(low, high):
        if arr[j] <= pivot:  # If the element is smaller than or equal to the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap it with the boundary element
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot in its final position
    return i + 1  # Return the final pivot position

def randomized_select(arr, low, high, k):
    """
    Recursively selects the k-th smallest element using the Randomized Quickselect algorithm.
    Randomly selects a pivot and partitions based on the pivot.
    """
    if low == high:  # Base case: if there's only one element, return it
        return arr[low]
    
    # Partition the array using a randomly chosen pivot
    pivot_index = partition_random(arr, low, high)
    
    # Recursively select the k-th smallest element
    if pivot_index == k:  # If the pivot is the k-th element, return it
        return arr[pivot_index]
    elif k < pivot_index:  # If k-th element is on the left, recurse on the left
        return randomized_select(arr, low, pivot_index - 1, k)
    else:  # If k-th element is on the right, recurse on the right
        return randomized_select(arr, pivot_index + 1, high, k)

def randomized_quickselect(arr, k):
    """
    Wrapper function to initiate the Randomized Quickselect algorithm.
    Adjusts k for zero-based indexing and calls the recursive function.
    """
    return randomized_select(arr, 0, len(arr) - 1, k - 1)  # Adjust k to zero-based indexing


# Print results for initial example
arr = [12, 3, 5, 7, 19, 26, 4, 9]  # Example array
k = 4  # We want the 4th smallest element
print(f"The {k}th smallest element using deterministic implementation is {deterministic_select(arr, k)}")
print(f"The {k}th smallest element using randomized implementation is {randomized_quickselect(arr, k)}")


# Empirical Comparison

def measure_time(func, arr, k):
    """
    Measures the execution time of the provided function (deterministic or randomized).
    """
    start_time = time.time()  # Start the timer
    func(arr.copy(), k)  # Call the selection function (use a copy of the array to avoid side effects)
    end_time = time.time()  # Stop the timer
    return end_time - start_time  # Return the time taken for execution

def run_comparison():
    """
    Compares the running times of the deterministic and randomized algorithms.
    Tests on random, sorted, and reverse-sorted arrays with increasing input sizes.
    """
    input_sizes = [100, 1000, 5000, 10000, 20000]  # Different input sizes for testing
    deterministic_times = []
    randomized_times = []

    for size in input_sizes:
        arr_random = random.sample(range(size * 2), size)  # Generate a random array
        arr_sorted = sorted(arr_random)  # Generate a sorted version of the array
        arr_reverse_sorted = arr_sorted[::-1]  # Generate a reverse-sorted version of the array
        k = size // 2  # Find the median (middle element)

        # Measure time for deterministic algorithm on random, sorted, and reverse-sorted arrays
        deterministic_times.append([
            measure_time(deterministic_select, arr_random, k),
            measure_time(deterministic_select, arr_sorted, k),
            measure_time(deterministic_select, arr_reverse_sorted, k)
        ])

        # Measure time for randomized algorithm on random, sorted, and reverse-sorted arrays
        randomized_times.append([
            measure_time(randomized_quickselect, arr_random, k),
            measure_time(randomized_quickselect, arr_sorted, k),
            measure_time(randomized_quickselect, arr_reverse_sorted, k)
        ])

    # Print out the timing results for each case
    print("\nComparison of Deterministic and Randomized Algorithms:\n")
    for i, size in enumerate(input_sizes):
        print(f"Input Size: {size}")
        print(f"Deterministic - Random: {deterministic_times[i][0]:.6f}s, Sorted: {deterministic_times[i][1]:.6f}s, Reverse: {deterministic_times[i][2]:.6f}s")
        print(f"Randomized - Random: {randomized_times[i][0]:.6f}s, Sorted: {randomized_times[i][1]:.6f}s, Reverse: {randomized_times[i][2]:.6f}s")
        print()

    return input_sizes, deterministic_times, randomized_times


def plot_comparison():
    """
    Plots the comparison of the running times of the two algorithms.
    Saves the plot as an image file and prints the results to the console.
    """
    input_sizes, deterministic_times, randomized_times = run_comparison()

    # Extract times for different distributions
    random_deterministic = [times[0] for times in deterministic_times]
    sorted_deterministic = [times[1] for times in deterministic_times]
    reverse_deterministic = [times[2] for times in deterministic_times]

    random_randomized = [times[0] for times in randomized_times]
    sorted_randomized = [times[1] for times in randomized_times]
    reverse_randomized = [times[2] for times in randomized_times]

    # Plot the results
    plt.figure(figsize=(10, 6))
    
    # Random array
    plt.plot(input_sizes, random_deterministic, label="Deterministic (Random Array)", marker="o")
    plt.plot(input_sizes, random_randomized, label="Randomized (Random Array)", marker="o")

    # Sorted array
    plt.plot(input_sizes, sorted_deterministic, label="Deterministic (Sorted Array)", linestyle="--", marker="x")
    plt.plot(input_sizes, sorted_randomized, label="Randomized (Sorted Array)", linestyle="--", marker="x")

    # Reverse sorted array
    plt.plot(input_sizes, reverse_deterministic, label="Deterministic (Reverse-Sorted Array)", linestyle=":", marker="s")
    plt.plot(input_sizes, reverse_randomized, label="Randomized (Reverse-Sorted Array)", linestyle=":", marker="s")

    # Formatting the plot
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Empirical Comparison of Deterministic and Randomized Selection Algorithms")
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig("algorithm_comparison.png")
    plt.show()

# Call this function to plot and save the comparison graph and print results
plot_comparison()

