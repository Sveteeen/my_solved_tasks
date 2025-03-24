numb = [int(i) for i in input().split()]

def quick_sort(numb):
    if len(numb) < 2:
        return numb

    pivot = len(numb) // 2
    smaller = []
    bigger = []

    for i in range(len(numb)):
        if i == pivot:
            continue
        if numb[i] < numb[pivot]:
            smaller.append(numb[i])
        elif numb[i] >= numb[pivot]:
            bigger.append(numb[i])


    return quick_sort(smaller) + [numb[pivot]] + quick_sort(bigger)

print(quick_sort(numb))
