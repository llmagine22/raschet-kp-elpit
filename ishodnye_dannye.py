import pandas as pd


def ishodnye_dannye1(num):
    a = int(str(num)[0])
    b = int(str(num)[1])

    # print(a, b)

    vn_elsn = abs(a - b)
    lac = abs(a - 1)
    ats = abs(a - 2)
    tg = abs(a - 3)
    deltaU = abs(b - 1)
    osn_nom = abs(b - 2)
    dop = abs(b - 3)

    new_number = f'{vn_elsn} {lac} {ats} {tg} {deltaU} {osn_nom} {dop}'
    print('Новый номер варианта: ', new_number)

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
    main_type = filtered_data["Основной Вид"].values[0]
    main_voltage = filtered_data["Напряжение основной"].values[0]
    reserve_type = filtered_data["Резервный вид"].values[0]
    reserve_voltage = filtered_data["Напряжение резервный"].values[0]

    # Проверка
    # print('Внешнее электроснабжение')
    # print(f"Основной Вид: {main_type}")
    # print(f"Напряжение основной: {main_voltage}")
    # print(f"Резервный вид: {reserve_type}")
    # print(f"Напряжение резервный: {reserve_voltage}")

    return int(main_type), int(main_voltage), int(reserve_type), int(reserve_voltage)
