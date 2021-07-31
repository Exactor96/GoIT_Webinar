def sort(l):
    return sorted(l)


def sort2(l):
    print(l)
    return sorted(l)

print(sort([]))

print(sort([3, 4, 2, 1]))
print(sort([2, 3, 1, 0, 'a', 'b']))

a = 10
b = a if a > 5 else 0

print(b)

num_list = [int(i) for i in input().split(' ')]
print(num_list)

s = input()
l3 = []
for i in s.split(' '):
    try:
        l3.append(float(i))
    except Exception as e:
        pass
print(l3)

def func1(a):
    return a + 10


func2 = lambda x: x + 10
print(func1(1))

d = {i: i for i in [1, 2, 3, 4, 5]}
print(d)
dd = {k: v + 10 for k, v in d.items()}
print(dd)

dd2 = {}
for k, v in d.items():
    dd2[k] = v + 10
print(d)
print(dd2)

print([i for i in filter(lambda x: x >= 10, [i for i in range(5, 15)])])

print('1', 1)
print(type('1'), type(1))
print(ord(b'A') == ord('A'), ord('A'))
print('П'.encode())
print('П'.encode('utf-8'))
# print('П'.encode('ascii'))
print('П'.encode('1251'))
