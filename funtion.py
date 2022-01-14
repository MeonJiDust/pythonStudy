"""def f(num):
    if num > 0:
        return num ** 2
    else:
        print("안 돼!!")

result = f(-1)
print(f(5))
print(result)

def fc(*args):
    print(args)
    print(type(args))

fc('hi', 'hello', 'hii')

def fcc(first, **kwargs): # *args, **kwargs는 나머지를 처리하는 것이기 때문에 **kwargs가 앞에 오면 안 됌

    print(first)
    print(kwargs)

fcc(first='hi' ,two='hello', three='hihi')

def fcfc(x, y = 3):
    print(x ** y)

fcfc(3, 5)

f = lambda x, y=3: print(x ** y)

f(3)"""

"""(lambda x, y = 3: print(x ** y))(5)"""


"""def f():
    num = 0

    if num < 1000:
        print("확인")
        num += 1
        return f()
    else:
        return print("Rmx")

f()"""

num = int(input("입력해!!"))

def factorial(num):

    sum = 1
    for i in range(1, num + 1):
        sum *= i

    return sum

print(factorial(num))

sum = 1
def factorial2(num):
    if num ==1:
        return 1
    return num * factorial2(num-1)

print(factorial2(num))
