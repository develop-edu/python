def no_arg():
	print('This is the no_arg function')

def introduce(name):	# 반환값 없음
	print(f'My name is {name}')

no_arg()	# 매개변수(인자, argument)가 없음
introduce('John')
print()

def add(a, b):
	print(f'덧셈연산: {a} + {b}')
	return a + b

a = 3
b = 5
print(f'{a} + {b} = {add(a, b)}')
print(f'{a} + {b} = {add(b=b, a=a)}')	 # 매개변수 지정
print()
#------------
def add_many(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print(f'add_many(1, 2) = {add_many(1, 2)}')
print(f'add_many(1, 3, 5, 7, 9) = {add_many(1, 3, 5, 7, 9)}')
print()

def calculate(operator, *args):
	if operator == '+':
		result = 0
		for i in args:
			result += i
	elif operator == '*':
		result = 1
		for i in args:
			result *= i
	
	return result

print(f'calculate(\'+\', 2, 3, 4) = {calculate("+", 2, 3, 4)}')
print(f'calculate(\'*\', 2, 3, 4) = {calculate("*", 2, 3, 4)}')
print()

def print_kwargs(**kwargs):	# Dictionary type 
	print(kwargs)
	
print_kwargs(a = 1)
print_kwargs(name = 'kim', num = 23)
print()

# 여러 값 반환하는 함수
def add_mul(a, b):
	return a + b, a * b	# tuple

a = 3
b = 7
print(f'{"여러 값 반환하는 함수":-^32}')
print(f'add_mul({a}, {b}) = {add_mul(a, b)}')

# 반환값이 없는 함수 종료하기
def not_fool(nick):
	if nick=='fool':
		print('[Warning]')
		return
	
	print(f'{nick} is not a fool')

not_fool('James')
not_fool('fool')

# initialized arguments
print(f'{"초기값 정해진 매개변수":-^32}')
def say_myself(name, old, man=True):
	print(f'나의 이름은 {name}입니다.')
	print(f'나이는 {old}입니다.')
	if man:
		print('남자입니다')
	else:
		print('여자입니다')

say_myself('홍길동', 17)
say_myself('신사임당', 1000, False)
print()

# global
print(f'{"global test":-^32}')
a = 1
def test(a):
	a += 100
print('before test:', a)
test(a)
print('after test:', a)

def use_global():
	global a
	a += 200
print('before use_global:', a)
use_global()
print('after use_global:', a)
print()

# lambda(익명함수)
'''
def sum(a, b):
	return a + b
'''
sum = lambda a, b : a + b
print(f'sum(3, 4) = {sum(3, 4)}')

print('람다식에서 조건문 사용하기')
print((lambda n, m: n if n % 2 == 0 else m)(1, 3))
print((lambda n, m: n if n % 2 == 0 else m)(2, 3))

sq = list(map(lambda x : x ** 2, range(5)))
print(sq)

def square(lst):
	ll = []
	for i in lst:
		ll.append(i ** 2)
	return ll

lst = [1, 5, 7, 4, 9]
print(square(lst))


