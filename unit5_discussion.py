"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each element in the list sequentially from index 0 to n-1.
    # In the worst case (when the element is at the very end or not present),
    # it must inspect all n elements, resulting in O(n) linear time complexity.
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search requires a sorted list and maintains 'low' and 'high' pointers.
    # Each iteration calculates the middle index and compares it to the target:
    # - If matched, returns the index.
    # - If the target is smaller, discards the right half by adjusting 'high'.
    # - If the target is larger, discards the left half by adjusting 'low'.
    # This halves the remaining search space every step, yielding O(log n) logarithmic time complexity.
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET TEST
    # ===============================
    print("\n=== SMALL DATASET TEST ===")
    small_list = [12, 25, 38, 45, 60, 75, 90]
    print(f"Dataset: {small_list}")

    # Test existing value (60)
    target_exist = 60
    print(f"\nSearching for existing value: {target_exist}")
    lin_res = linear_search(small_list, target_exist)
    bin_res = binary_search(small_list, target_exist)
    print(f"Linear Search Index: {lin_res}")
    print(f"Binary Search Index: {bin_res}")
    # Both algorithms find the value successfully; linear scanned sequentially,
    # while binary search targeted the middle immediately.

    # Test non-existing value (50)
    target_missing = 50
    print(f"\nSearching for non-existing value: {target_missing}")
    lin_res_missing = linear_search(small_list, target_missing)
    bin_res_missing = binary_search(small_list, target_missing)
    print(f"Linear Search Index: {lin_res_missing}")
    print(f"Binary Search Index: {bin_res_missing}")
    # Both algorithms correctly return -1 when the value is absent.

    # ===============================
    # LARGE DATASET TEST
    # ===============================
    print("\n=== LARGE DATASET TEST ===")
    # Create a larger sorted dataset of 1,000 integers
    large_list = list(range(0, 2000, 2))  # Even numbers from 0 to 1998
    target_large = 1542
    print(f"Large dataset size: {len(large_list)} elements")
    print(f"Searching for target: {target_large}")

    lin_res_large = linear_search(large_list, target_large)
    bin_res_large = binary_search(large_list, target_large)
    print(f"Linear Search Result Index: {lin_res_large}")
    print(f"Binary Search Result Index: {bin_res_large}")
    # On large datasets, binary search is dramatically more efficient. For 1,000 elements,
    # linear search can require up to 1,000 checks, whereas binary search takes at most ~10 steps.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []
    print(f"1. Empty List Test: {empty_list}")
    print(f"Linear Search on empty list: {linear_search(empty_list, 10)}")
    print(f"Binary Search on empty list: {binary_search(empty_list, 10)}")
    # Both algorithms safely handle empty lists by returning -1 without failing.

    # Edge Case 2: Single-element list
    single_list = [42]
    print(f"\n2. Single-Element List Test: {single_list}")
    print(f"Search for existing (42): Linear={linear_search(single_list, 42)}, Binary={binary_search(single_list, 42)}")
    print(f"Search for absent (99): Linear={linear_search(single_list, 99)}, Binary={binary_search(single_list, 99)}")
    # Single-element checks verify loop conditions and bounds correctly.

    # Edge Case 3: Boundary positions (first and last elements)
    bound_list = [5, 10, 15, 20, 25]
    print(f"\n3. Boundary Positions Test: {bound_list}")
    print(f"First position (5): Linear Index={linear_search(bound_list, 5)}, Binary Index={binary_search(bound_list, 5)}")
    print(f"Last position (25): Linear Index={linear_search(bound_list, 25)}, Binary Index={binary_search(bound_list, 25)}")
    # Linear search finds the first element instantly but requires full traversal for the last element.
    # Binary search handles boundaries seamlessly via pointer adjustments.


if __name__ == "__main__":
    main()