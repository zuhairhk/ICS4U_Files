def eras(n):
    a = [True] * n

    a[0], a[1] = False

    for i in range(2, (n * 0.5) + 1):
        if a[i] == True:
            x = 0
            for j in range(n + 1):
                if ((i * i) + (x * i)) < n:
                    a[j] = False
    
    for a[i] == True in range(n + 1):
        return a[i]

print(eras(100))