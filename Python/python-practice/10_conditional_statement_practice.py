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
Topic: Conditional Statements

- if
- if-else
- if-elif-else
- 조건에 따른 분기 처리
"""


# --- if | 단일 조건 ---

number = 10

if number > 0:
    print("number는 양수입니다.")


# --- if-else | 두 갈래 분기 ---

age = 16

if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")


# --- if-elif-else | 다중 분기 ---

score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("점수:", score)
print("등급:", grade)


# --- Logical Condition | 논리 연산과 함께 사용 ---

temperature = 25

if temperature >= 20 and temperature <= 30:
    print("날씨가 쾌적합니다.")
else:
    print("날씨가 쾌적하지 않습니다.")


# 💡 Learned
# 1. if는 조건이 True일 때만 실행된다.
# 2. if-else는 두 가지 경우로 분기한다.
# 3. if-elif-else는 여러 조건을 순차적으로 검사한다.
# 4. 조건문의 순서에 따라 결과가 달라질 수 있다.
# 5. 논리 연산자(and, or)는 조건문에서 자주 함께 사용된다.
