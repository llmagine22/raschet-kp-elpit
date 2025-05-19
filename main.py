if __name__ == '__main__':
    pass

from ishodnye_dannye import ishodnye_vn_elsn, ishodnye_big

num = str(input('Введите последние две цифры номера зачетки: '))

main_type, main_voltage, reserve_type, reserve_voltage = ishodnye_vn_elsn(num)

print(main_type, main_voltage, reserve_type, reserve_voltage)

lac24, lac48, lac60, lac220, ats48, ats60, ats220, tg220, deltaU24, deltaU48, deltaU60, system, osv_gar, osv_negar, sil, cos = ishodnye_big(
    num)

print(lac24, lac48, lac60,
      lac220, ats48, ats60, ats220, tg220, deltaU24, deltaU48, deltaU60, system, osv_gar, osv_negar, sil, cos)
