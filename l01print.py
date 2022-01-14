import copy
"""import keyword
# 주석 표현 한 줄 주석
"""
'''
end는 출력문이 끝나는 지점에 어떻게 끝낼지! 디폴트는 \n
sep의 디폴드는 한 칸 띄어쓰기, 콤마로 나누어진 부분 사이에 특정 값는 넣음
'''
"""
print("hi hello", end=' ')
print("hi my name is sihyun", end="! ")

print("안녕", "파이썬", sep='!')

print(keyword.kwlist)
print(dir(keyword))

print("3" + '5')

print(f'{3}' + '5')

num = [3, 5]
print(f'{max(num)}5')
print(type('3'))

value = 5 / 2
value2 = int(5 / 2)
print(value)
print(value2)

num1 = 3 ** 5
print(num1)

print(1.2 - 0.1)

print('\'Python\'s easy\'')

print("Pyhon's easy")
#''문자열 Python's easy!

data = 'Python'
print(data[len(data) - 1])

# 시작점 : 끝점 : 증감정도 (끝점 포함X)
print(data[0:3:2])
print(data[-1:-5:-1])

# 숫자 -> 문자
# 문자(Char) -> 숫자

print(chr(97)) # --> 숫자에서 문자
print(ord('a')) # --> 문자에서 숫자
print(ord('A')) # --> 문자에서 숫자

for i in range(10):
    print(i)

# for 변수 in iterable
# for 변수 in range(len(interable)):

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")


for i in range(10):
    if i == 5:
        break
    print(i)

for idx, value in enumerate(range(10, 20)): #enumerate는 인덱싱을 할 수 이따

    print(f"idx: {idx} / value: {value}")

num = int(input("input num: "))

print(type(num))
if num > 3:
    print(f"{num} > 3이다")
else:
    print(f"{num} < 3이다")


"""
"""for i in range(1, 32):
    if ((i % 10) == 3) or ((i % 10) == 6) or ((i % 10) == 9):
        print("박수")
    elif i // 10 == 3:
        print("박수")
    else:
        print(i)


num = int(input("input! "))

if num > 5:
    result = True
else:
    result = False

print(result)
result2 = True if num > 5 else False
print(result2)"""

"""value = [1, 2, 3, 2]
value[0] = "p"
print(value)

result = value.pop()

print(f"꺼내온 값: {result}")

print(value)"""

"""del(value)
print(value)"""

"""value2 = [1, 2, 3]

value2.append(4)
print(value2)
value2.insert(2, -1)
print(value2)

value3 = [3, 1, 2]
value4 = [3, 1, 2]

result = value3.sort()

result1 = sorted(value3)
print(value3)
print(result)
print(result1)

value4.reverse()
print(value4)

# print(sorted(value4, reverse=True))

value = [3, 1, 2, 3]

idx = value.extend([2, 4])

print(idx)"""

"""person = ['A', 'B', 'A', 'AB', 'O', 'AB', 'B', 'A', 'AB']
a = 0
b = 0
o = 0
ab = 0

for i in range(len(person)):

    if person[i] == 'A':
        a += 1
    elif person[i] == 'B':
        b += 1
    elif person[i] == 'O':
        o += 1
    elif person[i] == "AB":
        ab += 1

print(f"{a}, {b}, {o}, {ab}")


list_data = ['최웅', 77, '국연수', 93, '김지웅', 91, '엔제이', 88, '이솔이', 75]

max_num = list_data[1]
result = 1

for i in range(1, len(list_data), 2):

    if list_data[i] > max_num:
        max_num = list_data[i]
        result = i

print(list_data[result - 1])
print(list_data[result])

count = 1
graph = [[0] * 5 for _ in range(5)]

for i  in range(0, 5):
    for j in range(0, 5):
        graph[i][j] = count
        count += 1

print(graph)

data = [1, 2, 3]
copy_data = data

print(copy_data)
copy_data[1] = 5
print(copy_data)

print(data)

data = [1, 2, 3]

copy_data = data[:]
print(id(data[1]))
print(id(copy_data[1]))
copy_data[1] = 5
print(id(copy_data[1]))

data = [[1, 2], [3, 4]]

copy_data = copy.deepcopy(data)

copy_data[1] = 5

print(data)
print(copy_data)

arr = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]"""