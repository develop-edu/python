문자열 = '반복 문자열'
for 문자 in 문자열:
	print(문자)
print('-' * 24)

lst = [1, 2, 3, 'forth', [4, 5]]
for l in lst:
	print(l)
print('-' * 24)

tpl = ('first', 'second', 'third')
for t in tpl:
	print(t)
print('-' * 24)

lst_tpl = [(1, 2), (3, 4), (5, 6)]
for a, b in lst_tpl:
	print(f'{a} + {b} = {a + b}')
print('-' * 24)

for i in range(10):		# 0 <= i < 10
	print(i)
print('-' * 24)

for i in range(2, 10):	# 2 <= i < 10
	print(i)
print('-' * 24)

for i in range(1, 10, 2):	# 1, 3, 5, 7, 9
	print(i)
print('-' * 24)

print(f'{" 1부터 입력한 숫자까지 합 구하기 ":#^32}')
num = int(input('숫자를 입력하세요: '))
sum = 0
for i in range(num + 1):
	sum += i
print('합계는', sum, '입니다')
print('-' * 24)

### 구구단 출력하기 ###  --> 2중 반복문
for i in range(2, 10):
	for j in range(1, 10):
		print(f'{i} * {j} = {i * j:2}')
	print()

### 구구단 출력하기 ###  --> 3중 반복문
### 숙제~~  참조: gugudan.py

### 리스트 내포 사용 ###
a = [1, 2, 3, 4, 5]
result = []
for i in a:
	result.append(i ** 2)
print('1)', result)	# [1, 4, 9, 16, 25]

result = [i ** 2 for i in a]
print('2)', result)

# 전체 리스트 중 홀수만 추려서 10씩 곱하기
result = [i * 10 for i in a if i % 2 == 1]
print('3)', result)

'''
# 145page: 이 내용은 조금 과하다 싶음.
# 구구단의 모든 결과 담기
result = [x * y for x in range(2, 10)
	for y in range(1, 10)]
print(result)
'''