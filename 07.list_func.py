lst = [1, 2, 'third', [3, 4]]
i = 0
print('{0:#^48}'.format(' 리스트 함수들 '))
for fx in dir(lst):
	if fx.startswith('__'):
		continue
	print(fx, end = '( ), ')
	i += 1
	if i % 5 == 0:
		print()
print('\n')

print(f'lst: {lst}') 
# append( ); 뒤에 데이터를 붙인다.
lst.append(5)	# 데이터 추가
print(f'lst.append(5): {lst}')

# sort( )		# 정렬하기
lst = [1,65,3,5,32,9]
lst.sort()	# reverse = False(default), True; Similar with sorted(lst)
print(f'lst.sort(): {lst}')

# reverse( )	# 순서 뒤집기
lst = [1,65,3,5,32,9]
lst.reverse()
print(f'lst.reverse(): {lst}')

# index( )		# 인덱스
lst = [1,65,3,5,32,9]
print(f'lst.index(5): {lst.index(5)}')	# 인자에 해당하는 항목이 없을 경우 예외발생.

# insert( )		# 삽입
lst.insert(3, '추가')	# 첫번째 인자가 lst의 길이를 초과하는 경우, 마지막에 추가된다.
print(f"lst.insert(3, '추가'): {lst}")

# remove( )		# 제거
lst.remove('추가')		# 해당되는 항목이 없을 경우 ValueError 발생
print(f"lst.remove('추가'): {lst}")

# pop( )		# 끝에서 추출. 빈 리스트이면 IndexError 발생


# count( )		# 카운팅


# extend( )		# 리스트 연장
