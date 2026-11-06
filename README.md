# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search[cite: 8]
- Implement binary search[cite: 8]
- Compare performance[cite: 8]
- Analyze algorithm efficiency[cite: 8]

## Requirements

1. Test both algorithms on a small dataset.[cite: 8]
2. Test both algorithms on a large dataset.[cite: 8]
3. Demonstrate edge cases.[cite: 8]
4. Analyze performance.[cite: 8]
5. Create a real-world search scenario.[cite: 8]

## Discussion Board Reflection

Throughout this assignment, I learned how to implement and compare linear and binary search algorithms in Python, analyzing their respective $O(n)$ and $O(\log n)$ time complexities. A key challenge I encountered was correctly managing pointer indices (`low`, `high`, and `mid`) during binary search to prevent infinite loops or missing edge cases on empty and single-element lists. I overcame this by carefully tracing boundary conditions and ensuring the loop termination condition (`low <= high`) was robust.

In practice, linear search is best suited for small or unsorted datasets where the overhead of sorting outweighs search efficiency. Conversely, binary search is highly efficient for large, sorted collections such as database indexes or phone directories, slashing search times exponentially. However, the primary tradeoff for binary search is that the data must be kept in a sorted order, which introduces significant insertion and sorting overhead ($O(n \log n)$) if the dataset is frequently modified.