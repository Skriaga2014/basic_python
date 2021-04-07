from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as bakery:
    if len(argv) == 1:
        for line in bakery:
            print(line[:-1])
    elif len(argv) == 2 and argv[1].isdigit():
        n = 1
        for line in bakery:
            if n >= int(argv[1]):
                print(line[:-1])
            n += 1
    elif len(argv) == 2 and argv[1].isdigit():
        n = 1
        for line in bakery:
            if n >= int(argv[1]):
                print(line[:-1])
            n += 1
    elif len(argv) == 3 and argv[1].isdigit() and argv[2].isdigit():
        n = 1
        for line in bakery:
            if n >= int(argv[1]) and n <= int(argv[2]):
                print(line[:-1])
            n += 1
    else:
        print('Введены неверные параметры')