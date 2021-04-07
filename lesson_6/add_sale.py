from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as sale:
    sale.write(argv[1] + '\n')