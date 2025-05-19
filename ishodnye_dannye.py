import pandas as pd


def ishodnye_vn_elsn(num):
    a = int(str(num)[0])
    b = int(str(num)[1])
    vn_elsn = abs(a - b)
    lac = abs(a - 1)
    ats = abs(a - 2)
    tg = abs(a - 3)
    deltaU = abs(b - 1)
    osn_nom = abs(b - 2)
    dop = abs(b - 3)

    # new_number = f'{vn_elsn} {lac} {ats} {tg} {deltaU} {osn_nom} {dop}'
    print('Новый номер варианта: ', f'{vn_elsn}{lac}{ats}{tg}{deltaU}{osn_nom}{dop}')

    # Создаем таблицу (DataFrame) для внешнего электроснабжения
    data_vn_elsn = {
        "Вариант": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "Основной Вид": [1, 5, 1, 3, 2, 1, 2, 1, 3, 1],
        "Напряжение основной": [380, 380, 380, 380, 380, 380, 220, 380, 220, 380],
        "Резервный вид": [3, 2, 3, 4, 4, 5, 2, 3, 5, 2],
        "Напряжение резервный": [220, 380, 220, 380, 380, 380, 380, 380, 380, 380]
    }

    df = pd.DataFrame(data_vn_elsn)  # Создание DataFrame

    # Словарь соответствий
    mapping = {
        1: "Подстанция районных энергосистем",
        2: "Тяговая подстанция",
        3: "Электростанция промышленного предприятия",
        4: "Дизель-генераторная электростанция",
        5: "Высоковольтная линия СЦБ (ВЛ СЦБ)"
    }

    # Замена чисел на названия
    df["Основной Вид"] = df["Основной Вид"].replace(mapping)
    df["Резервный вид"] = df["Резервный вид"].replace(mapping)

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

    return str(main_type), int(main_voltage), str(reserve_type), int(reserve_voltage)


def ishodnye_big(num):
    a = int(str(num)[0])
    b = int(str(num)[1])

    lac = abs(a - 1)
    ats = abs(a - 2)
    tg = abs(a - 3)
    deltaU = abs(b - 1)
    osn_nom = abs(b - 2)
    dop = abs(b - 3)

    data_big = {
        "Вариант": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "Лац 24": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        "Лац 48": [7, 12, 17, 54, 47, 15, 40, 20, 42, 22],
        "Лац 60": [8, 42, 18, 15, 23, 40, 25, 10, 16, 27],
        "Лац 220": [1.5, 3, 4.5, 6, 4.5, 6, 9, 9, 12, 12],
        "Атс 48": [12, 34, 6, 20, 31, 10, 22, 33, 12, 30],
        "Атс 60": [6, 30, 15, 13, 6, 12, 18, 14, 31, 26],
        "Атс 220": [0, 1.5, 3, 0, 1.5, 2, 0, 1.5, 3, 0],
        "Тг 220": [1.5, 2, 0, 2.5, 3, 0, 3, 6, 5, 6],
        "ΔU24": ['21,5-28', '21,5-28', '21,5-28', '21-26', '21-26', '21-26', '21,5-28', '21,5-28', '21,5-28',
                 '21,5-28'],
        "ΔU48": ['43-50', '43-56', '43-56', '43-50', '43-50', '43-50', '43-56', '43-56', '43-50', '43-50'],
        "ΔU60": ['54-62', '54-62', '54-72', '54-72', '54-62', '54-62', '54-72', '54-72', '54-62', '54-62'],
        "Система": ['48/24', '24/48', '60/24', '48/60', '24/60', '60/48', 0, 0, 0, 0],
        "Освещение гарант": [1, 1.5, 2.5, 4, 5, 6.5, 8, 9.5, 11, 12],
        "Освещение негарант": [2, 4, 6, 8, 10, 15, 20, 25, 30, 35],
        "Силовое оборудование": [9, 10.5, 12, 19, 23, 35, 38, 42, 48, 50],
        "cos": [0.65, 0.67, 0.68, 0.85, 0.79, 0.68, 0.79, 0.77, 0.76, 0.75],

    }

    df = pd.DataFrame(data_big)  # Создание DataFrame

    # Словарь соответствий
    mapping = {
        0: "Централизованная",

    }

    df["Система"] = df["Система"].replace(mapping)

    #
    #
    #

    # Фильтрация данных для Лац
    filtered_data = df[df["Вариант"] == lac]
    lac24 = filtered_data["Лац 24"].values[0]
    lac48 = filtered_data["Лац 48"].values[0]
    lac60 = filtered_data["Лац 60"].values[0]
    lac220 = filtered_data["Лац 220"].values[0]

    # Фильтрация данных для Атс
    filtered_data = df[df["Вариант"] == ats]
    ats24 = filtered_data["Атс 24"].values[0]
    ats48 = filtered_data["Атс 48"].values[0]
    ats60 = filtered_data["Атс 60"].values[0]
    ats220 = filtered_data["Атс 220"].values[0]

    # Фильтрация данных для Тг
    filtered_data = df[df["Вариант"] == tg]
    tg220 = filtered_data["Тг 220"].values[0]

    # Фильтрация данных для ΔU
    filtered_data = df[df["Вариант"] == deltaU]
    deltaU24 = filtered_data["ΔU24"].values[0]
    deltaU48 = filtered_data["ΔU48"].values[0]
    deltaU60 = filtered_data["ΔU60"].values[0]

    # Фильтрация данных для Системы
    filtered_data = df[df["Вариант"] == osn_nom]
    system = filtered_data["Система"].values[0]
    if system != 0:
        system = str(f'Комбинированная {filtered_data["Система"].values[0]}')
    else:
        pass

    # Фильтрация данных для Освещения
    filtered_data = df[df["Вариант"] == dop]
    osv_gar = filtered_data["Освещение гарант"].values[0]
    osv_negar = filtered_data["Освещение негарант"].values[0]
    sil = filtered_data["Силовое оборудование"].values[0]
    cos = filtered_data["cos"].values[0]

    return 0


