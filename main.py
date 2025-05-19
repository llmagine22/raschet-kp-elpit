# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pandas as pd

num = int(input('Введите последние две цифры номера зачетки: '))
a = int(str(num)[0])
b = int(str(num)[1])

print(a, b)

vn_elsn = abs(a - b)
lac = abs(a - 1)
ats = abs(a - 2)
tg = abs(a - 3)
delta_U = abs(b - 1)
osn_nom = abs(b - 2)
dop = abs(b - 3)

print('Новый номер варианта: ', vn_elsn, lac, ats, tg, delta_U, osn_nom, dop)

# Создаем таблицу (DataFrame) для внешнего электроснабжения
data1 = {
    "Вариант": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "Основной Вид": [1, 5, 1, 3, 2, 1, 2, 1, 3, 1],
    "Напряжение основной": [380, 380, 380, 380, 380, 380, 220, 380, 220, 380],
    "Резервный вид": [3, 2, 3, 4, 4, 5, 2, 3, 5, 2],
    "Напряжение резервный": [220, 380, 220, 380, 380, 380, 380, 380, 380, 380]
}

df = pd.DataFrame(data1)  # Создание DataFrame

# Фильтрация данных для варианта "n"
filtered_data = df[df["Вариант"] == vn_elsn]

# Записываем значения в отдельные переменные
main_type_1 = filtered_data["Основной Вид"].values[0]
main_voltage_1 = filtered_data["Напряжение основной"].values[0]
reserve_type_1 = filtered_data["Резервный вид"].values[0]
reserve_voltage_1 = filtered_data["Напряжение резервный"].values[0]

# Выводим переменные
print('Внешнее электроснабжение')
print(f"Основной Вид: {main_type_1}")
print(f"Напряжение основной: {main_voltage_1}")
print(f"Резервный вид: {reserve_type_1}")
print(f"Напряжение резервный: {reserve_voltage_1}")
