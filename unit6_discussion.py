"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Create an empty dictionary to act as a hash table for restaurant reservations
    reservations = {}

    # Populate with at least 5 key-value pairs (confirmation code -> guest/party info).
    # In Python, a dict implements a hash table: each immutable key is hashed via
    # hash(key) to locate a slot in an internal sparse array, enabling average O(1)
    # insertion, lookup, update, and deletion without scanning every booking.
    reservations["RES-101"] = {"guest": "Jordan Lee", "party_size": 4, "time": "18:30"}
    reservations["RES-102"] = {"guest": "Priya Patel", "party_size": 2, "time": "18:45"}
    reservations["RES-103"] = {"guest": "Mateo Cruz", "party_size": 6, "time": "19:00"}
    reservations["RES-104"] = {"guest": "Hannah Kim", "party_size": 3, "time": "19:15"}
    reservations["RES-105"] = {"guest": "Devon Brooks", "party_size": 5, "time": "19:30"}

    print("\n=== INSERT OPERATIONS ===")
    print("Initial reservation hash table contents:")
    for code, details in reservations.items():
        print(f"  {code}: {details}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # Key lookup computes hash(key), jumps directly to the corresponding bucket/slot,
    # and compares keys for equality—achieving average O(1) time regardless of table size.
    lookup_one = reservations["RES-101"]
    lookup_two = reservations["RES-104"]

    print("\n=== LOOKUP OPERATIONS ===")
    print(f"Lookup 'RES-101' -> {lookup_one}")
    print(f"Lookup 'RES-104' -> {lookup_two}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before updating 'RES-102':", reservations["RES-102"])

    # Because keys in a dictionary are unique, assigning to an existing key hashes
    # 'RES-102' to its existing slot and overwrites the stored value in place rather
    # than inserting a duplicate key or increasing len(reservations).
    reservations["RES-102"] = {"guest": "Priya Patel", "party_size": 4, "time": "19:00"}

    print("After updating 'RES-102':", reservations["RES-102"])

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before deleting 'RES-103' (count =", len(reservations), "):", reservations)

    # Removing an entry locates 'RES-103' via its hash and deletes the key-value
    # association from the dictionary; Python's dict marks the entry as deleted so
    # open-addressing probe sequences for other keys remain intact.
    removed_booking = reservations.pop("RES-103")

    print("Removed 'RES-103' ->", removed_booking)
    print("After deleting 'RES-103' (count =", len(reservations), "):", reservations)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Safe lookup of a missing key using .get() instead of [] indexing.
    # Direct indexing reservations["RES-999"] raises a KeyError, whereas .get()
    # safely returns None (or a default value) when the key is not found.
    missing_lookup = reservations.get("RES-999")
    print(f"Edge Case 1 - Safe lookup of missing key 'RES-999': {missing_lookup}")

    # Edge Case 2: Safe deletion of a missing key using .pop(key, default).
    # Passing a fallback default (None) avoids a KeyError and leaves existing
    # reservations untouched.
    missing_delete = reservations.pop("RES-999", None)
    print(f"Edge Case 2 - Safe delete of missing key 'RES-999': {missing_delete}")
    print(f"Inventory/reservation count remains unchanged: {len(reservations)}")


if __name__ == "__main__":
    main()