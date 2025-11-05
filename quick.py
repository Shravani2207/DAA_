import random
import time
# ------------------ Deterministic Quick Sort ------------------
def deterministic_partition(arr, low, high):
    pivot = arr[high]              # Choose last element as pivot
    i = low - 1                    # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:        # If current element is smaller than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot correctly
    return i + 1
def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)
# ------------------ Randomized Quick Sort ------------------
def randomized_partition(arr, low, high):
    random_pivot = random.randint(low, high)       # Pick random pivot
    arr[high], arr[random_pivot] = arr[random_pivot], arr[high]  # Swap with last element
    return deterministic_partition(arr, low, high) # Partition normally

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)
# ------------------ Main Program ------------------
if __name__ == "__main__":
    size = int(input("Enter number of elements: "))
    # Random array
    arr = [random.randint(1, 1000) for _ in range(size)]
    # Copies for both quicksort versions
    arr1 = arr.copy()
    arr2 = arr.copy()
    print("\nOriginal Array:", arr)
    # Deterministic Quick Sort
    start = time.time()
    deterministic_quick_sort(arr1, 0, len(arr1) - 1)
    end = time.time()
    print("\nSorted Array (Deterministic):", arr1)
    print("Time taken (Deterministic): {:.6f} seconds".format(end - start))
    # Randomized Quick Sort
    start = time.time()
    randomized_quick_sort(arr2, 0, len(arr2) - 1)
    end = time.time()
    print("\nSorted Array (Randomized):", arr2)
    print("Time taken (Randomized): {:.6f} seconds".format(end - start))
--------------------------------------------------------------------------------






