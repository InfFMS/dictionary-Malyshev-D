# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
with open('parameters.txt',encoding='utf-8') as f:
    text = f.read()
sets = {}
mas = text.split('\t')
mas1 = []
for i in range(len(mas)):
    if '//' not in mas[i]:
        mas1.append(mas[i])
mas1 = (''.join(mas1)).split('\n')
rez = []
for i in range(len(mas1)):
    if mas1[i] != '':
        rez.append(mas1[i])
for i in range(len(rez)):
    rez[i] = rez[i].split()
    sets[rez[i][0]] = ' '.join(rez[i][1:len(rez[i])])
print(sets)