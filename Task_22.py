'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
n = int(input('Введите первое число '))
m = int(input('Введите  второре число '))
num_n = []
num_m = []
print(num_n)
print(num_m)

for i in range(n):
    num_n.append(int(input('Введите значения первого списка: ')))
for j in range(m):
    num_m.append(int(input('Введите значения второго списка: ')))
num_l = []
for i in num_n:
     if i in num_m and i not in num_l:
            num_l.append(i)
num_l.sort()
print(num_l)


