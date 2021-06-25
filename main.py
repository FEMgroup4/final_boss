# -*- coding: utf-8 -*-

# Необходимо для вывода

from get_data_arrays import output

# Стартовая точка программы
if __name__ == "__main__":
    from get_data_arrays import nodes_quantity as uz_num, nodes_fin as nodes_fin, forces_fin as usiliya, pinning
# nodes_quantity - количество узлов
# nodes_fin - координаты узлов
# forces_fin - список сил по узлам

# Функция добавления необходимых данных по элементам
def adding():
    temp = []
    for i in range(0, uz_num - 1):
        print('Значение для элемента ', i)
        temp.append(int(input()))
    print('Итоговый результат:', temp)
    des = input("Хотите изменить? (Да/Нет)")
    if des == "Да":
        temp = adding()
    return temp

print('Определим недостающие данные.')
print('Warning! Все данные вводятся исключительно в численном формате и не должны содержать иных символов. '
      'В противном случае, разработчик не несет ответственности за результаты вычисления.')
print('1. Задайте длины элементов.')
el_length = adding()
print('2. Задайте жёсткости элементов.')
gestkosti = adding()
# Выдадим юзеру его чертежи

balka = []
def chertezUzlov():
    print('Расчётная схема балки в масштабе')
    for i in range(1, uz_num+1):
        if usiliya[i-1] == 0:
            balka.append('-'*el_length[i-2])
        else:
            balka.append('-'*el_length[i-2]+ ' F = '+ str(usiliya[i-1]))
    balka[0] = "||"
    balka.append("||")
    print(balka)
    return balka
chertezUzlov()

# обьявление вспомогательной матрицы
arrayG = [[1, -1],
          [-1, 1]]

# формируем заготовку для массива матриц жесткостей
arrayGes = []
for i in range(uz_num-1):
    arrayGes.append([])
    for j in range(len(arrayG)):
        arrayGes[i].append([])
# на выходе получим [  [ [], [] ],  [ [], [] ],
#                      [ [], [] ],  [ [], [] ]  ]

# считаем матрицу жесткостей элементов
def makeMatricaGestcosti():
    for i in range(uz_num-1):
        for j in range(len(arrayG)):
            for k in range(len(arrayG[j])):
                arrayGes[i][j].append(float(gestkosti[i]) * float(arrayG[j][k]))
    return arrayGes

makeMatricaGestcosti()
# выводим матрицы жесткостей элементов
def vivod(arrayGes):
    k = 0
    for i in range(len(arrayGes)):
        for j in range(len(arrayGes[i])):
            if k % 2 == 0:
                print('Матрица жесткости ', i + 1, '-го элемента: \n', arrayGes[i][j])
                k += 1
            else:
                print('', arrayGes[i][j])
        k = 0

vivod(arrayGes)
print('')

#Делаем вспомогательный список
matGes = []
for i in range(len(gestkosti) + 1):
    matGes.append([])

# считаем матрицу жесткости системы
def makeMatricaGestcostiSistemi():
    #Задаём первый элемент
    matGes[0].append(arrayGes[0][0][0])
    for i in range(len(gestkosti) + 1):
        for j in range(len(gestkosti) + 1):
            #Если элемент на диагонали
            if i == j and i != 0 and i != len(gestkosti):
                matGes[i].append(arrayGes[i][0][0] + arrayGes[i - 1][0][0])
            #Если выше диагонали
            elif j == i - 1 and i != 0 and i != len(gestkosti) + 1:
                matGes[i].append(arrayGes[i - 1][0][1])
            #Если ниже диагонали
            elif j == i + 1 and i != len(gestkosti) + 1:
                matGes[i].append(arrayGes[i][0][1])
            elif j != i and j != -1 and i != -1:
                matGes[i].append(0)
    matGes[-1].append(arrayGes[-1][0][0])
    return matGes


makeMatricaGestcostiSistemi()

print('Матрица жесткости системы')
for i in range(len(matGes)):
    print(matGes[i])
print('')

def vvodGranichnihUsloviy():
    for i in range(len(matGes)):
        for j in range(len(matGes[i])):
            if j == 0 or j == len(matGes) - 1 or i == 0 or i == len(matGes) - 1:
                matGes[i][j] = 0
    matGes[0][0] = 1
    matGes[-1][-1] = 1
    return matGes

vvodGranichnihUsloviy()

print('Матрица жесткости системы с граничными условиями')
for i in range(len(matGes)):
    print(matGes[i])
print('')

print('\n' + 'Конец моей части')
