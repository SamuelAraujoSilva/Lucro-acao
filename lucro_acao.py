array = input()

k = [int(n) for n in list(array.split(','))]

maior_lucro = 0

for index, a in enumerate(k):
    for b in k[:index:-1]:
        lucro = b - a
        if lucro > 0 and lucro > maior_lucro:
            maior_lucro = lucro

print(maior_lucro)