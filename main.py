if __name__ == '__main__':
    pass

from ishodnye_dannye import ishodnye_vn_elsn, ishodnye_lac, ishodnye_ats

num = str(input('Введите последние две цифры номера зачетки: '))

main_type, main_voltage, reserve_type, reserve_voltage = ishodnye_vn_elsn(num)



print(main_type, main_voltage, reserve_type, reserve_voltage)
