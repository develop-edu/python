# 정수 포맷팅
i = 3
j = 5
print('i: %2d' % i)				# i:  3
print('j: {0:03d}'.format(j))	# j: 005
print(f'i * j = {i * j : 3}')	# i * j =  15

# 문자열 포맷팅
s = 'abcdDEEFgh'
print('s: %s, s[1]: %c' % (s, s[1]))
print('s[2:5]: {0}'.format(s[2:5]))
print(f's[3:-1]: {s[3:-1]}')

# 부동소수점 포맷팅
pi = 3.141592654
print('pi: %.2f' % pi)
print('pi: {0:.3f}'.format(pi))
print(f'pi: {pi:.4f}')

# 퍼센트
per = 82.5
print('퍼센트: %.1f%%' % per)
print('퍼센트: {0:.1f}%'.format(per))
print(f'퍼센트: {per:.1f}%')