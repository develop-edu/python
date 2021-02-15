lst = [1, 2, 'third', [3, 4]]
print(f'lst: {lst}\n')

# 인덱싱
print(f'lst[1]: {lst[1]}')	# 2
print(f'lst[3]: {lst[3]}')	# [3, 4]
print()

# 슬라이싱
print(f'lst[1:] : {lst[1:]}')
print()

# 연산하기; +, *, len()
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(f'{lst1} + {lst2} = {lst1 + lst2}')
print(f'{lst1} * 3 = {lst1 * 3}')
print(f'len(lst1) = {len(lst1)}')
print()

# 수정과 삭제
lst1[0] = 'abc'
print(f"change lst1[0] to 'abc' = {lst1}")
del lst1[1]
print(f'del lst1[1] = {lst1}')
