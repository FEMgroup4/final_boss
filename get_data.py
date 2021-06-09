# Получение из файла с данными массива информации
# Открываем файл для чтения с заданной кодировкой
# Проверяем первый символ. Если это "tab" - пишем в строку символ "&"
# В противном случае в строку пишем строки данных

def initial_data():
    with open("file.txt", 'r', encoding='utf8') as file:
        res_data = []
        for line in file:
            if not line.startswith('\t'):
                data = line.split(' ')  # Делим строку по символу "пробел"
                res_data.append(data)
            else:
                # Стартсимвол новой ячейки записи
                data = '&'
                res_data.append(data)
        res_data.append('&')    # Добавляем флаг окончания файла
    return res_data
