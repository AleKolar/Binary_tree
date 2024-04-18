'''Линейный поиск
Алгоритм линейного поиска определяется на таких структурах данных как массивы,
списки и надстройки над ними — очередь и стек. Такой алгоритм является «решением в лоб»
и сводится к перебору одного элемента за другим и операции сравнения на каждом. Как правило,
линейный поиск применяется к неотсортированным структурам.'''

def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

#array = list(map(int, input().split()))
#element = int(input())
array = [1, 3, 3, 3, 4, 6, 7, 9, 7]
element = 3

print(find(array, element))

def count(array, element):
    for a in array:
        if a == element:
            return array.count(a)
    return False

    #return False

#array = list(map(int, input().split()))
#element = int(input())

array = [1, 3, 3, 3, 4, 6, 7, 9, 7, 3, 3]
element = 3

print(count(array, element))

'''Двоичный поиск
Алгоритм двоичного поиска является более совершенным, чем линейный поиск, однако он накладывает на структуру сильное 
ограничение — она должна быть отсортирована.

Допустим, что у нас стоит такая же задача — найти индекс определённого элемента в массиве. В связи с тем, 
что алгоритм может искать только в отсортированном массиве, используем генератор последовательных чисел range. 
Суть двоичного поиска сводится к тому, что на каждой итерации размер исследуемого массива уменьшается в 2 раза.'''

def binary_search(array, element, left, right):
    if left > right or left >= len(array):  # если левая граница превысила превысила правую или длину массива,
        return False  # значит, элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

#element = int(input())
element = 55
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(f'Index of number {element}:', binary_search(array, element, 0, 99))

'''Сортировка пузырьком'''

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

'''Cортировки вставками'''

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x