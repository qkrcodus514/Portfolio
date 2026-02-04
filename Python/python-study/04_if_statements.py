"""
📘 Python Study Examples

- Core concept examples only
- Detailed explanations are documented in README.md
- Practice and experimental code is maintained separately
"""

# ==============================
# [Example 01] 비교 연산자
# ==============================
ans1 = 5 > 2
ans2 = 4 != 4

print("5 > 2 결과:", ans1)
print("4 != 4 결과:", ans2)

# ==============================
# [Example 02] 논리 연산자
# ==============================
stat1 = 2 < 4 and 5 > 1
stat2 = 4 > 6 or 9 < 0

print("논리 연산 결과 1:", stat1)
print("논리 연산 결과 2:", stat2)

# ==============================
# [Example 03] if 문 (값 보정)
# ==============================
cookie = int(input("숫자를 입력하세요: "))

if cookie < 0:
    cookie = cookie * (-1)

print("결과:", cookie)

# ====================================
# [Example 04] if-else 문 (짝수/홀수)
# ====================================
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print(num,"짝수입니다")
else:
    print(num, "홀수입니다.")

# ==============================
# [Example 05] if-elif 문
# ==============================
x = int(input("숫자를 입력하세요: "))

if x % 2 == 0:
    print("2의 배수입니다")
elif x % 3 == 0:
    print("3의 배수입니다")

# ==========================================
# [Example 06] if-elif-else 문 (숫자 맞추기)
# ==========================================
answer = 33
num = int(input("숫자를 입력하세요: "))

if num > answer:
    print("그 수보다 작아요")
elif num < answer:
    print("그 수보다 커요")
else:
    print("정답!")