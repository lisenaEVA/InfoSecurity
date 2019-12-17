alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
text = open('text_code.txt', encoding='utf-8')
temp = open('temp.txt', encoding='utf-8')


def create_dic(f):  # функция создания словаря
    dic = {}
    for line in f:
        str_len = len(line)  # Возвращает число элементов
        i = 0
        while i < str_len:
            c = line[i]
            if c not in alpha:
                i += 1
                continue

            if dic.get(c) == None:  # возвращает значение ключа, но если его нет возвращает None
                dic[c] = 1
            else:
                dic[c] = dic[c] + 1
            i = i + 1
    return dic


def lisst(temp):  # создаем словарь, превращаем в кортеж и сортируем

    dic_temp = create_dic(temp)  # создаем словарь шаблона
    list_dic_temp = list(dic_temp.items())  # создаем списки кортежей и сортируем его по первым элементам пар
    list_dic_temp.sort(key=lambda i: i[1])  # сортируем
    return list_dic_temp


list_dic_temp = lisst(temp)
list_dic_text = lisst(text)
print(list_dic_temp)
while True:
    res = ''
    fin = (list_dic_temp[-1])
    fin2 = (list_dic_text[-1])
    fin1 = fin[0]
    fin2 = fin2[0]
    print(fin1)
    print(fin2)
    sd = alpha.index(fin2[0]) - alpha.index(fin1[0])

    cod_text = open('text_code.txt', encoding='utf-8')
    for line in cod_text:

        i = 0
        while i < len(line):
            c = line[i]
            if c not in alpha:
                i += 1
                res += c

            else:
                c1 = alpha[(alpha.index(c) + sd) % len(alpha)]
                res += c1
                i += 1

    list_dic_text.pop(-1)
    print(res)
    result = input('текст читается?')
    if result == 'у':
        break