# Создайте программу-переводчик, которая хранит перевод
#  слов с русского языка на английский.
# После запуска программа выводит список слов в словаре 
# и предлагает пользователю ввести слово для перевода. 
# Если введенного слова нет в словаре выводится сообщение "нет такого слова".
# Используйте словари для словаря:)
rueng = {'один':'one', 'два':'two', 'три':'three', 'четыре':'four',
         'пять':'five', 'шесть':'six', 'семь':'seven', 'восемь':'eight',
         'девять':'nine', 'десять':'ten', 'яблоко':'apple', 'груша':'pear',
         'апельсин':'orange', 'персик':'peach', 'банан':'banana', 'клубника':'strawberry'}
print(rueng[input()])