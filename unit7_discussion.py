"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Copy the input list so the caller's original list is never mutated
    arr = list(lst)
    n = len(arr)

    # Outer loop controls passes; nested loops cause O(n^2) comparisons/swaps
    # in average and worst cases as elements bubble into sorted position
    for i in range(n):
        swapped = False
        # Compare adjacent pairs in the unsorted prefix (0 to n - 1 - i)
        for j in range(0, n - 1 - i):
            # Use strict '>' so equal elements are not swapped, preserving stability
            if arr[j] > arr[j + 1]:
                # Swap out-of-order neighboring elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Early exit if a full pass makes no swaps (list is already sorted)
        if not swapped:
            break

    return arr


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case: lists of length 0 or 1 are already sorted
    if len(lst) <= 1:
        return list(lst)

    # Divide: split the list into two halves around the midpoint
    mid = len(lst) // 2
    left_sorted = merge_sort(lst[:mid])
    right_sorted = merge_sort(lst[mid:])

    # Conquer/Combine: merge the two sorted halves into one sorted list
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    merged = []
    i = 0
    j = 0

    # Compare elements at the front of left and right; using '<=' preserves
    # relative order of equal values (stability)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from whichever half still has items
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    # Dataset #1: Unsorted list of 8 content engagement/relevance scores
    dataset_1 = [48, 12, 95, 34, 77, 19, 63, 25]
    bubble_d1 = bubble_sort(dataset_1)
    merge_d1 = merge_sort(dataset_1)

    print("\n=== DATASET #1 ===")
    print("Original Dataset #1:", dataset_1)
    print("Dataset #1 - Bubble Sort result:", bubble_d1)
    print("Dataset #1 - Merge Sort result: ", merge_d1)
    print("Dataset #1 - Results match?      ", bubble_d1 == merge_d1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    # Dataset #2: Second dataset with different values and repeated ratings
    dataset_2 = [85, 40, 85, 15, 60, 40, 92, 10]
    bubble_d2 = bubble_sort(dataset_2)
    merge_d2 = merge_sort(dataset_2)

    print("\n=== DATASET #2 ===")
    print("Original Dataset #2:", dataset_2)
    print("Dataset #2 - Bubble Sort result:", bubble_d2)
    print("Dataset #2 - Merge Sort result: ", merge_d2)
    print("Comparison: Both produce the identical ascending order", bubble_d2,
          "while preserving equal values across passes/merges.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list []
    # Bubble Sort makes zero swaps and exits immediately; Merge Sort hits its
    # base case (len <= 1) and returns a new empty list safely.
    empty_list = []
    print("Edge Case 1 - Empty list [] -> Bubble:", bubble_sort(empty_list),
          "| Merge:", merge_sort(empty_list))

    # Edge Case 2: Already-sorted list [10, 20, 30, 40, 50]
    # Bubble Sort performs one pass with no swaps and breaks early; Merge Sort
    # still divides down to single elements and merges in O(n log n) time.
    sorted_list = [10, 20, 30, 40, 50]
    print("Edge Case 2 - Already sorted [10..50] -> Bubble:", bubble_sort(sorted_list),
          "| Merge:", merge_sort(sorted_list))

    # Edge Case 3: Duplicate values [55, 22, 55, 11, 22]
    # Both algorithms keep equal values in ascending order without errors.
    duplicates_list = [55, 22, 55, 11, 22]
    print("Edge Case 3 - Duplicates -> Bubble:", bubble_sort(duplicates_list),
          "| Merge:", merge_sort(duplicates_list))


if __name__ == "__main__":
    main()