sacos = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
n = 5
c = 0

for i in sacos[n:]:
    verd = False
    j = c
    for _ in range(n - 1):
        for k in sacos[j+1:i+1]:
            if sacos[j] + k == i:
                verd = True
                break

        if verd:
            break
        j += 1

    if not verd:
        print('errado = ', i)
    c += 1
