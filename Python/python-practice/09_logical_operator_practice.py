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
Topic: Logical Operators

- and
- or
- not
- 논리 연산은 bool 값을 결합한다
"""


# --- and | 모두 True일 때 True ---

print("True and True:", True and True)
print("True and False:", True and False)


# --- or | 하나라도 True이면 True ---

print("True or False:", True or False)
print("False or False:", False or False)


# --- not | 반전 ---

print("not True:", not True)
print("not False:", not False)


# --- Logical with Comparison | 비교 + 논리 연산 ---

age = 20

print("age >= 18 and age < 30:", age >= 18 and age < 30)
print("age < 18 or age > 65:", age < 18 or age > 65)


# 💡 Learned
# 1. and 는 모든 조건이 True일 때 True.
# 2. or 는 하나라도 True이면 True.
# 3. not 은 결과를 반전시킨다.
# 4. 논리 연산자는 비교 연산과 함께 자주 사용된다.
