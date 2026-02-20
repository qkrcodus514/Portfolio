"""
🧪 [Portfolio Experiment] Python Code Log

This file records hands-on experimentation through direct code execution.
It follows the learning flow: 
Attempt → Result → 💡 Reflection

Revisions are applied after reviewing execution results.

📘 Structured examples are stored in study files.
🧠 Conceptual explanations are documented in the README 🐍.
"""

"""
Topic: List Methods Practice

- append()
- insert()
- remove()
- sort()
- sorted()
"""


# --- List Declaration | 리스트 선언 ---

fruits = ["banana", "apple", "cherry"]
print("Original List:", fruits)


# --- append() | 요소를 맨 뒤에 추가 ---

fruits.append("orange")
print("After append():", fruits)


# --- insert() | 특정 위치에 요소 추가 ---

fruits.insert(1, "grape")
print("After insert():", fruits)


# --- remove() | 특정 값 삭제 ---

fruits.remove("banana")
print("After remove():", fruits)


# --- sort() | 리스트 자체를 정렬 (원본 변경) ---

fruits.sort()
print("After sort():", fruits)


# --- sorted() | 정렬된 새로운 리스트 반환 (원본 유지) ---

numbers = [3, 1, 4, 2]
print("Original numbers:", numbers)

sorted_numbers = sorted(numbers)
print("After sorted():", sorted_numbers)
print("Original numbers (unchanged):", numbers)


# 💡 Learned
# 1. append()는 리스트의 맨 뒤에 요소를 추가한다.
# 2. insert()는 원하는 위치에 요소를 추가할 수 있다.
# 3. remove()는 특정 값을 삭제한다.
# 4. sort()는 원본 리스트를 정렬한다.
# 5. sorted()는 원본을 변경하지 않고 새로운 정렬된 리스트를 반환한다.
