---

Following DSA concept in Krish Naik's Udemy DSA Course to get a structure

# 📘 Topic Today: Python Basic Syntax and Semantics

---

### 🔹 Syntax vs Semantics
- **Syntax**: The set of rules that defines the combinations of symbols considered correctly structured Python code.
- **Semantics**: The meaning or interpretation of a piece of code once it has been parsed.

---

### 🔹 Case Sensitivity
- Python is a **case-sensitive** language. For example, `Variable` and `variable` are treated as different identifiers.

---

### 🔹 Commenting in Python
- **Single-line comment**: Use `#`
- **Multi-line comment**: Use triple single quotes `'''` or triple double quotes `"""`

---

### 🔹 Indentation
- Indentation is crucial in Python to group statements.
- Used for control structures like `if`, `for`, `while`, etc.

---

### 🔹 Mutable vs Immutable Data Structures
- **Mutable**: Variables referencing the same value will have the same memory address.
- **Immutable**: Variables referencing the same value will have different memory addresses.
- Example:
  ```python
  a = [1, 2]; b = a        # Same address (mutable)
  x = 5; y = 5             # Different address (immutable)```

---

### 🔹 Line Continuation

* Use `\` to continue a line of code across multiple lines.

  ```python
  result = 1 + 2 + 3 + \
           4 + 5
  ```

---

### 🔹 Multiple Statements on One Line

* Separate them using `;`

  ```python
  x = 5; y = 10; z = x + y; print(z)
  ```

---

### 🔹 Identifying Data Structures

* Use `type()` to find the type of a variable.

  * Example:

    ```python
    print(type(variable_name))  # Output: <class 'int'> or similar
    ```
* In Jupyter notebooks:

  ```python
  type(variable)  # Output: int
  ```

---

```

Let me know if you'd like to save this into your project as a `.md` file too.
```
