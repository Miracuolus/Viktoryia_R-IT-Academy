import math

def generator(hi=math.inf):
    i = 0
    while i < hi:
        i += 1
        if i % 3 == 0:
            yield 'Василий'
        else:
            yield i

g = generator(200)
for j in g:
    print(j, end=', ')
