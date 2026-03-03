"""
📘 Python Study Examples

- Core concept examples only
- Detailed explanations are documented in README.md
- Practice and experimental code is maintained separately
"""

#===============================
# [Example 01] 음수 인덱싱
#===============================

# --- Pattern 1: Access From the End ---
fruit = "Watermelon"

print("인덱싱 결과:", fruit[1])
print("마지막 문자:", fruit[-1])
print("뒤에서 세 번째 문자", fruit[-3])

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

result = numbers[-5:-2]
print("numbers[-5:-2] 결과", result)


#============================================
# [Example 02] 시작 인덱스 생략 슬라이싱 예제
#============================================

# --- Pattern 2: Negative Slice Range ---
letters = ["I", "L", "O", "V", "E", "Y", "O", "U"]

print("슬라이싱 결과:", letters[:3])
print("슬라이싱 결과:", letters[:])

filename = "report.pdf"

result = filename[:-4]
print("확장자 제거 결과", result)


#============================================
# [Example 03] 끝 인덱스를 생략한 슬라이싱 예제
#============================================

characters = ["M", "O", "M", "A", "N", "D", "D", "A", "D"]

print("슬라이싱 결과:", characters[5:])
print("슬라이싱 결과:", characters[3:])

email = "user@example.com"

result = email[:4]
print("아이디 부분:", result)


#===============================
# [Example 04] in 연산자
#===============================

# --- Pattern 1: Membership in List ---
numbers = [1, 3, 5, 7, 9]

print("5가 리스트에 있는가?", 5 in numbers)
print("2가 리스트에 있는가?", 2 in numbers)


# --- Pattern 2: Membership in String ---
message = "Python is fun"

print("'P'가 포함되어 있는가?", 'P' in message)
print("'Java'가 포함되어 있는가?", 'Java' in message)


# --- Pattern 3: Dictionary Key Membership ---
student_score = {
"철수": 90,
"영희": 85,
"상혁": 95
}

print("철수가 있는가?", "철수" in student_score)
print("90이 key로 존재하는가?", 90 in student_score) # False

# 값 검색은 values() 사용
print("90이 값으로 존재하는가?", 90 in student_score.values())


#===============================
# [Example 05] len() 활용
#===============================

# Length of different data types
numbers = [10, 20, 30, 40, 50]

print("리스트의 길이:", len(numbers))

text = "sweet home"

print("문자열 길이:", len(text))

student_score = {
"Mark": 90,
"Jack": 85,
"Justin": 88
}

print("학생 수:", len(student_score))

data = [1, 7, 3, 15, 27, 35, 49, 56]

print("마지막 요소(len 사용):", data[len(data)-1])
print("마지막 요소 (음수 인덱싱):", data[-1])

scores = [95, 88, 76, 92, 85]

result = scores[:len(scores) // 2]
print("앞쪽 절반 데이터:", result)


# Using len() for logic
password = "abc123"

if len(password) >= 6:
    print("사용 가능한 비밀번호입니다.")
else:
    print("비밀번호가 너무 짧습니다.")

#===============================
# [Example 06] 연결 연산
#===============================

first = "Welcome"
second = "Home"

result = first + " " + second
print("문자열 연결 결과:", result)

num1 = [1, 2, 3]
num2 = [4, 5, 6]

result = num1 + num2
print("리스트 연결 결과:", result)

age = 23

print("나이:", age)
print("나이: " + str(age))


#===============================
# [Example 07] 반복 연산
#===============================

star = "*"

print(star * 5)

numbers = [1,7]

result = numbers * 3
print("리스트 반복 결과:", result)

