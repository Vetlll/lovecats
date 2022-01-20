def cleaner(func):
    import re
    def wrapper(foo):
        foo = re.sub("[,.!$*+/\"\]]", "", foo)
        foo = foo.replace("\\", "")
        return func(foo)
    return wrapper
@cleaner
def foo(src):
    print(src)
foo('This is my special text, with special simbols. They are such as "!,$*+/\\]", but what a F..k')



import time

def cashing(fun):
    cash = dict()
    def func(*args):
        if args not in cash:
            cash[args] = fun(*args)
        return cash[args]
    return func
@cashing
def foo(x: int, y: int) -> int:
    result = x + y
    time.sleep(result)
    return result
print(foo(1, 1))
print(foo(1, 2))
print(foo(1, 2))
print(foo(2, 1))