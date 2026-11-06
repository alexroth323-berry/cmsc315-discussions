"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

Completed by Alexander Roth
"""

from collections import deque


class Stack:
    def __init__(self):
        # Internal data structure: a Python list where the end represents the top of the stack.
        self.items = []

    def push(self, value):
        # Add value to the top of the stack.
        # This supports LIFO (Last-In, First-Out) behavior because items are added and removed from the same end.
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value from the top of the stack.
        if self.is_empty():
            print("  [Warning] Stack underflow: Cannot pop from an empty stack.")
            return None
        return self.items.pop()

    def peek(self):
        # Return the top value without removing it from the stack.
        if self.is_empty():
            print("  [Warning] Cannot peek: Stack is empty.")
            return None
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Internal data structure: collections.deque provides O(1) appends and pops from both ends.
        self.items = deque()

    def enqueue(self, value):
        # Add value to the back of the queue.
        # This supports FIFO (First-In, First-Out) behavior as items join at the rear and leave from the front.
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value from the front of the queue.
        if self.is_empty():
            print("  [Warning] Queue underflow: Cannot dequeue from an empty queue.")
            return None
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it from the queue.
        if self.is_empty():
            print("  [Warning] Cannot view front: Queue is empty.")
            return None
        return self.items[0]

    def is_empty(self):
        # Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO (LIFO)
    # ===============================
    print("\n=== STACK DEMO (Last-In, First-Out) ===")
    my_stack = Stack()

    print("1. Pushing 4 items onto the stack: Page 1, Page 2, Page 3, Page 4")
    my_stack.push("Browser Page 1")
    my_stack.push("Browser Page 2")
    my_stack.push("Browser Page 3")
    my_stack.push("Browser Page 4")

    print(f"   Top of stack (peek): {my_stack.peek()}")

    print("2. Demonstrating LIFO behavior by popping items:")
    while not my_stack.is_empty():
        print(f"   Popped: {my_stack.pop()}")

    print("3. Edge Case: Attempting to pop and peek on an empty stack:")
    my_stack.pop()
    my_stack.peek()

    print("4. Edge Case: Single-item stack lifecycle:")
    my_stack.push("Single Task")
    print(f"   Pushed 1 item. Is empty? {my_stack.is_empty()}")
    print(f"   Popped item: {my_stack.pop()}")
    print(f"   After removal, is empty? {my_stack.is_empty()}")

    # ===============================
    # QUEUE DEMO (FIFO)
    # ===============================
    print("\n=== QUEUE DEMO (First-In, First-Out) ===")
    my_queue = Queue()

    print("1. Enqueuing 4 items into the queue: Customer A, Customer B, Customer C, Customer D")
    my_queue.enqueue("Customer A (Network Issue)")
    my_queue.enqueue("Customer B (Password Reset)")
    my_queue.enqueue("Customer C (Software Install)")
    my_queue.enqueue("Customer D (Billing Inquiry)")

    print(f"   Front of queue (front): {my_queue.front()}")

    print("2. Demonstrating FIFO behavior by dequeuing items:")
    while not my_queue.is_empty():
        print(f"   Dequeued: {my_queue.dequeue()}")

    print("3. Edge Case: Attempting to dequeue and check front on an empty queue:")
    my_queue.dequeue()
    my_queue.front()

    print("4. Edge Case: Single-item queue lifecycle:")
    my_queue.enqueue("Express Ticket")
    print(f"   Enqueued 1 item. Is empty? {my_queue.is_empty()}")
    print(f"   Dequeued item: {my_queue.dequeue()}")
    print(f"   After removal, is empty? {my_queue.is_empty()}")

    # ===============================
    # CUSTOM REAL-WORLD SCENARIO: SUPPORT DESK TICKET ROUTER
    # ===============================
    print("\n=== CUSTOM SCENARIO: SUPPORT DESK TICKET ROUTER ===")
    support_queue = Queue()
    action_stack = Stack()

    print("Incoming support requests arrive in a FIFO queue:")
    support_queue.enqueue("Ticket #101: Printer offline")
    support_queue.enqueue("Ticket #102: VPN connection error")

    print(f"Next ticket to be serviced: {support_queue.front()}")

    processed_ticket = support_queue.dequeue()
    print(f"Processed: {processed_ticket}")
    action_stack.push(processed_ticket)

    print(f"Last processed action logged to undo stack: {action_stack.peek()}")
    print(f"Remaining tickets in queue: {not support_queue.is_empty()}")


if __name__ == "__main__":
    main()