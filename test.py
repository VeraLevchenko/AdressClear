from openpyxl import load_workbook
from PyQt5 import QtCore, QtWidgets
import re

# app = QtWidgets.QApplication([])
# wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
# print(wb_patch)
# wb = load_workbook(wb_patch)
wb1 = load_workbook('D:/AdressClear/Src/table_input.xlsx')
table_input = wb1.active

wb2 = load_workbook("D:/AdressClear/Src/street_list.xlsx")
street_list = wb2.active

wb3 = load_workbook("D:/AdressClear/Src/snt_list.xlsx")
snt_list = wb3.active

# print(sheet_reestr_ul.max_row)
# ------------------------Поиск названия улицы----------------------------------------------------

def get_build1(input_adress, street):
    build = "None"
    # liters = ["А", "Б", "В", "Г", "Д", "Е", "Е", "Ж", "З", "а", "б", "в", "г", "д", "ж", "з", ""]
    # names = ["д", "д.", "дом", "здание", "зд.", "дом.", "строение", ]
    liters = ["А", "Б", ""]
    names = ["д", "д.", ""]
    list_build_data_liter = [f"{street},{name}{i}{liter}" for name in names for i in range(2, 0, -1) for liter in liters]
    list_build_liter = [f"{street},{i}{liter}" for liter in liters for i in range(2, 0, -1)]

    print(list_build_data_liter)
def get_build(input_adress, street):
    build = "None"
    get_build1(input_adress, street)

    for j in range(1, snt_list.max_row + 1):
        snt = snt_list[j][0].value
        index = input_adress.find(snt)
        if index > 0:
            break
        else:
            snt = "None"
    return build



def get_snt(input_adress):
    snt = "None"
    for j in range(1, snt_list.max_row + 1):
        snt = snt_list[j][0].value
        index = input_adress.find(snt)
        if index > 0:
            break
        else:
            snt = "None"
    return snt

def get_street(input_adress):
    street = "None"
    for j in range(1, street_list.max_row + 1):
        street = street_list[j][0].value
        index = input_adress.find(street)
        if index > 0:
            break
        else:
            street = "None"
    return street




# перебирает адреса
for i in range(1, table_input.max_row + 1):
    input_adress = str(table_input[i][16].value)
    print(input_adress)
    input_adress = input_adress.replace("-", '')
    input_adress = input_adress.replace(" ", '')
    input_adress = input_adress.replace("№", '')
    input_adress = input_adress.replace("Кемеровскаяобл", '')
    input_adress = input_adress.replace("обл.Кемеровская", '')
    print(input_adress)
    snt = get_snt(input_adress)
    print(snt)
    street = get_street(input_adress)
    print(street)
    build = get_build(input_adress, street)

#     ul = get_ul(adres, snt)
#     sheet[i][3].value = ul
#     adres_without_ul = get_adres_without_ul(adres, ul)
#     numbers = get_number(adres_without_ul)
#     k = 4
#     # -----записывает числа из адреса в столбцы
#     for number in numbers:
#         sheet[i][k].value = number
#         k += 1
# wb.save('D:/project_Python/Adress_clear/source.xlsx')
# # app.exec()
