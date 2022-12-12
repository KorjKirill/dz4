from random import randint
n = 50
mas1 = []
mas2=[]
for i in range(n):
    mas1.append(randint(1, 99))
print(mas1)
mas2=[]
for i in range(n):
    mas2.append(randint(1, 99))
print(mas2)
masrav=[]
for i in range(n):
    for j in range(n):
        if (mas1[i]==mas2[j]):
            masrav.append(mas1[i])

print("В обоих есть ",masrav)
print('Есть в первно, но нет во втром ',list(set(mas1).difference(mas2)))
print('Есть во втромо, но нет в первом',list(set(mas2).difference(mas1)))
print('Входит в первый или во втрой(не в оба сразу)',list(set(mas1).difference(mas2)),list(set(mas2).difference(mas1)))

