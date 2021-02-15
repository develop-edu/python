s = ' abcdDEEFgh'
i = 0
print('{0:#^48}'.format(' 문자열 함수들 '))
for fx in dir(s):
	if fx.startswith('__'):
		continue
	print(fx, end = '( ), ')
	i += 1
	if i % 5 == 0:
		print()

print('s:', s)

# count( )
print(f"d의 개수: {s.count('d')}")
print(f"E의 개수: {s.count('E')}")
print()

# find( ), index( )
print(f"find('d'): {s.find('d')}")
print(f"index('d'): {s.index('d')}")
print(f"find('e'): {s.find('e')}")
#print(f"index('e'): {s.index('e')}")	# ValueError: substring not found
print()

# join( )
print(f"','join(): {','.join(s)}")	# s 문자열 사이에 ',' 추가
print()

# upper( ), lower( )
print(f"'{s}'.upper(): '{s.upper()}'")
print(f"'{s}'.lower(): '{s.lower()}'")
print()

s2 = s + '  '
print(f'Spaced string:[{s2}]')
# lstrip( ), rstrip( ), strip( )
print(f'lstrip(): [{s2.lstrip()}]')
print(f'rstrip(): [{s2.rstrip()}]')
print(f'strip(): [{s2.strip()}]')
print()

# replace( )
py = 'Pithon'
print(f"{py}.replace('i', 'y'): {py.replace('i', 'y')}")
print()

# split( ) --> default: ' '
info = '2020-09-11,108,22.4,19.2,27.1'
data = info.split(',')	# data: list type
for d in data:
	print(d)
