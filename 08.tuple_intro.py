t = (1, '문자열', [1,2,3])
for d in dir(t):
	if d.startswith('__'):
		continue
	print(f'{d}()')
print()

print(f't: {t}')
print()

#t[0] = 2	# TypeError: 'tuple' object does not support item assignment
#del t[1]	# TypeError: 'tuple' object doesn't support item deletion

print(f't[0]: {t[0]}')		# indexing
print(f't[1:]: {t[1:]}')	# slicing
print()

t1 = ('another', 5)
print(f't1: {t1}')
print(f't + t1: {t + t1}')	# 연산결과도 tuple
