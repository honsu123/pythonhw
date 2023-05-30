#  Требуется найти в массиве A[1..N] самый близкий 
#  по величине элемент к заданному числу X. 
#  Пользователь в первой строке вводит натуральное 
#  число N – количество элементов в массиве. 
#  В последующих  строках записаны N целых чисел Ai. 
#  Последняя строка содержит число X
from random import randint
my_list = list()
lens = int(input("Введите длинну списка: "))

for i in range(lens):
    my_list.append(randint(0, 10))
print(my_list)

num = int(input("Введите число: "))
max_ = 0
for i in my_list:
    if max_ < i and i < num:
        max_ = i
print(max_)
