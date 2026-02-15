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
Topic: Basic Syntax Practice
(print, calculation, input, conditional statements)

- 기본 출력 연습
- 섭씨 → 화씨 변환
- 숫자 자릿수 판별
- 점수에 따른 등급 판별
"""



# 1. print() 출력 연습
print('*')
print('**')
print('***')
print('****')
print('*****')

print('-' * 30)

# 2. 섭씨 → 화씨 변환
celsius = 18
fahrenheit = celsius * (9 / 5) + 32
print('섭씨 18도는 화씨로:', fahrenheit)

print('-' * 30)

# 3. 숫자 자릿수 판별
num = int(input('숫자를 입력하세요: '))

if 1 <= num <= 9:
    print('한 자리 숫자입니다.')
elif 10 <= num <= 99:
    print('두 자리 숫자입니다.')
else:
    print('세 자리 숫자 이상입니다.')

print('-' * 30)

# 4. 점수에 따른 학점 판별
score = int(input('점수를 입력하세요: '))

if score == 0:
    print('학점: F')
elif 0 < score < 77:
    print('학점: B+')
elif 77 <= score < 88:
    print('학점: A0')
else:
    print('학점: A+')