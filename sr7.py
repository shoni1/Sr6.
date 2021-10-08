try:
    n = int(input('Введите кол-во элементов массива:')) #Кол-во элементов массива
    a = [] #Создаем массив
    for i in range (n):
        a.append(int(input('Введите массив:'))) #Заполняем его
    delta = int(input('введите delta:')) #Вводим дельту
    counter = 0 #Создаем счетчик отличающихся элементов
    m=a[0]
    for i in range(n):
        if a[i]<m:
            m = a[i]
    for i in range (len(a)):
        if m + delta == a[i]:
            counter += 1
    print(counter)
except ValueError: 
    print('Это не число. Введите число.')

