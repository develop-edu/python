class Calculator:
	def __init__(self, a, b):	# 생성자(Constructor)
		self.a = a		# 객체 변수 a 생성
		self.b = b		# 객체 변수 b 생성
		
	def add(self):	# 더하기
		print(f'{self.a} + {self.b} = {self.a + self.b}')
		
	def sub(self):	# 빼기
		print(f'{self.a} - {self.b} = {self.a - self.b}')

	def mul(self):	# 곱하기
		print(f'{self.a} * {self.b} = {self.a * self.b}')
		
	def div(self):	# 나누기
		print(f'{self.a} / {self.b} = {self.a / self.b : 0.2f}')

cal1 = Calculator(3, 7)
cal2 = Calculator(2, 5)
cal1.add()
cal1.sub()
cal2.mul()
cal2.div()
