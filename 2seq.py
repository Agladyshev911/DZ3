import re
elements = input('Введите любые цифры через запятую, слэш или точку с запятой: ')
list_elements = re.split(",|/|;", elements)

for i, item in enumerate(list_elements):
    list_elements[i] = int(item)

unique_list_elements = list(set(list_elements))

unique_list_elements = ",".join(map(str, unique_list_elements))

print(f'Уникальные элементы получившегося списка: {unique_list_elements}')
