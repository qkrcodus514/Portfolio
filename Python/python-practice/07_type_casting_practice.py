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
Topic: Type Casting & Numeric Behavior

- int(), float(), str(), bool() 형 변환
- 나눗셈 연산자의 결과 타입 차이
- 자동 형 변환 (Implicit Casting)
"""


# --- int() | 문자열 → 정수 변환 ---

text_num = "25"
converted_int = int(text_num)

print("Original:", text_num, "| Type:", type(text_num))
print("After int():", converted_int, "| Type:", type(converted_int))


# --- float() | 정수 → 실수 변환 ---

num_int = 10
converted_float = float(num_int)

print("Original:", num_int, "| Type:", type(num_int))
print("After float():", converted_float, "| Type:", type(converted_float))


# --- str() | 실수 → 문자열 변환 ---

num_float = 3.14
converted_str = str(num_float)

print("Original:", num_float, "| Type:", type(num_float))
print("After str():", converted_str, "| Type:", type(converted_str))


# --- bool() | 불리언 변환 ---

print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(""))


# --- / vs // | 나눗셈 결과 비교 ---

print("10 / 3 =", 10 / 3, "| Type:", type(10 / 3))
print("10 // 3 =", 10 // 3, "| Type:", type(10 // 3))


# --- Implicit Casting | 자동 형 변환 ---

result = 5 + 2.0
print("5 + 2.0 =", result, "| Type:", type(result))


# -----------------------------------
# 💡 Learned
# -----------------------------------
# 1. 형 변환은 int(), float(), str(), bool() 함수로 명시적으로 수행한다.
# 2. 숫자 형태의 문자열만 int()로 변환 가능하다.
# 3. bool()은 값이 비어 있으면 False, 그렇지 않으면 True를 반환한다.
# 4. / 연산자는 항상 float을 반환한다.
# 5. int와 float 연산 시 float으로 자동 형 변환된다.
