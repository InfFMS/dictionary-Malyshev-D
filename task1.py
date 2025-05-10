# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
strkeys = input()
strvalues = input()
keys = strkeys.split()
values = strvalues.split()
mydict = {}
for i in range(len(keys)):
    mydict[keys[i]] = int(values[i])
print(mydict)