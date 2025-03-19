numb = [int(i) for i in input().split()]

def quick_sort(numb):
    if len(numb) < 2:
        return numb

    pivot = len(numb) // 2
    smaller = []
    bigger = []

    for i in numb[:pivot]:
        if i < numb[pivot]:
            smaller.append(i)
        elif i >= numb[pivot]:
            bigger.append(i)

    for i in numb[pivot + 1:]:
        if i < numb[pivot]:
            smaller.append(i)
        elif i > numb[pivot]:
            bigger.append(i)

    return quick_sort(smaller) + [numb[pivot]] + quick_sort(bigger)

print(quick_sort(numb))
