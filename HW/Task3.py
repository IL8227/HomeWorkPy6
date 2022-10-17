# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# старый код

lst = [2, 3, 5, 6]
result_lst = []
for i in range((len(lst)+1)//2):
    result_lst.append(lst[i]*lst[len(lst)-1-i])    
print(result_lst)

# новый код
lst = [2, 3, 5, 6]
result_lst = []
print([result_lst.append(lst[i]*lst[len(lst)-1-i]) for i in range((len(lst)+1)//2)])  
print(result_lst)