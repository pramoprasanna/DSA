Day 04 and Day 05 - ABSENT.

# 📘 Space Complexity in Data Structures & Algorithms

## ✅ What is Space Complexity?

**Space Complexity** refers to the **total memory used** by an algorithm during its execution, including:
- **Input storage** (often ignored in analysis)
- **Auxiliary space** (extra space required to solve the problem)

---

## 🧠 Types of Space Complexity

| Complexity | Description                          | Example                        |
|------------|--------------------------------------|--------------------------------|
| **O(1)**   | Constant space                       | Swapping, Two Pointers         |
| **O(n)**   | Linear space                         | Creating a copy of an array    |
| **O(n²)**  | Quadratic space                      | 2D matrix operations           |
| **O(log n)** | Logarithmic space                  | Recursive Binary Search        |
| **O(n + m)** | Combined space for multiple inputs | Merging two arrays             |

---

## 🔄 In-Place Algorithms

- Operate **without using extra space** (typically **O(1)**).
- **Example:**  
  Move all zeroes to the end of an array using the Two Pointers technique.

---

## 🧪 Auxiliary vs Total Space

- **Auxiliary Space**: Additional memory used by the algorithm (not including input).
- **Total Space**: Input + auxiliary space.
- In most algorithm analysis, we focus on **auxiliary space**.

---

## 💡 Tips for Space Complexity Analysis

- Check for:
  - Extra data structures: `list`, `set`, `dict`
  - Recursion depth (adds to the stack)
  - Temporary or loop variables
- Beware of implicit memory usage:
  - String slicing or list comprehensions can increase space usage

---

✅ *Use this as a reference to evaluate memory efficiency alongside time complexity in your problem-solving!*
