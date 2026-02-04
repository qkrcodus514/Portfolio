"""
📘 Python Study Examples

- Core concept examples only
- Detailed explanations are documented in README.md
- Practice and experimental code is maintained separately
"""

# ==============================
# [Example 01] append()
# ==============================
num = []
num.append(10)

print("append 결과:", num)

word = ["a", "b", "c"]
word.append("d")

print("append 결과:", word)

# ==============================
# [Example 02] insert()
# ==============================
num = [1, 2, 3, 4, 5]
num.insert(2, 3)

print("inert 결과:", num)

# ==============================
# [Example 03] remove()
# ==============================
words = ["d", "b", "a", "c"]
words.remove("d")

print("remove 결과:", words)

# ==============================
# [Example 04] sort()
# ==============================
value = [6, 4, 2, 1, 8]

print("정렬 전 리스트", value)
value.sort()
print("정렬 후 리스트:", value)

foods = ["carrot", "apple", "banana"]

print("정렬 전 리스트:", foods)
foods.sort()
print("정렬 후 리스트:", foods)

# ==============================
# [Example 05] sorted()
# ==============================
numbers = [5, 3, 8, 13, 20]
result = sorted(numbers)

print("정렬 결과:", result)
print("원본 리스트:", numbers)

# ================================
# [Example 06] sorted() 내림차순
# ================================
scores = [96, 92, 91, 88, 85]
result = sorted(scores, reverse=True)

print("내림차순 정렬 결과:", result)

