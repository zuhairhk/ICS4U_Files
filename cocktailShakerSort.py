def cocktailShaker(a):
    sIndex = 0
    eIndex = int(len(a) - 1)
    swapped = True

    while swapped:
        swapped = False

        for i in range(sIndex, eIndex):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        eIndex -= 1

        for i in range(eIndex-1, sIndex-1, -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        sIndex += 1

    return a

from random import randrange

a = [randrange(-10, 10) for i in range(10)]
print('Non sorted list is ---->', a)
print('Sorted list using cocktail shaker sort is ---->', cocktailShaker(a))