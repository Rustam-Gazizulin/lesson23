with open('Евтушенко.txt', encoding='utf-8') as f:
    file_content = f.read()
    content = file_content.split('\n')


def my_gen(content):
    count = 0
    while count < 5:
        yield content[count]
        count += 1


fr = my_gen(content)
print(fr)
print(next(fr))
print(next(fr))
print(next(fr))


def squares(start, stop):
    for i in range(start, stop):
        yield i * i


generator = squares(1, 5)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
