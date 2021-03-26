lst1 = [1, 2, 3]
print(f'lst1\' address: {id(lst1)}')   # 주소값은 실행할 때마다 달라질 수 있다.
print()

lst2 = lst1
print(f'lst1: {lst1} @ {id(lst1)}')
print(f'lst2: {lst2} @ {id(lst2)}')

lst2[1] = 7
print('-- After lst[2]=3 --')
print(f'lst1: {lst1}')
print(f'lst2: {lst2}')
print('\n')

##############
# 얕은 복사
##############
lst1 = [1, 2, 3]
print('[[ Shallow Copy ]]')
#1. [:]
lst2 = lst1[:]
print('-- [:] --')
print(f'lst1: {lst1} @ {id(lst1)}')
print(f'lst2: {lst2} @ {id(lst2)}')

lst2[1] = 5
print('-- After lst2[1]=5 --')
print(f'lst1: {lst1}')
print(f'lst2: {lst2}')
print()

#2. copy 모듈 사용
import copy
lst1 = [1, 2, 3]
lst2 = copy.copy(lst1)
print('-- copy.copy() --')
print(f'lst1: {lst1} @ {id(lst1)}')
print(f'lst2: {lst2} @ {id(lst2)}')

lst2[1] = 5
print('-- After lst2[1] = 5 --')
print(f'lst1: {lst1}')
print(f'lst2: {lst2}')
print()

lst1 = [[1, 2], [3, 4]]  # 2차원 리스트
lst2 = copy.copy(lst1)
print('-- copy.copy() 2 --')
print(f'lst1: {lst1} @ {id(lst1)}')
print(f'lst2: {lst2} @ {id(lst2)}')
lst1[1][0] = 7
print('-- After lst1[1][0] = 7 --')
print(f'lst1: {lst1}')
print(f'lst2: {lst2}')
print()

##############
# 깊은 복사
##############
import copy
print('[[ Deep Copy ]]')
lst1 = [[1, 2], [3, 4]]
lst2 = copy.deepcopy(lst1)
print('-- copy.deepcopy() --')
print(f'lst1: {lst1} @ {id(lst1)}')
print(f'lst2: {lst2} @ {id(lst2)}')
lst1[1][0] = 7
print('-- After lst1[1][0] = 7 --')
print(f'lst1: {lst1}')
print(f'lst2: {lst2}')
print()

##############
# 변수 만드는 방법
##############
# tuple
a, b = ('first', 'second')
print(f'a:{a}, b:{b}')
(a, b) = 'first', 'second'
print(f'a:{a}, b:{b}')
# list
[a, b] = ['first', 'second']
print(f'a:{a}, b:{b}')

a = b = 'python'  # 같은 값 대입
print(f'id(a):{id(a)}, id(b):{id(b)}')

print('*' * 32)
a = 7
b = 3
print(f'a:{a}, b:{b}')
a, b = b, a  #
print(f'a:{a}, b:{b}')