import random
import time
import random — imports Python’s random module (used to pick a random pivot in randomized quicksort).
import time — imports the time module (used to measure elapsed time for each sort).
# ------------------ Deterministic Quick Sort ------------------
Comment separating the deterministic quicksort section.
def deterministic_partition(arr, low, high):
Defines the function deterministic_partition which takes:
arr — the list to be partitioned,
low — starting index of the subarray,
high — ending index of the subarray (we choose arr[high] as pivot).
pivot = arr[high]              # Choose last element as pivot
pivot stores the value of the last element of the current subarray. This is the deterministic pivot choice (always last element).
i = low - 1                    # Index of smaller element
i tracks the boundary of elements ≤ pivot. Initially set to low - 1 meaning no smaller elements seen yet.
for j in range(low, high):
Loop j over all indices from low to high - 1 to compare each element with pivot.
if arr[j] <= pivot:        # If current element is smaller than pivot
If the current element arr[j] is ≤ pivot, it belongs to the "left" (smaller-or-equal) partition.
i += 1
arr[i], arr[j] = arr[j], arr[i]  # Swap
Increment i (expand left partition) and swap arr[i] with arr[j], moving the smaller element into the left partition. This is an in-place swap.
arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot correctly
After the loop, swap pivot (arr[high]) with arr[i+1] — pivot goes to its correct sorted position, with all elements left of it ≤ pivot and right of it > pivot.
return i + 1
Return the pivot index (i + 1) so the caller can recurse on the two subarrays.
________________________________________
def deterministic_quick_sort(arr, low, high):
Define the full deterministic quicksort recursive function.
if low < high:
Base check: there are at least two elements to sort. If low >= high, subarray has 0 or 1 element and is already sorted.
pi = deterministic_partition(arr, low, high)
Partition the subarray and get pivot index pi.
deterministic_quick_sort(arr, low, pi - 1)
deterministic_quick_sort(arr, pi + 1, high)
Recursively sort left subarray (low to pi-1) and right subarray (pi+1 to high).
________________________________________
# ------------------ Randomized Quick Sort ------------------
Comment separating randomized quicksort section.
def randomized_partition(arr, low, high):
Define partition function for randomized quicksort.
random_pivot = random.randint(low, high)       # Pick random pivot
Choose a random index between low and high (inclusive). This randomness helps avoid worst-case inputs designed for deterministic pivot choices.
arr[high], arr[random_pivot] = arr[random_pivot], arr[high]  # Swap with last element
Swap the randomly chosen pivot element into position high so we can reuse the same partition logic as deterministic_partition.
return deterministic_partition(arr, low, high) # Partition normally
Call the deterministic partition (which expects the pivot at high) and return its pivot index.
________________________________________
def randomized_quick_sort(arr, low, high):
Define randomized quicksort recursive function.
if low < high:
Base check as before.
pi = randomized_partition(arr, low, high)
randomized_quick_sort(arr, low, pi - 1)
randomized_quick_sort(arr, pi + 1, high)
Partition using random pivot and recursively sort left and right partitions.
________________________________________
# ------------------ Main Program ------------------
Separator comment for the main execution block.
if __name__ == "__main__":
Standard Python idiom: execute the following only when the script is run directly (not when imported).
size = int(input("Enter number of elements: "))
Read number of elements from user and convert to int.
arr = [random.randint(1, 1000) for _ in range(size)]
Create a list arr of length size with random integers between 1 and 1000 (inclusive). The list is random so timing comparisons are meaningful.
arr1 = arr.copy()
arr2 = arr.copy()
Create two independent copies so both sorts operate on the exact same initial data for fair timing comparison.
print("\nOriginal Array:", arr)
Print the generated original array for reference.
________________________________________
start = time.time()
deterministic_quick_sort(arr1, 0, len(arr1) - 1)
end = time.time()
Record start time, run deterministic quicksort on arr1, then record end time. time.time() returns current time in seconds (floating point).
print("\nSorted Array (Deterministic):", arr1)
print("Time taken (Deterministic): {:.6f} seconds".format(end - start))
Print sorted arr1 and the time difference end - start formatted to 6 decimal places.
________________________________________
start = time.time()
randomized_quick_sort(arr2, 0, len(arr2) - 1)
end = time.time()
Same timing pattern for randomized quicksort on arr2.
print("\nSorted Array (Randomized):", arr2)
print("Time taken (Randomized): {:.6f} seconds".format(end - start))
Display the result and timing for randomized quicksort.
________________________________________
Partition invariant: After partitioning, pivot is in final sorted position; left elements ≤ pivot; right elements > pivot.
In-place algorithm: Quick sort here sorts the array in place — it uses no extra arrays (only recursion stack).
Stability: Quick sort is not stable — equal elements can change relative order because of swaps.
Time complexity:
Average: O(n log n)
Best: O(n log n)
Worst: O(n²) — occurs for bad pivot choices (e.g., already sorted array when pivot is always first/last).
Randomized quicksort benefit: Random pivot makes worst-case probabilistically unlikely, giving expected O(n log n) even for adversarial inputs.
Space complexity: O(log n) expected for recursion stack (balanced partitions), O(n) worst-case stack depth for skewed partitions.
Deterministic pivot choice (last element) is simple but can be exploited; randomized pivot reduces that risk.
Practical note: For very small subarrays, implementations often switch to insertion sort (faster constant factor).
Seeding randomness: For reproducible timing comparisons you might seed the RNG with random.seed(some_value) before creating arr. 
But for comparisons between algorithms, identical initial arrays already ensure fairness.

Questions
What is Quick Sort?
Quick Sort is a divide-and-conquer sorting algorithm that picks a pivot, partitions the array around the pivot, and recursively sorts the left and right parts. It is efficient and works in-place
What is the pivot element
The pivot is the element used to divide the array into two parts — one with values smaller or equal to the pivot and the other with values greater than the pivot.
Difference between Deterministic and Randomized Quick Sort?
Deterministic Quick Sort	Randomized Quick Sort
Pivot chosen fixed (last element)	Pivot chosen randomly
Worst-case occurs on sorted/reverse input	Randomization avoids worst-case in most cases
Easier to implement	More robust and secure

