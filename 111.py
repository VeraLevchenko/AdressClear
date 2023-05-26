street = "Кирова"
liters = ["А", "Б", ""]
names = ["д"]
max_number = 2
list_build_data_liter = [f"{street},{name}{i}{liter}" for name in names for i in range(max_number, 0, -1) for liter in liters]

# print(list_build_data_liter)

index = list_build_data_liter.index("Кирова,д1А") + 1
print("индекс", index)




# -------------------------------------------------------------------------------------
print("На краю или в середине index % len(liters)", index % len(liters))

if index % len(liters) == 0:
	name_rez = index//len(liters)
	print("В какую секцию попадает????  index//len(liters) = ", name_rez)

else:
	name_rez = index//len(liters) + 1
	print("В какую секцию попадает???? name_rez ", name_rez)
	# print("отстаток от деления на количество номеров", name_rez%max_number)

print("отстаток от деления на количество номеров", name_rez%max_number)

if name_rez == 1:
	print("ssdf\sdf",index)
	number = max_number
	print(number)
else:
	if name_rez%max_number == 0:
		number = 1
	else:
		number = max_number + 1 - name_rez%max_number
print(number)
#---------------------------------------------------------------------------------------------

print("len(liters)", len(liters))

if index <= len(liters):
	liter_rez = liters[index - 1]
else:
	if index % len(liters) == 0:
		liter_rez = liters[index % len(liters) - 1]
	else:
		liter_rez = liters[index - len(liters) * (name_rez-1) - 1]

print("Буква", liter_rez)
print("-----------------")

build = f"{number}{liter_rez}"
print(build)