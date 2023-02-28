def foo():
    for i in range(1,10):
        yield i * 2

print(list(foo()))

print(map(list, foo()))