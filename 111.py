street = "Кирова"
liters = ["А", "Б", "В", ""]
names = ["д", "д.", ""]
max_number = 3
list_build_data_liter = [f"{street},{name}{i}{liter}" for name in names for i in range(max_number, 0, -1) for liter in liters]

print(list_build_data_liter)

index = list_build_data_liter.index("Кирова,д1Б") + 1
print("индекс", index)
if index <= len(liters) + 1:
	liter_rez = liters[index - 1]
else:
	liter_rez = liters[index % len(liters) - 1]
print("Буква", liter_rez)

if index % len(liters) == 0:
	name_rez = names[len(liters) - 1]
else:
	print(index//len(liters))
	name_rez = index//len(liters) + 1
	print("name_rez ", name_rez)
	a = max_number -


#
# 5 liter = 2 (4 - длина списка)
# номер = 2 (Если остаток от деления 5 / длину списка номер = 0, то длина списка, иначе длина списка  + 1)
# имя = 1