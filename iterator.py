with open('Евтушенко.txt', encoding='utf-8') as f:
    file_content = f.read()
    content = file_content.split('\n')
    it = iter(content)
for _ in range(8):
    f = next(it)
    if 'потоков' in f:
        print(f)


