# 기본 while 문
count = 0
while count < 10:
	count += 1	# count = count + 1
	print(f'{count}번 나무를 찍었습니다.')
	if count == 10:
		print('나무 넘어갑니다 !!!')
print('끝')

print(f'{"과일 사러 가기":#^32}')
메뉴 = '\n' + '-' * 24 + '\n1)과일 구경하기\n2)과일 사기\n3)계산하기\n4)장보기 끝'
num = 0
while num != 4:		# 조건 만족시까지 반복
	print(메뉴)
	msg = input('\n번호를 입력하세요: ')
	num = int(msg, base=10)
	if num == 1:
		print('사과, 망고가 있네요')
	elif num == 2:
		print('사과 2개 살게요~')
	elif num == 3:
		print('계산이요')
	elif num == 4:
		print('장 다 봤어요')
	else:
		print('1 ~ 4까지 번호를 입력하세요')
print()

# break 활용
print(f'{" break 활용 ":#^24}')
count = 0
while count < 3:
	count += 1
	if count == 2:
		break
	print(count)
print()

# continue 활용
print(f'{" continue 활용 ":#^24}')
count = 0
while count < 3:
	count += 1
	if count == 2:
		continue
	print(count)
print('*' * 32)

import random
print(f'{" 숫자 맞추기 게임(1 ~ 99) ":#^32}')
num = random.randint(1, 100)
while True:	# 무한 반복
	i = int(input('숫자(1 ~ 99)를 입력하세요: '))
	if num > i:
		print(f'{i}보다 큰 숫자입니다.')
	elif num < i:
		print(f'{i}보다 작은 숫자입니다.')
	else:
		print('정답입니다')
		break
