if __name__ == '__main__':
    print('Hello World!')

from ishodnye_dannye import ishodnye_dannye1

num = int(input('Введите последние две цифры номера зачетки: '))

main_type, main_voltage, reserve_type, reserve_voltage = ishodnye_dannye1(num)

print(main_type, main_voltage, reserve_type, reserve_voltage)


