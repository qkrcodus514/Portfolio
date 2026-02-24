"""
📘 Python Study Examples

- Core concept examples only
- Detailed explanations are documented in README.md
- Practice and experimental code is maintained separately
"""
 
#===============================
# [Example 01] for문
#===============================

# --- Pattern 1: Iteration Over Elements (Direct Access) ---
scores = [95, 82, 76, 64, 74, 58]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"

    print(f"[Result] Score = {score}, Grade = {grade}")


# --- Pattern 2: Filtering Pattern ---
scores = [45, 78, 88, 59, 92]
passed = []

for score in scores:
    if score >= 60:
        passed.append(score)

print("합격자 점수", passed)


#===============================
# [Example 02] range()문
#===============================

# --- Pattern 1: Index-Based Iteration ---
names = ["Tom", "Keria", "Faker"]
scores = [98, 92, 87]

for i in range(len(names)):
    print(f"{i+1}번 학생 {names[i]}의 점수는 {scores[i]}점 입니다.")


# --- Pattern 2: Accumulation Pattern ---
scores = [88, 79, 47, 95, 29]
total = 0

for i in range(len(scores)):
    total += scores[i]

average = total / len(scores)

print(f"총점: {total}")
print(f"평균: {average}")


#===============================
# [Example 03] while문
#===============================

# --- Pattern 1: Counter Pattern (누적 계산) ---
i = 1
total = 0
while i <= 10:
    total += i
    i += 1

print(f"1부터 10까지의 합: {total}")


# --- Pattern 2: Sentinel Pattern (특정 입력까지 반복) ---
user_input = ""

while user_input != "exit":
    user_input = input("문자를 입력하세요 (종료: exit): ")
    print(f"입력한 값: {user_input}")

print("프로그램 종료")


# --- Pattern 3: Validation Pattern (검증 반복) ---
correct_password = "1234"
input_password = ""

while input_password != correct_password:
    input_password = input("비밀번호를 입력하세요: ")

print("접속 성공!")


# --- Pattern: Interactive Guessing Game ---
answer = 7
guess = 0

while guess != answer:
    guess = int(input("1~10 사이 숫자를 입력하세요: "))

    if guess < answer:
        print("너무 작아요")
    elif guess > answer:
        print("너무 커요")
    else:
        print("정답입니다")


# --- Pattern 4: Infinite Loop + break ---
while True:
    print("1. 시작")
    print("2. 종료")

    choice = input("번호를 선택하세요 ")

    if choice == "1":
        print("프로그램 시작!")
    elif choice == "2":
        print("프로그램 종료!")
        break
    else:
        print("잘못된 입력입니다.")


# --- Pattern 5: Countdown Pattern ---
count = 5

while count > 0:
    print(f"카운트다운: {count}")
    count -= 1

print("발사")


#===============================
# [Example 04] break문
#===============================

# --- Pattern: Early Termination ---
email = "student123@gmail.com"
user_id = ""

# "ch" = "character"
for ch in email:
    if ch == "@":
        break
    user_id += ch

print("아이디:", user_id)


