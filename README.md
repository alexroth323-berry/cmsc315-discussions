# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior through a peak-hour restaurant reservation lookup system.

## Learning Objectives

- Inserted key-value pairs
- Retrieved values efficiently
- Updated existing values
- Removed entries
- Understood hashing concepts

## Requirements

1. Created and populated a dictionary.
2. Demonstrated lookup operations.
3. Demonstrated update operations.
4. Demonstrated delete operations.
5. Tested edge cases.
6. Created a real-world scenario.

## Discussion Board Reflection

While completing this assignment, I practiced how Python dictionaries use key hashing and internal bucket slots to support fast insertions, lookups, updates, and deletions, as well as how to handle missing keys safely using `.get()` and `.pop()` defaults. One challenge I worked through was making sure updating an existing reservation code overwrote the entry cleanly without creating duplicate records, and ensuring missing-key lookups and removals avoided raising `KeyError` exceptions.

A hash table maps keys through a hash function to compute an index for storing and retrieving values directly rather than scanning items sequentially. Collisions happen when two different keys hash to the same slot or probe path, which can lengthen lookup chains or probing sequences as load increases. In real-world systems like restaurant reservation tables, e-commerce catalogs, or social media profiles, hash tables improve efficiency by delivering average $O(1)$ constant-time access, keeping response times fast even during peak traffic.