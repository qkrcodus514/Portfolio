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
Topic: Basic Data Types & Arithmetic Operation

- 변수 선언과 자료형 확인
- type() 함수로 data type 관찰
- 정수 연산 후 값 변화 확인
"""


# --- Variable Declaration | 변수 선언 ---

name = "Python"
age = 20
height = 175.5

print("name:", name)
print("age:", age)
print("height:", height)


# --- Type Check | 자료형 확인 ---

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))


# --- Reassignment | 값 재할당 ---

age = age + 1
print("After +1 age:", age)

name = "Python3"
print("After change name:", name)


# --- Multiple Assignment | 여러 변수 동시에 선언 ---

x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)


# --- Variable Naming Convention | 변수 이름 규칙 ---

my_variable = 10
user_name = "Hiro"

print("my_variable:", my_variable)
print("user_name:", user_name)


# 💡 Learned
# 1. 변수는 값을 저장하는 공간이다.
# 2. 변수는 언제든지 새로운 값으로 재할당할 수 있다.
# 3. type()을 사용하면 자료형을 확인할 수 있다.
# 4. 변수 이름은 의미 있게 작성하는 것이 좋다.
# 5. Python에서는 snake_case 방식을 주로 사용한다.