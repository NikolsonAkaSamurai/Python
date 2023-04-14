import matplotlib.pyplot as plt
import random

# генерация 20 рандомных чисел в диапазоне от 0 до 50
data = [random.randint(0, 50) for i in range(20)]

# создание графика
plt.plot(data)

# добавление названий осей
plt.xlabel('Номер элемента')
plt.ylabel('Значение')

# добавление заголовка графика
plt.title('Рандомные числа')

# отображение графика
plt.show()
