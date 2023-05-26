from openpyxl import load_workbook

from PyQt5 import QtCore, QtWidgets
import re

# app = QtWidgets.QApplication([])
# wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
# print(wb_patch)
# wb = load_workbook(wb_patch)
wb1 = load_workbook('C:/AdressClear/Src/table_input.xlsx')
table_input = wb1.active

wb2 = load_workbook("C:/AdressClear/Src/street_list.xlsx")
street_list = wb2.active

wb3 = load_workbook("C:/AdressClear/Src/snt_list.xlsx")
snt_list = wb3.active

# print(sheet_reestr_ul.max_row)



def generate_list(input_adress, street): # генерирует список сочетаний для поиска зданий
    liters = ["А", "Б", "В", "Г", "Д", "Е", "Е", "Ж", "З", "а", "б", "в", "г", "д", "ж", "з", ""]
    names = ["д", "д.", "дом", "здание", "зд.", "дом.", "строение", ""]
    # liters = ["А", "Б", ""]
    # names = ["д", "д.", ""]
    list_build_data_liter = [f"{street},{name}{i}{liter}" for name in names for i in range(200, 0, -1) for liter in liters]
    return(list_build_data_liter, liters)

def get_number_build(input_adress, generate_adress ):  # возвращает найденную строку со значением улицы и здания
    number_build = "None"
    for number_build in generate_adress:
        index = input_adress.find(number_build)
        if index > 0:
            break
        else:
            number_build = "None"
    return number_build

def get_build(input_adress, street):     # возвращает номер здания
    list_build_data_liter, liters = generate_list(input_adress, street)
    number_build = get_number_build(input_adress, list_build_data_liter)
    if number_build != "None":
        number = make_num_build(list_build_data_liter, liters, number_build)
        print("Адрес здания: ", number_build)
        print("Номер: ", number)

def make_num_build(list_build_data_liter, liters, number_build):
    max_number = 200
    index = list_build_data_liter.index(number_build) + 1
    # print("индекс", index)

    # -------------------------------------------------------------------------------------
    # print("На краю или в середине index % len(liters)", index % len(liters))

    if index % len(liters) == 0:
        name_rez = index // len(liters)
        # print("В какую секцию попадает????  index//len(liters) = ", name_rez)

    else:
        name_rez = index // len(liters) + 1
        # print("В какую секцию попадает???? name_rez ", name_rez)
        # print("отстаток от деления на количество номеров", name_rez%max_number)

    # print("отстаток от деления на количество номеров", name_rez%max_number)

    if name_rez == 1:
        # print("ssdf\sdf",index)
        number = max_number
        # print(number)
    else:
        if name_rez % max_number == 0:
            number = 1
        else:
            number = max_number + 1 - name_rez % max_number
    # print(number)
    # ---------------------------------------------------------------------------------------------

    # print("len(liters)", len(liters))

    if index <= len(liters):
        liter_rez = liters[index - 1]
    else:
        if index % len(liters) == 0:
            liter_rez = liters[index % len(liters) - 1]
        else:
            liter_rez = liters[index - len(liters) * (name_rez - 1) - 1]

    # print("Буква", liter_rez)
    # print("-----------------")

    build = f"{number}{liter_rez}"
    # print(build)
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
    # print(input_adress)
    snt = get_snt(input_adress)
    # print(snt)
    street = get_street(input_adress)
    print("Улица: ", street)
    if street != "None":
        build = get_build(input_adress, street)
