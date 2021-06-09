# Сортируем данные списка
# Для начала разбиваем список на списки по темам
# Удаляем весь мусор из полученных списков
# Переводим строки в числа
# Объявим некоторые переменные
nodes = []          # Список с узлами
elements = []       # Список с элементами
pinning = []        # Список с закреплениями
forces = []         # Список с силами


# Функция разбивает общий список на отдельные списки
def splitting(data):
    if data[0] == '&':
        i = 1               # Счетчик для символов списка
        n = 0               # Счетчик для выбора массива
        while i != len(data):
            if n == 0:
                if data[i] == '&':
                    i += 1
                    n += 1
                else:
                    nodes.append(data[i])
                    i += 1
            elif n == 1:
                if data[i] == '&':
                    i += 1
                    n += 1
                else:
                    elements.append(data[i])
                    i += 1
            elif n == 2:
                if data[i] == '&':
                    i += 1
                    n += 1
                else:
                    pinning.append(data[i])
                    i += 1
            elif n == 3:
                if data[i] == '&':
                    i += 1
                    n += 1
                else:
                    forces.append(data[i])
                    i += 1
            else:
                print("Ошибка при сортировке массива: неверная структура файла")
    return nodes, elements, pinning, forces


# Функция для вывода списков
def output(nodes, elements, pinning, forces):
    print("Узлы:")
    for m in nodes:
        print(m, end='\n')
    print('\n')
    print("Элементы:")
    for m in elements:
        print(m, end='\n')
    print('\n')
    print("Закрепления:")
    for m in pinning:
        print(m, end='\n')
    print('\n')
    print("Силы:")
    for m in forces:
        print(m, end='\n')


# Функция, убирающая мусор из списка с узлами
def sorting_nodes():
    i = 0                   # Счетчик для списка nodes
    sort = []               # Отсортированный список узлов
    while i != len(nodes):  # Избавляемся от символа новой строки
        temp = nodes[i]
        string = temp[len(temp) - 1]
        string = string[:4]
        temp[len(temp) - 1] = string
        sort.append(temp)
        i += 1
    num_list = []
    num = []
    for row in sort:        # Переводим стоки в числа
        for item in row:
            n = str_to_num(item)
            if n is not None:
                num.append(str_to_num(item))
        num_list.append(num)
        num = []
    return num_list


# Функция, убирающая мусор из списка с элементами
def sorting_elements():
    i = 0                       # Счетчик для списка nodes
    sort = []                   # Отсортированный список узлов
    while i != len(elements):   # Избавляемся от символа новой строки
        temp = elements[i]
        string = temp[len(temp) - 1]
        string = string[:4]
        temp[len(temp) - 1] = string
        sort.append(temp)
        i += 1
    num_list = []
    num = []
    for row in sort:        # Переводим стоки в числа
        for item in row:
            n = str_to_num(item)
            if n is not None:
                num.append(str_to_num(item))
        num_list.append(num)
        num = []
    return num_list


# Функция, убирающая мусор из списка с закреплениями
def sorting_pinning():
    i = 0                       # Счетчик для списка nodes
    sort = []                   # Отсортированный список узлов
    while i != len(pinning):   # Избавляемся от символа новой строки
        temp = pinning[i]
        string = temp[len(temp) - 1]
        string = string[:1]
        temp[len(temp) - 1] = string
        sort.append(temp)
        i += 1
    num_list = []
    num = []
    for row in sort:  # Переводим стоки в числа
        for item in row:
            n = str_to_num(item)
            if n is not None:
                num.append(str_to_num(item))
        num_list.append(num)
        num = []
    return num_list


# Функция, убирающая мусор из списка с силами
def sorting_forces():
    i = 0                        # Счетчик для списка nodes
    sort = []                    # Отсортированный список узлов
    while i != len(forces):      # Избавляемся от символа новой строки
        if i != (len(forces) - 1):
            temp = forces[i]
            string = temp[len(temp) - 1]
            string = string[:4]
            temp[len(temp) - 1] = string
            sort.append(temp)
            i += 1
        else:
            sort.append(forces[i])
            i += 1
    num_list = []
    num = []
    for row in sort:  # Переводим стоки в числа
        for item in row:
            n = str_to_num(item)
            if n is not None:
                num.append(str_to_num(item))
        num_list.append(num)
        num = []
    return num_list


# Функция, превращающая строку в число
def str_to_num(s):
    if '.' in s and s.replace('.', '').isdigit():
        return float(s)
    elif s.isdigit():
        return int(s)


# Основная функция, включающая все остальные
def sorting(data):
    nodes, elements, pinning, forces = splitting(data)
    nodes = sorting_nodes()
    elements = sorting_elements()
    pinning = sorting_pinning()
    forces = sorting_forces()
    #output(nodes, elements, pinning, forces)
    return nodes, elements, pinning, forces
