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
Topic: List Slicing

- 기본 슬라이싱
- 시작/끝 생략
- 음수 인덱스
- step 사용
- 리스트 복사
"""


# --- List Declaration | 리스트 선언 ---

numbers = [10, 20, 30, 40, 50, 60]
print("Original List:", numbers)


# --- Basic Slicing | 기본 슬라이싱 ---

print("numbers[0:3]:", numbers[0:3])
print("numbers[2:5]:", numbers[2:5])


# --- Omit Start or End | 시작/끝 생략 ---

print("numbers[:3]:", numbers[:3])
print("numbers[3:]:", numbers[3:])


# --- Negative Index | 음수 인덱스 ---

print("numbers[-3:]:", numbers[-3:])
print("numbers[:-2]:", numbers[:-2])


# --- Step | 간격 지정 ---

print("numbers[::2]:", numbers[::2])
print("numbers[::-1]:", numbers[::-1])  # 리스트 뒤집기


# --- List Copy | 리스트 복사 ---

copied_list = numbers[:]
print("Copied List:", copied_list)


# 💡 Learned
# 1. 리스트 슬라이싱은 [start:end] 형태로 사용한다.
# 2. start나 end를 생략할 수 있다.
# 3. 음수 인덱스를 사용하면 뒤에서부터 접근한다.
# 4. step을 사용하면 간격을 지정할 수 있다.
# 5. [:]는 리스트를 복사할 때 사용할 수 있다.
