import random as rd
invenory={'зелье':1,'меч':7,'шлем':3,'лук':5,'да':10}
sum=0
while(input('Добавить предмет в рюкзак ?')!='no'):
    c=input('Введите название предмта')
    d=int(input('Введите вес предмета'))
    invenory[c]=d
    for value in invenory.values():
        sum += value
        if (sum > 50):
            print('Иневентарь пелеполнен')
            exit()
print(invenory)
if(input('Удалить предмет из инвенторя ')=='yes'):
    c=input('Какой предмет удалить?')
    del invenory[c]
print(invenory)
