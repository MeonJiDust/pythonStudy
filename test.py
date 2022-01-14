from decimal import Decimal as dc
"""a = 5
b = 3
print(a, b)
a, b = b, a
print(a, b)

a = 1, 3, 5

print(a)

x, y, z = a

print(f'x: {x}, y: {y}, z: {z}')"""

"""data = {'1': 'one', '2': 'two', 1: 1, 2: 2, (1, 2): '12'}

data[3] = 'three'

result = data.keys()
print(result)
print(type(result))
print(list(result))

result2 = data.items()
print(list(result2))
print(data[3])

del data['1']

check = ['1', '2', '3']

for num in check:
    value = data.get(num)

    if value:
        print(value)
    else:
        print(value)

print(data) # 키 값에는 수정 가능한 객체가 오면 안 된다.
#튜플은 수정 불가능한 객체"""

"""person = ['A', 'B', 'A', 'AB', 'O', 'AB', 'B', 'A', 'AB']
result = {}

for blood in person:
    if result.get(blood):
        result[blood] = result[blood] + 1
    else:
        result[blood] = 1

print(result)"""

"""#집합: set()
person = ['A', 'B', 'A', 'AB', 'O', 'AB', 'B', 'A', 'AB']
print(list(set(person)))

data = [[0] * 5 for _ in range(5)]

for line in data:
    print(line)
"""

"""value = 1 << 1

numbers = 0

try:
    number =  int(input("input: "))
except Exception as e:
    number = -1
    print(e)

print(number)

value = dc('1.2')
print(value)"""



