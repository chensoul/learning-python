#!/usr/bin/env python
# coding=utf-8

def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 159

fib
f = fib
f(100)

fib(0)
print(fib(0))


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")  # output: Hello, Alice!
greet("Bob", "Hi")  # output: Hi, Bob!


def create_user(name, age=18, gender="male", email=None):
    user = {"name": name, "age": age, "gender": gender}
    if email:
        user["email"] = email
    return user


user1 = create_user("Alice")
user2 = create_user("Bob", 20)
user3 = create_user("Charlie", gender="female", email="charlie@example.com")

print(user1)  # output: {'name': 'Alice', 'age': 18, 'gender': 'male'}
print(user2)  # output: {'name': 'Bob', 'age': 20, 'gender': 'male'}
print(user3)  # output: {'name': 'Charlie', 'age': 18, 'gender': 'female', 'email': 'charlie@example.com'}


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)  # 2
standard_arg(arg=2)  # 2

pos_only_arg(1)  # 1
kwd_only_arg(arg=3)  # 3

combined_example(1, 2, kwd_only=3)  # 1 2 3
combined_example(1, standard=2, kwd_only=3)  # 1 2 3


def foo(name, **kwds):
    return 'name' in kwds


# foo(1, **{'name': 2})
# TypeError: foo() got multiple values for argument 'name'


def foo(name, /, **kwds):
    return 'name' in kwds


foo(1, **{'name': 2})  # True


def concat(*args, sep="/"):
    return sep.join(args)


concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

list(range(3, 6))  # normal call with separate arguments
args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
f(0)
f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
