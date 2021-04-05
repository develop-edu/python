money = True
if money:
	print('택시 타고 간다')
else:
	print('걸어서 간다')
print()

print(f'{"비교 연산자":-^32}')
x = 65
y = 96
if x < y:
	print(f'{y}는 {x}보다 크다')
else:
	print(f'{y}는 {x}보다 작다')

if x > y:
	print(f'{x}는 {y}보다 크다')
else:
	print(f'{x}는 {y}보다 작다')

if x == y:
	print(f'{x}는 {y}와 같다')
else:
	print(f'{x}는 {y}와 다르다')

if x >= y:
	print(f'{x}는 {y}보다 같거나 크다')
else:
	print(f'{x}는 {y}보다 작다')
print()

print(f'{"점수에 따른 성적표":-^32}')
점수 = 87
if 점수 >= 90:
	성적 = '수'
elif 점수 >= 80:	# 80 <= 점수 < 90
	성적 = '우'
elif 점수 >= 70:	# 70 <= 점수 < 80
	성적 = '미'
elif 점수 >= 60:	# 60 <= 점수 < 70
	성적 = '양'
else:
	성적 = '가'
print(f'점수:{점수}, 성적:{성적}')
print()

print(f'{"논리 연산자":-^32}')
돈 = 5000
카드 = True
if 돈 > 3000 or 카드:
	print('택시 타고 간다')
else:
	print('걸어 간다')
print()

print(f'{"포함 연산자":-^32}')
리스트 = [1, 2, 3]		# (1, 2, 3)
if 1 in 리스트:
	print(f'{리스트} 안에 1이 포함되어 있습니다')
else:
	print(f'{리스트} 안에 1이 포함되어 있지 않습니다')

문자열 = '가나다라마바사아자차카타파하'
if '김' in 문자열:
	print(f'\'{문자열}\' 안에 \'김\'이 포함되어 있습니다')
else:
	print(f'\'{문자열}\' 안에 \'김\'이 포함되어 있지 않습니다')

과일가게 = ['사과', '바나나', '샤인머스캣', '망고', '파인애플', '포도']
print(과일가게)
과일 = '람부탄'
if 과일 in 과일가게:
	print(f'{과일}을 샀습니다')
else:
	print(f'{과일}은(는) 팔지 않습니다.')

# -------------
print(f'{"pass 예제":-^32}')
if '참외' in 과일가게:
	pass
else:
	print(f'참외는 다 팔렸습니다.')


