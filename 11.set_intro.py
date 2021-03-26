s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(f's1:{s1}')
print(f's2:{s2}')

# 합집합
u = s1 | s2
s = s1.union(s2)
print(f'합집합: {u} or {s}')

# 교집합
i = s1 & s2
s = s1.intersection(s2)
print(f'교집합: {i} or {s}')

# 차집합
print(f'차집합: {s1 - s2}')

# 배타적 논리합
print(f'배타합: {s1 ^ s2}')