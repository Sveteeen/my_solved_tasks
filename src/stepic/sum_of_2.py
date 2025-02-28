'''Сумма двух
На вход подается список чисел и целевое число на отдельной строке. Верните индексы двух чисел, которые в сумме дают целевое число.

Любые входные данные имеют только 1 решение и один и тот же элемент списка не нужно использовать дважды.

Индексы можно вернуть в любом порядке.

Sample Input:

2,7,11,15
9
Sample Output:

[0, 1]'''

x = [int(i) for i in input().split(',')]
y = int(input())
j = sorted(x)
index1 = 0
index2 = len(x) - 1
while j[index1] + j[index2] != y:
    if j[index1] + j[index2] > y:
        index2 -= 1
    else:
        index1 += 1

res = [x.index(j[index1]), x.index(j[index2])]
if x.index(j[index1]) == x.index(j[index2]):
    res = [x.index(j[index1]), x.index(j[index2], x.index(j[index1]) + 1, len(x))]
if x.index(j[index1]) > x.index(j[index2]):
    res = [x.index(j[index2]), x.index(j[index1])]
print(res)

'''
1:
2,7,11,15
9

2:
3,2,4
6

3:
3,3
6

5:
-1, -2, -3, -4, -5
-8
'''
