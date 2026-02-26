"""
📘 Python Study Examples

- Core concept examples only
- Detailed explanations are documented in README.md
- Practice and experimental code is maintained separately
"""

# =======================================
# [Example 01] 변수와 연산자를 이용한 계산
# =======================================

num1 = 12
num2 = num1 + 10
answer = num2 / 2

print("정답은", answer, "이다!")


# ================================
# [Example 02] 숫자형의 몫과 나머지
# ================================

price = 13
people = 5

print("1인당 금액은:", price // people)
print("남은 금액은:", price % people)


# ==============================
# [Example 03] 숫자형 제곱 연산
# ==============================

print("2의 8제곱은:", 2 ** 8)
print("2의 10 제곱은:", 2 ** 10)


# =====================================
# [Example 04] 연산 결과를 변수로 저장
# =====================================

remainder = 4 % 3
power_result = 2 ** 4

print("나머지는:", remainder)
print("제곱 결과:", power_result)


# ===================================
# [Example 05] 문자열의 덧셈과 곱셈
# ===================================

print("안녕" + "하세요")

team = "T1"
cheer = team + " 사랑해 "

print(cheer * 3)

str1 = "Love"+"Faker"
str2 = "Doran" * 2
result = (str1 + str2) * 2

print(result)
