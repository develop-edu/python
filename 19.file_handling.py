
## 파일 만들기
#f = open('new_file.txt', 'w')	# 이미 파일이 있으면 덮어쓰게 된다.
#f.write('새로운 파일')
#f.close()
#
## 파일 읽기
#f = open('new_file.txt', 'r')
#print(f.read())
#f.close()

'''
i = 0
for d in dir(f):
	if d.startswith('_'):
		continue
	print(d, end='(), ')
	i += 1
	if i % 5 == 0:
		print()

buffer(), close(), closed(), detach(), encoding(), 
errors(), fileno(), flush(), isatty(), line_buffering(), 
mode(), name(), newlines(), read(), readable(), 
readline(), readlines(), seek(), seekable(), tell(), 
truncate(), writable(), write(), writelines(), 
'''

# 여러 줄 쓰기
f = open('lines.txt', 'w')	# 이미 파일이 있으면 덮어쓰게 된다.
for i in range(1, 11):
	f.write(f'{i}번째 줄\n')
f.close()

# 여러 줄 읽기
f = open('lines.txt', 'r')
# read()로 한꺼번에 읽어들이기
#print(f.read())

# readline()로 한 줄씩 읽어들이기
while True:
	l = f.readline()
	if not l: 	# 읽은 줄이 없으면..
		break
	print(l)

# readlines()로 모든 줄 읽어들이기
#lines = f.readlines()
#for l in lines:
#	print(l)

f.close()

# append 모드
f = open('lines.txt', 'a')
for i in range(11, 21):
	f.write(f'{i}번째 줄\n')
f.close()

# with
with open('lines.txt', 'r') as f:
	for l in f.readlines():
		print(l.strip())
