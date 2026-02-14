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
Topic: input() Function Practice

- input()의 반환 자료형 확인
- 형 변환 전후 비교
- 숫자 연산 시 형 변환 필요성 이해
"""


# Input
user_input = input("값을 입력하세요: ")

print("입력한 값:", user_input)
print("입력값의 자료형:", type(user_input))


# Type Casting
number = int(user_input)

print("형 변환 후 값:", number)
print("형 변환 후 자료형:", type(number))


# Arithmetic Operation
print(f"입력한 숫자의 2배: {number * 2}")


# 💡 Learned
# 1. input()은 항상 문자열(str)을 반환한다.
# 2. 숫자 계산을 위해서는 반드시 형 변환이 필요하다.
# 3. 잘못된 입력이 들어오면 ValueError가 발생할 수 있다.