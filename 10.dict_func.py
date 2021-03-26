dic = {1:'first', 2:'second', 3:'third'}
print(f'dic: {dic}')

# keys( )
print(f'keys: {dic.keys()}')	# dict_keys()
# values( )
print(f'values: {dic.values()}')	# dict_values()
print()

# items( )
for k, v in dic.items():
	print(f'key:{k}, value:{v}')
print()
	
# clear( )
dic.clear()
print(f'After clear: {dic}')

# get( )
dic = {1:'first', 2:'second', 3:'third'}
print(f'dic[1]: {dic[1]}')
print(f'dic.get(1): {dic.get(1)}')
#print(f'dic[4]: {dic[4]}')	# KeyError: 4
print(f'dic.get(4): {dic.get(4)}')	# return None
print()

# in ; __contain__(key)
print(f'2 in dic: {2 in dic}')
print(f'5 in dic: {5 in dic}')