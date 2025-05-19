import pandas as pd


def ishodnye_vn_elsn(num):
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

# Вот бы кто-нибудь вбил большую таблицу за меня...

    return str(main_type), int(main_voltage), str(reserve_type), int(reserve_voltage)

def ishodnye_lac(num):
    a = int(str(num)[0])
    b = int(str(num)[1])

    lac = abs(a - 1)
    ats = abs(a - 2)
    tg = abs(a - 3)
    deltaU = abs(b - 1)
    osn_nom = abs(b - 2)
    dop = abs(b - 3)

    data_lac = {
        "Вариант": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "Лац 24": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        "Лац 48": [7, 12, 17, 54, 47, 15, 40, 20, 42, 22],
        "Лац 60": [8, 42, 18, 15, 23, 40, 25, 10, 16, 27],
        "Лац 220": [1.5, 3, 4.5, 6, 4.5, 6, 9, 9, 12, 12]
    }

    df = pd.DataFrame(data_lac)  # Создание DataFrame

    return 0


def ishodnye_ats(num):
    a = int(str(num)[0])
    b = int(str(num)[1])

    ats = abs(a - 2)
    tg = abs(a - 3)
    deltaU = abs(b - 1)
    osn_nom = abs(b - 2)
    dop = abs(b - 3)

    data_ats = {
        "Вариант": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "Атс 48": [12, 34, 6, 20, 31, 10, 22, 33, 12, 30],
        "Атс 60": [6, 30, 15, 13, 6, 12, 18, 14, 31, 26],
        "Атс 220": [0, 1.5, 3, 0, 1.5, 2, 0, 1.5, 3, 0]
    }

    df = pd.DataFrame(data_ats)  # Создание DataFrame

    return 0