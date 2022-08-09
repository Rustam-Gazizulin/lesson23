with open('Евтушенко.txt', encoding='utf-8') as f:
    file_content = f.read()
    lines = file_content.split('\n')
    for line in lines[:4]:
        print(line)
print('=' * 40)


with open('Евтушенко.txt', encoding='utf-8') as f:
    counter = 0
    while True:
        try:
            line = next(f)
        except StopIteration:
            break
        print(line)
        counter += 1
        if counter > 3:
            break
print('=' * 40)

l = [1, 2, 3, 4, 5]
it = iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it, 'STOP'))
print('=' * 40)
print(list(it))
print('=' * 40)


class MyIter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        if self.n > self.current:
            buf = self.current
            self.current += 2
            return buf
        else:
            raise StopIteration


it = MyIter(8)

# it = iter(it)

print(next(it))
print(next(it))
print(list(it))

