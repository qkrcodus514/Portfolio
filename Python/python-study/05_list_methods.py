"""
📘 Python Study Examples

- Core concept examples only
- Detailed explanations are documented in README.md
- Practice and experimental code is maintained separately
"""

# ==============================
# [Example 01] append()
# ==============================

# --- Pattern 1: Initialize and Append ---
num = []
num.append(10)

print("append 결과:", num)

# --- Pattern 2: Extend Existing List ---
word = ["a", "b", "c"]
word.append("d")

print("append 결과:", word)


# ==============================
# [Example 02] insert()
# ==============================

# --- Pattern: Insert at Specific Index ---
num = [1, 2, 3, 4, 5]
num.insert(2, 3)

print("insert 결과:", num)


# ==============================
# [Example 03] remove()
# ==============================

# --- Pattern: Remove Specific Value ---
words = ["d", "b", "a", "c"]
words.remove("d")

print("remove 결과:", words)


# ==============================
# [Example 04] sort()
# ==============================

# --- Pattern 1: Numeric Sorting (In-place) ---
value = [6, 4, 2, 1, 8]

print("정렬 전 리스트", value)
value.sort()
print("정렬 후 리스트:", value)


# --- Pattern 2: String Sorting ---
foods = ["carrot", "apple", "banana"]

print("정렬 전 리스트:", foods)
foods.sort()
print("정렬 후 리스트:", foods)


# ==============================
# [Example 05] sorted()
# ==============================

# --- Pattern 1: Create New Sorted List ---
numbers = [5, 3, 8, 13, 20]
result = sorted(numbers)

print("정렬 결과:", result)
print("원본 리스트:", numbers)


# ================================
# [Example 06] sorted() 내림차순
# ================================

# --- Pattern 2: Descending Order ---
scores = [96, 92, 91, 88, 85]
result = sorted(scores, reverse=True)

print("내림차순 정렬 결과:", result)

