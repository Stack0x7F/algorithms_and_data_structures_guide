def Stalin_sort(data: list) -> list:
    kept = [data[0]] # список для сохранения оставшихся значений, первый элемент по дефолту становится наименьшим
    maxSoFar = data[0] # максимум из пройденных элементов, изначально [0]
    for i in range(1, len(data)):
        if data[i] >= maxSoFar: 
            kept.append(data[i]) # в список добавляется элемент
            maxSoFar = data[i] # максимум обновляется
    
    return kept

unsorted_list = [1,4,2,3,6,5,5,7,7]

print(Stalin_sort(unsorted_list))

"""
лучший алгоритм сортировки эвер.

сложность O(n)
"""