Why do we use random pivot selection?
To avoid worst-case time complexity and make Quick Sort more stable and efficient for all types of input. It prevents adversarial cases.
What is the worst-case time complexity of Quick Sort?
Worst-case: O(n²)
Occurs when array is sorted or reverse & pivot chosen badly.
What is the average time complexity
Average time complexity: O(n log n)
What is the space complexity of Quick Sort
Space complexity: O(log n) (due to recursive stack).
Is Quick Sort stable?
No. Quick Sort is not stable because equal elements can be swapped changing their order.
What is partitioning?
Partitioning rearranges the array so that all elements ≤ pivot come before pivot and > pivot come after pivot.
Why did we take two arrays arr1 and arr2?
To apply deterministic quick sort on one and randomized quick sort on the other, so we can compare output and execution time fairly.
Why do we measure time in this program
To compare and show that randomized Quick Sort generally performs faster and avoids worst-case scenarios.
What library is used for random pivot?
random module → random.randint(low, high)
It selects a random index for pivot.
What library is used for time calculation?
time module → time.time() to measure execution duration.
What type of algorithm is Quick Sort?
Divide and Conquer algorithm.
Which sorting algorithm is faster — Merge Sort or Quick Sort?
Quick Sort usually performs faster in practice due to in-place sorting & better cache performance, though worst-case is worse.
Where is Quick Sort used in real life?
Used in C / C++ standard library (qsort()), Python TimSort uses Quick Sort concepts internally, databases, and system-level sort functions.
________________________________________
What is the basic idea behind Quicksort?
Quicksort is a divide-and-conquer sorting algorithm.
It works by:
Divide: Choose a pivot and partition the array so that:
Elements ≤ pivot go to left
Elements > pivot go to right
Conquer: Recursively sort the left and right parts
Combine: Nothing (subarrays already sorted)
What is the Partition() function in Quicksort?
Partition selects a pivot and rearranges the array such that:
Elements ≤ pivot are moved to left
Elements > pivot are moved to right
It returns the final index of the pivot after arrangement.
What is the worst-case time complexity of Quicksort and why?
Worst case: Θ(n²)
Occurs when partitioning is extremely unbalanced — for example, when the pivot is always the smallest or the largest element.
What is the best-case time complexity of Quicksort and why?
Best case: O(n log n)
Happens when pivot always divides the list into two equal halves.
Why might deterministic Quicksort perform poorly?
Because if the pivot selection is unlucky (like sorted input), partitions become highly unbalanced, leading to Θ(n²) time.
What is median-of-medians? Why is it used?
Median-of-medians is a linear-time (O(n)) algorithm used to find the pivot such that partitions are balanced.
It ensures Quicksort always runs in O(n log n) in worst case.
Why is median-of-medians not used in practice?
Because although it guarantees worst-case O(n log n),
it has high constant overhead, making it slower in practice than randomized pivot selection.
How does Randomized Quicksort avoid worst-case?
It picks a random pivot, making it highly unlikely to always get bad partitions.
Expected time complexity remains O(n log n).
What is the expected number of comparisons in Randomized Quicksort?
Expected comparisons = O(n log n)
Derived using probability that two elements are compared only once.
Explain the key probability fact used in analysis.
For two sorted elements zi and zj,
they are compared only if one of them is chosen as the first pivot among elements between them.
Probability =
[
\frac{2}{j - i + 1}
]
What does I{ zi is compared to zj } represent?
It is an indicator random variable that equals:
1 if zi and zj are compared
0 otherwise
Describe the Partition steps.
Pick pivot (rightmost or random index)
Keep index i for smaller elements
Traverse array; swap when element ≤ pivot
Place pivot in correct position
Return pivot index
Difference between Partition and Randomized-Partition?
Partition	Randomized-Partition
Always uses last element as pivot	Picks random element as pivot
Can cause worst-case on sorted input	Avoids worst-case with high probability
Why is Quicksort usually preferred over Merge Sort?
Faster in practice
Cache-efficient (in-place)
Lower constant factors

Why does Quicksort not need a combine step?
Subarrays are already sorted after recursive calls.
________________________________________

