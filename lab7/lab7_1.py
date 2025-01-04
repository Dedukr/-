def main():
	def show(dic):
		for i in dic:
			print(
				f"{i} has area of {dic.get(i)[0]} with population of {dic.get(i)[1]} and is located in {dic.get(i)[2]}")

	def add(dic):
		name = input("What country do you want to add?\n").title()
		if not name:
			return print("Not valid input")
		if name in dic:
			return print(f"There is already a record about this country:\n{dic.get(name)}")
		area = input("Enter the area of the country:\n")
		if not area.isdigit():
			return print("Not valid input")
		population = input("Enter the population of the country:\n")
		if not population.isdigit():
			return print("Not valid input")
		continent = input("Enter the continent of that country:\n")
		dic[name] = [area, population, continent]
		print(f"\nSuccessfully added {name}")

	def delete(dic):
		el = input("What country record do you want to delete?\n").title()
		try:
			dic.pop(el)
			print(f"\nSuccessfully deleted {el}")
		except:
			return print("Not valid country")

	def show_sorted(dic):
		dic = dict(sorted(dic.items()))
		show(dic)

	def is_Africa_or_Asia(dic):
		set = ("Africa", "Asia")
		for i in dic.keys():
			if dic.get(i)[2] in set:
				print(i)

	countries = {"Ukraine": [603_700, 41_167_335, "Europe"], "Ethiopia": [1_104_300, 132_900_000, "Africa"],
	             "Poland": [312_685, 37_766_327, "Europe"], "Cote d'ivoire": [322_462, 30_900_000, "Africa"],
	             "UK": [244_376, 68_265_209, "Europe"], "China": [9_596_961, 1_409_670_000, "Asia"],
	             "Canada": [9_984_670, 41_288_599, "America"], "India": [3_287_263, 1_428_627_663, "Asia"],
	             "Niger": [1_267_000, 26_342_784, "Africa"], "Singapore": [735.6, 6_040_000, "Asia"]}

	while True:
		ans = int(input(
			"\nWhat do you want to do?\n1. Show all\n2. Add new country\n3. Remove a country record\n4. Show sorted list of countries\n5. Check if Africa or Asia\n6. Exit\n(Enter the number)\n"))
		match ans:
			case 1:
				show(countries)
			case 2:
				add(countries)
			case 3:
				delete(countries)
			case 4:
				show_sorted(countries)
			case 5:
				is_Africa_or_Asia(countries)
			case 6:
				print("Goodbye")
				break
			case _:
				print("Enter the correct number")
				continue


if __name__ == "__main__":
	main()
