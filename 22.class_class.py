class Student:
	total = 0	# 클래스 변수
	
	def __init__(self, num, name):
		self.num = num	# 객체 변수
		self.name = name
		Student.total += 1
		
	@classmethod	# 다음 메서드가 클래스 메서드임을 선언
	def getTotal(self):
		#print(self.num)	# 에러 발생. 클래스 메서드 내에서는 객체 변수를 호출할 수 없음.
		return Student.total

st1 = Student(3, '홍길동')
print(f'Total: {st1.getTotal()}')		# 클래스 메서드이지만, 인스턴스 메서드 형태로 호출 가능.
st2 = Student(5, '장길산')
print(f'Total: {Student.getTotal()}')	# 클래스 메서드 호출