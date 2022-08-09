with open('Евтушенко.txt', encoding='utf-8') as f:
    file_content = f.read()
    content = file_content.split('\n')
    it = iter(content)
for _ in range(4):
    f = next(it)
    print(f)


