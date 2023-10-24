import math


def sondan_kichik_uchga_bolinmaydi(son: int): # <- return shu yerga qaytadi
    current_num = 0
    while current_num < son: #<- Shu yerga qaytadi continue
        current_num += 1
        if current_num % 3 == 0:
            continue
        print(f'{current_num} 3ga bo\'linmaydi')

sondan_kichik_uchga_bolinmaydi(100)