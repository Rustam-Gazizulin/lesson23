with open('Евтушенко.txt', encoding='utf-8') as f:
    file_content = f.read()
    lines = file_content.split('\n')
    for line in lines[:4]:
        print(line)

print(lines[:4])

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
