def generate_list(input_adress, street): # генерирует список сочетаний для поиска зданий
    liters = ["А", "Б", "В", "Г", "Д", "Е", "Е", "Ж", "З", "а", "б", "в", "г", "д", "ж", "з", ""]
    names = ["д", "д.", "дом", "здание", "зд.", "дом.", "строение", ""]
    list_build_data_liter = [f"{street},{name}{i}{liter}" for name in names for i in range(200, 0, -1) for liter in liters]
    return(list_build_data_liter, liters)

def get_number_build(input_adress, generate_adress ):  # возвращает найденную строку со значением улицы и здания "Кирова,16Г"
    number_build = "None"
    for number_build in generate_adress:
        index = input_adress.find(number_build)
        if index > 0:
            break
        else:
            number_build = "None"
    return number_build

def make_num_build(list_build_data_liter, liters, number_build):  # Возвращает номер здания "16Г"
    max_number = 200
    index = list_build_data_liter.index(number_build) + 1
    # -------------------------------------------------------------------------------------
    if index % len(liters) == 0:
        name_rez = index // len(liters)
    else:
        name_rez = index // len(liters) + 1
    if name_rez == 1:
        number = max_number
    else:
        if name_rez % max_number == 0:
            number = 1
        else:
            number = max_number + 1 - name_rez % max_number
    # ---------------------------------------------------------------------------------------------
    if index <= len(liters):
        liter_rez = liters[index - 1]
    else:
        if index % len(liters) == 0:
            liter_rez = liters[index % len(liters) - 1]
        else:
            liter_rez = liters[index - len(liters) * (name_rez - 1) - 1]
    build = f"{number}{liter_rez}"
    return build

def getBuild(input_adress, street):     # Главная функция - возвращает номер здания
    list_build_data_liter, liters = generate_list(input_adress, street)
    number_build = get_number_build(input_adress, list_build_data_liter)
    number = number_build
    if number_build != "None":
        number = make_num_build(list_build_data_liter, liters, number_build)
        # print("Адрес здания: ", number_build)
        # print("Номер: ", number)
    return number

