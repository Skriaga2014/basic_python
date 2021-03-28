'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя
ключевое слово yield, например:

odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...

2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield.
'''

n = 16
result = [i for i in range(1, n + 1) if i % 2 == 0]
print(result)