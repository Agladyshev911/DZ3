list = []
list_elements = int(input('Введите количество элементов списка: '))
for i in range(list_elements):
    list.append(int(input("Введите элемент " + str(i+1) + ": ")))
list.sort()
print(f'Ваш список: {list}')

