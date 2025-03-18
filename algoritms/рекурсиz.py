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
def count(numb):
    if not numb:
        return 0
    return 1 + count(numb[1:])


print(count(numb))
