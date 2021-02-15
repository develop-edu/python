# 문자열 더하기
str_a = '가나다'
str_b = 'abc'
print(str_a + str_b)

# 문자열 곱하기
print(str_a * 3)	# 가나다가나다가나다

# 문자열 길이 구하기
print(str_a + ' 길이:', len(str_a))	# '가나다 길이: 3'

# 인덱싱
print(str_a[1])	# 가
print(str_b[2])	# b

# 슬라이싱
print(str_a[0:2])	# 가나
print(str_b[1:])	# bc
print(str_a[-1])	# 다
print(str_a[:-1])	# 가나