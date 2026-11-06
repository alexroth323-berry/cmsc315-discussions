# Unit 4 Discussion: Binary Search Trees

## Overview

This project implemented a Binary Search Tree (BST) in Python to demonstrate recursive tree operations, node insertion, searching, and in-order traversal.

## Learning Objectives Achieved

- Built a functional `BST` and `Node` class in Python.
- Implemented recursive node insertion based on value comparisons.
- Designed recursive search algorithms for $O(\log n)$ efficient lookups.
- Performed in-order traversal to retrieve sorted node values.
- Analyzed BST organization, performance benefits, and edge case behaviors.

## Implementation Details

1. **BST Construction & Insertion**:
   - Created `Node` and `BST` classes.
   - Values were inserted recursively: elements smaller than the current node were placed into the left subtree, while larger elements were routed to the right subtree.

2. **In-Order Traversal**:
   - Implemented `inorder()` using recursive depth-first traversal (Left Subtree -> Node -> Right Subtree).
   - Verified that visiting nodes in this sequence consistently produced output in ascending sorted order.

3. **Searching**:
   - Implemented recursive search logic.
   - Demonstrated $O(\log n)$ lookup efficiency by discarding half of the remaining subtrees at each step.

4. **Edge Cases**:
   - Verified that searching and traversing an empty tree (or `None` root reference) handled null references gracefully without throwing runtime errors.

## Discussion Board Reflection

### Reflection Questions & Answers

1. **What concepts or skills did you learn while completing this assignment?**
   - I learned how to construct a binary search tree data structure from scratch using Python, focusing on recursive helper functions for inserting nodes, searching for target values, and navigating subtrees via in-order traversal.

2. **What challenges did you encounter, and how did you overcome them?**
   - A primary challenge was managing recursive return values during tree node insertions to ensure new child nodes properly attached back up the call stack. I resolved this by explicitly returning updated node references (`return node`) at each step of the recursion.

3. **Explain BST behavior and compare how ordering creates efficiency as compared to other data structures.**
   - BSTs enforce a strict ordering rule where values smaller than a node reside in its left subtree and larger values reside in its right subtree. This structure allows search operations to eliminate half of the remaining branches at every node comparison, achieving $O(\log n)$ efficiency on balanced trees compared to the $O(n)$ linear scan required for standard lists or linked lists.