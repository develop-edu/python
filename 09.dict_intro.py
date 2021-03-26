dic = {1:'first', 2:'second'}
i = 0
for d in dir(dic):
	if d.startswith('__'):
		continue
	print(f'{d}()', end=', ')
	i += 1
	if i % 5 == 0:
		print()
print()

print(dic)
dic[3] = 'third'
print(f'추가: {dic}')
dic[3] = '세번째'
print(f'수정: {dic}')
del dic[3]
print(f'삭제: {dic}')
print()
