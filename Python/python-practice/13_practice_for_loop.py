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
Topic: Loop Practice with Strings

- 문자열을 대상으로 반복문 사용
- 숫자 포함 여부를 조건문으로 검사
- 조건 충족 시 break로 반복문 종료
"""

password = "abc123"
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
        break
if has_digit:
    print("숫자가 포함된 비밀번호 입니다")
else:
    print("숫자가 포함되어 있지 않습니다")

# --- Notes ---
# has_digit : 숫자가 포함되었는지를 저장하는 boolean 변수
# ch        : character의 약자, 문자열 반복 시 각 문자를 의미
# isdigit() : 문자열이 숫자일지 확인하는 메서드
#
# 💡 Learned
# break 사용하면 조건을 만족하는 순간 반복문을 종료할 수 있다. 