
# 문자열 인덱싱 예제
word = 'world'

print('문자열 인덱싱 결과:', word[1])


# 리스트 인덱싱 및 값 변경
animal = ['dog', 'cat', 'watermelon']
animal[2] = 'lion'

print('변경된 리스트:', animal)

# 리스트 슬라이싱 예제
beta = [2, 4, 6, 8, 10, 12, 14]

# 슬라이싱은 종료 인덱스를 포함하지 않음
print('슬라이싱 결과:', beta[2:5])

# 중첩 리스트 인덱싱 예제
words = [1, 2, ['a', 'b', ['Life', 'is']]]

result = words[2][2][0]

print('중첩 리스트에서 가져온 값:', result)

# input() 예제
name = input('이름을 입력하세요: ')

print('안녕하세요', name)

# 형 변환 예제: 문자열을 정수로 변환
a = '345'

print('a의 타입은:', type(a))

b = int('345')

print('b의 타입은:', type(b))

