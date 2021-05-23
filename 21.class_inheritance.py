class Parent:
	def __init__(self, lastname):
		self.lastname = lastname
		
class Child(Parent):	# Parent 클래스 상속받기
	def __init__(self, lastname, name):
		super().__init__(lastname)
		self.name = name
		
	def whoami(self):
		print(f'I am {self.lastname}.{self.name}')

hong = Child( '홍', '길동')
hong.whoami()