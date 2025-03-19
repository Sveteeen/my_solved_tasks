#сумма массива 
numb = [int(i) for i in input().split()]

def summ(numb):
    if len(numb) == 0:
        return 0
    if len(numb) == 1:
        return numb[0]
    return numb[0] + summ(numb[1:])


print(summ(numb))


#максимум в массиве

numb = [int(i) for i in input().split()]

def maxim(numb):
    if len(numb) == 1:
        return numb[0]
    return max(numb[0], maxim(numb[1:]))


print(maxim(numb))

#подсчет количества элементов в массиве
numb = [int(i) for i in input().split()]
def count(numb):
    if not numb:
        return 0
    return 1 + count(numb[1:])


print(count(numb))

'''
Задача о монетках
Дано: число — денежная сумма, которую
надо собрать из монет номиналом 3 или 5
Надо: определить, можно ли собрать эту
сумму Пример:
7 — нельзя
17 — можно (3, 3, 3, 3, 5)
'''

