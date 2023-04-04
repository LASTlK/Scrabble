# Задача Скрабл

'''en_point = {1: 'AEIOULNSTR',
            2: 'DG',
            3: 'BCMP',
            4: 'FHVWY',
            5: 'K',
            8: 'JX',
            10: 'QZ'}

ru_point = {1: 'АВЕИНОРСТ',
            2: 'ДКЛМПУ',
            3: 'БГЁЬЯ',
            4: 'ЙЫ',
            5: 'ЖЗХЦЧ',
            8: 'ШЕЮ',
            10: 'ФЩЪ'}

y = input('Введите язык (ru/en): ')
x = input('Введите слово: ').upper()

if y == 'en':
    res = [key for i in x for key, value in en_point.items() if i in value]
    print(sum(res))
else:
    res = [key for i in x for key, value in ru_point.items() if i in value]
    print(sum(res))'''


# Номер 4.5

'''x = int(input('Введите число: '))
res = 1
for i in range(1, x):
    res *= i

print(f'Факториал числа {x} равен {res * x})'''


# Номер 4.7

'''x = int(input('Введите число: '))
y = 0
for i in range(1, x + 1):
    y += i
for i in range(x - 1):
    y -= int(input())
print(y)'''