'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
lst = [2, 3, 5, 9, 3]
avg = [lst[i] for i in range(1, len(lst), 2)]
print(lst)
print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum(avg)}')
    