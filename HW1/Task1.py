# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 




from this import d


lst = [2,3,5,9,3]
s_odd = 0
# for i in range(len(lst)):
#     if i % 2 != 0:
#         s_odd += lst[i]
print(lst)
# print(s_odd)


# r = [i % 2 != 0 for i in range(len(lst))]

r = [i % 2 != 0 for i, d in enumerate(lst)]
print()
