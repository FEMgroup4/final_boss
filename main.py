# Основной файл программы
from get_data import initial_data
# from sort_data import sorting
from get_data_arrays import output
# from get_data_arrays import nodes_coord

# Получение данных из файла
res_data = initial_data()

# Пробный вывод массива информации
for row in res_data:
    for item in row:
        print(item, end=' ')
    print()

output()
# nodes_coord()
