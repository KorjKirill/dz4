from random import randint
n = 10
mas = []
for i in range(n):
    mas.append(randint(1, 99))
print(mas)

for i in range(n - 1):
    for j in range(n - i - 1):
        if mas[j] > mas[j + 1]:
            temp=mas[j]
            mas[j] = mas[j + 1]
            mas[j + 1] = temp

print(mas)