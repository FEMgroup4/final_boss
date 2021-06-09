# Приводим отсортированные значения из файла к значениям, с 
# Добавляем сортировку
from sort_data import sorting
from get_data import initial_data

# Задаем некоторые переменные
nodes = []          # Список с узлами
elements = []       # Список с элементами
pinning = []        # Список с закреплениями
forces = []         # Список с силами


# Получение данных из файла
res_data = initial_data()

# Сортировка полученных данных и приведение их к необходимому виду
nodes, elements, pinning, forces = sorting(res_data)

# Получим количество элементов
nodes_quantity = len(nodes)

# Функция получения списка с координатами узлов
def nodes_coord():
    i = 0
    sort = []
    while i != len(nodes):
        temp = nodes[i]
        sort.append(temp[1])
        i += 1
    return sort


nodes_fin = nodes_coord()

# Функция получения списка с силами
def forces_list():
    i = 0       # Счетчик для списка forces
    k = 0       # Счетчик для нового списка сил
    flag = 0    # Флаг конца списка forces
    sort = []
    while k != nodes_quantity:          # Проверка номера узла
        temp = forces[i]
        if temp[0] != k:                # Если силы в узле нет
            sort.append(0)
            k += 1
        else:                           # Если сила в узле есть
            sort.append(temp[1])
            k += 1
            if i < len(forces) - 1:     # Проверка, чтобы значение не вышло за пределы forces
                i += 1
    return sort


forces_fin = forces_list()

# Тестовый вывод
def output():
    print("\nКоличество узлов: ", nodes_quantity, '\n')
    print("Координаты узлов:")
    for m in nodes_fin:
        print(m, end='\n')
    print("\nЗначения сил по узлам:")
    for m in forces_fin:
        print(m, end='\n')
