from openpyxl import load_workbook

from PyQt5 import QtCore, QtWidgets
import re

import func

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
    # print(input_adress)
    snt = get_snt(input_adress)
    # print(snt)
    street = get_street(input_adress)
    print("Улица: ", street)
    if street != "None":
        build = func.getBuild(input_adress, street)
        print("Здание", build)


