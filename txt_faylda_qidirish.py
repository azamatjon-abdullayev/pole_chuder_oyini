

import csv    #togrisi va haqiqiy
with open("C:/Users/user/Desktop/rrr.txt", encoding='utf-8') as r_file:

    file_reader = csv.DictReader(r_file, delimiter = ",")

    count = 0

    for row in file_reader:
        if count == 0:

            print(f'Файл содержит столбцы: {", ".join(row)}')

        print(f' {row["ismlar"]} - {row["fam"]}', end='') # ismlar ,fam, yoshi
        print(f' va u {row["tugilgan_yili"]} yil tugilgan.')
        count += 1


import io
word = input("Qidiring = ")
with io.open("C:/Users/user/Desktop/rrr.txt", encoding="utf-8") as file:
    for line in file:
        if word in line:
            print(line, end="")



