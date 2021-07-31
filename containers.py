from collections import namedtuple

nt = (
    ('name', 'Mick'),
    ('age', 5)
)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d.update({'a': 4})
#
# print(d)
# print(d.pop('b'))
# print(d)
# print(d.popitem())
# print(d)

Point = namedtuple('Point', ['x', 'y'])
print(*[1, 2, 3, 4, 5], **{'sep': r'/'})
def a(*args, **kwargs):
    print(args)
    print(kwargs)

a(*[1,2,3], **{'a': 'a', 'b': 'b'})