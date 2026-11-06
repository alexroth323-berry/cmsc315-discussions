# Unit 2 Discussion: Stacks and Queues

## Overview
This assignment explores two fundamental linear data structures:
- Stack (LIFO: Last-In, First-Out)
- Queue (FIFO: First-In, First-Out)

## Implementation Summary
- **Stack:** Built using a Python list backing store where `push` and `pop` operate on the top (end) of the list in $O(1)$ amortized time.
- **Queue:** Built using `collections.deque` to guarantee $O(1)$ efficiency for both `enqueue` and `dequeue` operations.
- **Edge Cases:** Implemented checks for empty data structures to prevent underflow errors during `pop`, `dequeue`, `peek`, and `front` operations.

## Reflection Essay
While completing this assignment, I learned how to implement linear data structures from scratch and manage state using LIFO and FIFO access policies. A key challenge I encountered was handling edge cases gracefully, such as attempting to pop or peek from an empty structure without throwing runtime errors. I overcame this by adding conditional validation checks inside each method to output clear warning messages when structures are empty. 

Stacks and queues serve opposing purposes in real-world applications. A stack uses LIFO behavior, which makes it ideal for scenarios requiring reversal or history tracking, such as a web browser's back button or text editor undo features. Conversely, a queue uses FIFO behavior, ensuring fairness by processing items in the exact order they arrive, which is essential for customer service ticketing systems, print spoolers, and task scheduling in operating systems.