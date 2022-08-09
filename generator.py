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
