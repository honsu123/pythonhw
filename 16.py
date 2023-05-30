# Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в 
# массиве. В последующих  строках записаны N целых 
# чисел Ai. Последняя строка содержит число X
from random import randint
my_list = list()
lens = int(input("Введите длинну списка: "))

for i in range(lens):
    my_list.append(randint(0, 10))
print(my_list)

num = int(input("Введите число: "))
count = 0

for i in my_list:
    if i == num:
        count += 1
print(count)