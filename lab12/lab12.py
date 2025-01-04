import json


def main():
	def Open(name, mode):
		try:
			return open(name, mode, encoding="utf-8")
		except:
			print(f"There was an error while opening file {name}")
			return None

	def read(filename):
		file = Open(filename, 'r')
		data = json.load(file)
		file.close()
		return data

	def show(filename):
		data = read(filename)
		for i in data:
			print(
				f"{i} has area of {data.get(i)[0]} with population of {data.get(i)[1]} and is located in {data.get(i)[2]}")

	def add(filename):
		data = read(filename)
		name = input("What country do you want to add?\n")
		if not name:
			return print("Not valid input")
		if name in data:
			return print(f"There is already a record about this country:\n{data.get(name)}")
		area = input("Enter the area of the country:\n")
		if not area.isdigit():
			return print("Not valid input")
		population = input("Enter the population of the country:\n")
		if not population.isdigit():
			return print("Not valid input")
		continent = input("Enter the continent of that country:\n")

		data[name] = [area, population, continent]

		file = Open(filename, "w")
		json.dump(data, file, indent=4)
		file.close()

	def delete(filename):
		el = input("What country record do you want to delete?\n")
		data = read(filename)
		try:
			data.pop(el)
			file = Open(filename, "w")
			json.dump(data, file, indent=4)
			file.close()
		except:
			return print("Not valid country")

	def show_sorted(filename):
		file = Open(filename, 'r')
		data = json.load(file)
		data = dict(sorted(data.items()))
		for i in data:
			print(
				f"{i} has area of {data.get(i)[0]} with population of {data.get(i)[1]} and is located in {data.get(i)[2]}")

	def search(filename):
		data = read(filename)
		density = float(input("What value do you want to search for?\n"))
		for i in data.keys():
			if data.get(i)[1] / data.get(i)[0] >= density:
				print(
					f"{i} has area of {data.get(i)[0]} with population of {data.get(i)[1]} and its population density is {data.get(i)[1] / data.get(i)[0]}")

	def is_Africa_or_Asia(filename):
		set = ("Africa", "Asia")
		data = read(filename)
		for i in data.keys():
			if data.get(i)[2] in set:
				print(i)

	countries = {"Ukraine": [603_700, 41_167_335, "Europe"], "Ethiopia": [1_104_300, 132_900_000, "Africa"],
	             "Poland": [312_685, 37_766_327, "Europe"], "Cote d'ivoire": [322_462, 30_900_000, "Africa"],
	             "UK": [244_376, 68_265_209, "Europe"], "China": [9_596_961, 1_409_670_000, "Asia"],
	             "Canada": [9_984_670, 41_288_599, "America"], "India": [3_287_263, 1_428_627_663, "Asia"],
	             "Niger": [1_267_000, 26_342_784, "Africa"], "Japan": [377975, 123970000, "Asia"]}

	filename = "file.json"
	file = Open(filename, "w")
	file.write(json.dumps(countries, indent=4))
	file.close()

	while True:
		ans = int(input(
			"\nWhat do you want to do?\n1. Show all\n2. Add new country\n3. Remove a country record\n4. Search by population density\n5. Show sorted list of countries\n6. Check if Africa or Asia\n7. Exit\n(Enter the number)\n"))
		match ans:
			case 1:
				show(filename)
			case 2:
				add(filename)
			case 3:
				delete(filename)
			case 4:
				search(filename)
			case 5:
				show_sorted(filename)
			case 6:
				is_Africa_or_Asia(filename)
			case 7:
				break
			case _:
				print("Enter the correct number")
				continue


if __name__ == "__main__":
	main()
