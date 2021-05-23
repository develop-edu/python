import mod1	# mod1.py가 현재 파일과 같은 폴더에 있다.

print(mod1.add(3, 4))
print(mod1.sub(5, 2))

'''
from mod1 import add	# mod1 모듈에서 add함수만 추가
from mod1 import add, sub # mod1 모듈에서 add, sub함수 추가
from mod1 import *		# mod1 모듈 내의 모든 항목 추가

print(add(3, 4))	# mod1의 add()함수 호출
'''