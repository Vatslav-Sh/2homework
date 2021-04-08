

def _filter(i, f):
    for e in f:
        if i(e):
            yield e

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(_filter(lambda x: x % 2 == 0, (iter(lst)))))

# second way

def _filter(lst):
    yield [item for item in lst if item % 2 == 0]

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [print(item) for item in _filter(lst)]








