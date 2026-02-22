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
Topic: Sequence Operations

- 음수 인덱싱
- in 연산자
- len() 함수
- 연결(+) 연산자
- 반복(*) 연산자
"""


# --- 음수 인덱싱 (Negative Indexing) ---


numbers = [10, 20, 30, 40, 50]

print("원본 리스트:", numbers)
print("마지막 요소:", numbers[-1])
print("뒤에서 두 번째 요소:", numbers[-2])

text = "Python"

print("문자열:", text)
print("마지막 문자:", text[-1])
print("뒤에서 세 번째 문자:", text[-3])

# 💡 Learned
# 음수 인덱스는 뒤에서부터 접근한다.
# 리스트와 문자열 모두 동일한 방식으로 동작한다.



# --- in 연산자 (Membership Test) ---


print("\n--- in 연산자 테스트 ---")

print("30이 numbers 안에 있는가?", 30 in numbers)
print("100이 numbers 안에 있는가?", 100 in numbers)

print("'P'가 text 안에 있는가?", "P" in text)
print("'z'가 text 안에 있는가?", "z" in text)

# 조건문과 함께 사용
if 40 in numbers:
    print("40은 리스트에 존재합니다.")

# 💡 Learned
# in 연산자는 특정 값이 시퀀스 안에 존재하는지 True/False로 반환한다.



# --- len() 함수 ---


print("\n--- len() 함수 ---")

print("numbers의 길이:", len(numbers))
print("text의 길이:", len(text))

empty_list = []
print("빈 리스트 길이:", len(empty_list))

# 💡 Learned 
# len()은 시퀀스의 요소 개수를 반환한다.
# 빈 시퀀스의 길이는 0이다.



# --- 연결 연산자 (+) ---


print("\n--- 연결 연산자 ---")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2
print("list1:", list1)
print("list2:", list2)
print("연결 결과:", combined_list)

str1 = "Hello"
str2 = "World"

combined_str = str1 + " " + str2
print("문자열 연결:", combined_str)

# 💡 Learned 
# + 연산자는 시퀀스를 이어 붙인다.
# 원본은 변경되지 않고 새로운 시퀀스가 생성된다.



# --- 반복 연산자 (*) ---


print("\n--- 반복 연산자 ---")

repeat_list = [1, 2] * 3
print("[1, 2] * 3 결과:", repeat_list)

repeat_str = "Hi! " * 3
print("'Hi! ' * 3 결과:", repeat_str)

# 💡 Learned
# * 연산자는 시퀀스를 지정한 횟수만큼 반복한다.
# 리스트와 문자열 모두 동일하게 동작한다.



# --- 종합 실험 (Mini Practice) ---


print("\n--- 종합 실험 ---")

data = ["apple", "banana", "cherry"]

print("데이터:", data)
print("데이터 개수:", len(data))

if "banana" in data:
    print("banana는 데이터에 포함되어 있습니다.")

extended_data = data + ["orange"]
print("확장된 데이터:", extended_data)

repeated_data = data * 2
print("반복된 데이터:", repeated_data)

print("마지막 요소:", data[-1])

# 💡 Final Reflection
# - 리스트와 문자열은 공통적으로 '시퀀스'이다.
# - 인덱싱, 길이 확인, 포함 여부 검사, 연결, 반복이 가능하다.
# - 대부분의 동작 방식이 서로 유사하다.