import keyword
# 주석 표현 한 줄 주석
"""
end는 출력문이 끝나는 지점에 어떻게 끝낼지! 디폴트는 \n
sep의 디폴드는 한 칸 띄어쓰기, 콤마로 나누어진 부분 사이에 특정 값는 넣음

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



