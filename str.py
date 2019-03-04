word = 'Архангельск'

# Вывести последнюю букву в слове
print(word[-1])

# Вывести количество букв а в слове
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
a = 0
for i in word.lower():
    if i in 'аеёиоуыэюя':
        a += 1
print(a)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
a = len(sentence.split())
print(a)

# Вывести первую букву каждого слова на отдельной строке
for i in sentence.split():
    print(i[0][0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

a = 0
for i in sentence.split():
    a += len(i)
print(a/ len(sentence.split()))

