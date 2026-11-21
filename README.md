# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort in Python across multiple datasets and edge cases.

## Learning Objectives

- Implemented Bubble Sort
- Implemented Merge Sort
- Understood divide-and-conquer
- Compared algorithm efficiency

## Requirements

1. Tested Bubble Sort and Merge Sort.
2. Used multiple datasets.
3. Demonstrated edge cases.
4. Analyzed performance.
5. Created a real-world sorting example.

## Discussion Board Reflection

While completing this assignment, I implemented iterative Bubble Sort and recursive Merge Sort in Python, tested both algorithms on multiple datasets and edge cases, and analyzed how recursion and divide-and-conquer compare to adjacent-element swapping. One challenge I worked through was keeping the original input lists unmodified while ensuring both sorting functions handled empty lists, already-sorted lists, and duplicate values cleanly.

Bubble Sort repeatedly compares and swaps neighboring elements, resulting in $O(n^2)$ average and worst-case time complexity due to nested loops, though an early-exit flag helps on already-sorted inputs. Merge Sort divides a list recursively into halves and merges sorted sublists in guaranteed $O(n \log n)$ time, at the cost of $O(n)$ extra memory for sublists and merged output. For large or peak-traffic workloads—such as ranking trending shows or personalized watchlists on a streaming platform—Merge Sort scales far better than Bubble Sort, whereas Bubble Sort is mainly suited to small lists or teaching basic comparison mechanics.